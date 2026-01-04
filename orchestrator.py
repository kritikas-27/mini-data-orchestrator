"""
Orchestrator responsibility:
- Detect new images in SMB share
- Move image to blob storage
- Store metadata in relational database
"""
import sqlite3
from pathlib import Path

DB_PATH = Path("database/metadata.db")

def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS image_metadata (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            source TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


import shutil
from datetime import datetime

SMB_DIR = Path("smb_share/images")
BLOB_DIR = Path("blob_storage/images")

def image_workflow(image_path):
    """
    Workflow:
    1. Store raw image in blob storage
    2. Index metadata in relational DB
    """

    BLOB_DIR.mkdir(parents=True, exist_ok=True)

    target = BLOB_DIR / image_path.name
    shutil.move(image_path, target)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO image_metadata (filename, source, timestamp) VALUES (?, ?, ?)",
        (image_path.name, "TRUMPF_MACHINE", datetime.utcnow().isoformat())
    )

    conn.commit()
    conn.close()

    print(f"[ORCHESTRATOR] Image processed: {image_path.name}")


def detect_new_images():
    SMB_DIR.mkdir(parents=True, exist_ok=True)

    for image in SMB_DIR.iterdir():
        if image.is_file():
            image_workflow(image)

if __name__ == "__main__":
    init_db()
    detect_new_images()
