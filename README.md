# Mini Industrial Data Orchestration Pipeline

This project is a small academic prototype that simulates an industrial data orchestration workflow. Sample files are mock inputs used to simulate machine-generated data; the focus is on orchestration logic rather than dataset size.

## Concept
The goal is to demonstrate orchestration logic rather than production infrastructure.

## Architecture
- SMB share simulated via filesystem
- Orchestrator implemented in Python
- Raw data stored in blob storage (filesystem)
- Metadata indexed in a relational database (SQLite, MariaDB simulation)

## What the orchestrator does
1. Detects new files in an SMB-like folder
2. Moves raw data to blob storage
3. Indexes metadata in a relational database

## Technologies
- Python
- SQLite
- File-based storage
- Data orchestration concepts

## Note
This project focuses on system understanding and orchestration concepts.
