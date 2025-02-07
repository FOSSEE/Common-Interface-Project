from datetime import datetime
import json
import os
import shutil
import sqlite3


def update_media_column(db_path, table_name):
    """
    Updates the media column in the table to store '<save_id>.png' based on the save_id value.
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # SQL to update the media column
        sql = f"UPDATE {table_name} SET media = save_id || '.png';"

        # Execute the update query
        cursor.execute(sql)

        # Commit the changes
        conn.commit()
        print(f"Media column in '{table_name}' updated successfully.")

    except sqlite3.Error as e:
        print(f"An error occurred while updating the media column: {e}")

    finally:
        # Close the database connection
        if conn:
            conn.close()


def join_and_copy_images(db_path, statesave_table, gallery_table):
    try:
        # Connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # SQL to join the tables on 'description' and fetch image_path and media
        sql = f"""
        SELECT s.base64_image, g.media
        FROM {statesave_table} AS s
        JOIN {gallery_table} AS g ON s.description = g.description;
        """

        # Execute the query to fetch the data
        cursor.execute(sql)
        rows = cursor.fetchall()

        if not rows:
            print(f"No matching records found in {statesave_table} and {gallery_table}.")
            return

        # Loop over each pair and run the copy command
        for row in rows:
            image_path, media_path = row
            source_path = f"file_storage/{image_path}"
            destination_path = f"eda-frontend/src/static/gallery/{media_path}"

            # Copy the image to the media path
            try:
                shutil.copyfile(source_path, destination_path)
                print(f"Copied {source_path} to {destination_path}")
            except Exception as e:
                print(f"Error copying {source_path} to {destination_path}: {e}")

        print("All image copy operations completed.")

    except sqlite3.Error as e:
        print(f"An error occurred while querying the database: {e}")

    finally:
        # Close the database connection
        if conn:
            conn.close()


# Example usage
if __name__ == "__main__":
    # Path to your SQLite database
    database_path = "xcosblocks.sqlite3"

    # Table to work with
    table_name = "saveAPI_gallery"
    statesave_table = "saveAPI_statesave"

    update_media_column(database_path, table_name)

    join_and_copy_images(database_path, statesave_table, table_name)
