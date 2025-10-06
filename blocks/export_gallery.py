import os
from os.path import abspath, join
from pathlib import Path
import re
import sqlite3
import subprocess

# --- Configuration ---
# Path to your Django SQLite database file
DB_PATH = "xcosblocks.sqlite3"

# Table to work with
table_name = "saveAPI_gallery"

# Base directory where exports will be stored
EXPORT_BASE_DIR = Path("uploads")

SCILAB_DIR = "../../scilab_for_xcos_on_cloud"
SCILAB_DIR = abspath(SCILAB_DIR)
SCILAB = join(SCILAB_DIR, "bin", "scilab-adv-cli")

SCILAB_START = (
    "try;funcprot(0);lines(0,120);"
    "clearfun('messagebox');"
    "function messagebox(msg,title,icon,buttons,modal),disp(msg),endfunction;"
    "function xinfo(msg),disp(msg),endfunction;"
    "funcprot(1);"
    "catch;[error_message,error_number,error_line,error_func]=lasterror();"
    "disp(error_message,error_number,error_line,error_func);exit(3);end;"
)
SCILAB_END = (
    "catch;[error_message,error_number,error_line,error_func]=lasterror();"
    "disp(error_message,error_number,error_line,error_func);exit(2);end;exit;"
)

SCILAB_CMD = [
    SCILAB,
    "-noatomsautoload",
    "-nogui",
    "-nouserstartup",
    "-nb",
    "-nw",
    "-e",
    SCILAB_START,
]

LOGFILEFD = 123


def sanitize_filename(filename: str) -> str:
    """Replace unsafe filesystem characters with '_'."""
    return re.sub(r'[\\/:"*?<>|]+', "_", filename)


def handle_line(current_line, line):
    line = line.rstrip()
    if line.endswith("..."):
        # Remove continuation and add to buffer
        current_line += line.rstrip(".").rstrip() + " "
        complete_line = False
    else:
        if current_line:
            current_line += line
        else:
            current_line = line
        complete_line = True
    return current_line, complete_line


def handle_script(script_dump, f):
    current_line = ""

    lines = script_dump.splitlines()

    if not lines:
        return

    for line in lines:
        current_line, complete_line = handle_line(current_line, line)
        if complete_line:
            f.write(current_line.rstrip() + "\n")
            current_line = ""

    # Write remaining line if any
    if current_line:
        f.write(current_line.rstrip() + "\n")


def export_gallery_row(row):
    """
    Export one gallery row to xcos (and optionally sci) file.
    row is a dict with keys same as column names.
    """
    name = sanitize_filename(row["name"])
    data_dump = row["data_dump"]
    script_dump = row["script_dump"]

    folder_path = EXPORT_BASE_DIR / name
    folder_path.mkdir(parents=True, exist_ok=True)

    # --- Export .xcos ---
    xcos_path = f"{folder_path}/{name}.xcos"
    with open(xcos_path, "w", encoding="utf-8") as f:
        f.write(data_dump)
    print(f"✅ Saved Xcos file: {xcos_path}")

    # --- Export .sci (optional) ---
    if script_dump:
        sci_path = f"{folder_path}/{name}.sci"
        with open(sci_path, "w", encoding="utf-8") as f:
            f.write(script_dump)
        print(f"✅ Saved Script file: {sci_path}")
        wfname = run_scilab(folder_path, sci_path)
    else:
        wfname = ""

    log_file = f"{folder_path}/output.txt"
    with open(log_file, "w") as f:
        proc = subprocess.run(
            ["xcosformat.sh", xcos_path],
            stdout=f,
            stderr=subprocess.STDOUT,
        )
        rc = proc.returncode
        if rc != 0:
            print(f"❌ Failed: xcosformat.sh {xcos_path}: code: {rc}")
        else:
            print(f"✅ Ran: xcosformat.sh {xcos_path}")
            proc = subprocess.run(
                ["xcos2xml/replacesplitblocks.sh", xcos_path, wfname],
                stdout=f,
                stderr=subprocess.STDOUT,
            )
            rc = proc.returncode
            if rc != 0:
                print(
                    f"❌ Failed: xcos2xml/replacesplitblocks.sh {xcos_path} {wfname}: rc: {rc}"
                )
            else:
                print(f"✅ Ran: xcos2xml/replacesplitblocks.sh {xcos_path} {wfname}")


def run_scilab(folder_path, sci_path):
    log_name = f"{folder_path}/scilab-log.txt"
    logfilefd = os.open(log_name, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)

    if logfilefd != LOGFILEFD:
        os.dup2(logfilefd, LOGFILEFD)
        os.close(logfilefd)

    proc = subprocess.Popen(
        SCILAB_CMD,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        start_new_session=True,
        universal_newlines=True,
        pass_fds=(LOGFILEFD,),
    )

    os.close(LOGFILEFD)

    wfname = f"{folder_path}/workspace.dat"
    command = f"exec('{sci_path}');save('{wfname}');"
    cmd = "try;" + command + SCILAB_END + "\n"
    proc.stdin.write(cmd)
    proc.stdin.flush()
    (stdout, stderr) = proc.communicate()
    rc = proc.returncode
    if rc != 0:
        print(f"❌ Scilab failed: {sci_path}: return code {rc}: log {log_name}")
        print(f"--- Scilab stdout ---\n{stdout}")
        print(f"--- Scilab stderr ---\n{stderr}")
        return ""
    else:
        print(f"✅ Saved Workspace file: {wfname}")
        return wfname


def main():
    EXPORT_BASE_DIR.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # access columns by name

    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT id, save_id, name, data_dump, script_dump
        FROM {table_name}
    """)

    for row in cursor.fetchall():
        export_gallery_row(row)

    conn.close()


if __name__ == "__main__":
    main()
