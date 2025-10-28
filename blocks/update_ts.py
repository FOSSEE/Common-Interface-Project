#!/usr/bin/env python3

import os
import sqlite3
import subprocess
from datetime import datetime, timezone

# === CONFIG ===
DB_PATH = "xcosblocks.sqlite3"
STATIC_BASE = "eda-frontend/src/static/gallery"
TABLE_NAME = "saveAPI_gallery"
MEDIA_COL = "media"
SAVE_TIME_COL = "save_time"


def get_git_commit_time(file_path):
    """Return latest commit time (UTC datetime) for given file."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%at", "--", file_path],
            capture_output=True,
            text=True,
            check=True,
        )
        ts = result.stdout.strip()
        print(f"Git log time for {file_path}: {ts}")
        if not ts:
            return None
        return datetime.fromtimestamp(int(ts), tz=timezone.utc)
    except subprocess.CalledProcessError:
        return None


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(f"SELECT id, {MEDIA_COL} FROM {TABLE_NAME}")
    rows = cur.fetchall()

    updated = 0
    skipped = 0

    for row in rows:
        row_id, media_path = row
        file_path = os.path.join(STATIC_BASE, media_path)

        if not os.path.exists(file_path):
            print(f"⚠️  Missing file: {file_path}")
            skipped += 1
            continue

        commit_time = get_git_commit_time(file_path)
        if not commit_time:
            print(f"⚠️  No git log for {file_path}")
            skipped += 1
            continue

        cur.execute(
            f"UPDATE {TABLE_NAME} SET {SAVE_TIME_COL} = ? WHERE id = ?",
            (commit_time.isoformat(), row_id),
        )
        print(f"✅ Updated {media_path} → {commit_time}")
        updated += 1

    conn.commit()
    conn.close()

    print(f"\nDone. Updated {updated}, skipped {skipped}.")


if __name__ == "__main__":
    main()
