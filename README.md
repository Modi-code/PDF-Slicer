# PDF Page Slicer Utility

A lightweight Python desktop script that opens a graphical interface (GUI) allowing users to select a PDF file and split it into individual, sequentially numbered single-page PDF files.

## Features
* **No Hardcoded Paths:** Uses interactive `tkinter` file and directory dialogs.
* **Safety Checks:** Automatically detects cancelled actions and handles missing folders.
* **Sequential Numbering:** Tracks and renames pages cleanly using a starting offset counter.

## Tech Stack
* Python 3
* `pypdf` (PDF manipulation library)
* `tkinter` (File/Directory dialogs)

## How to Use
```bash
# 1. Clone the repository
git clone https://github.com/Modi-code/PDF-Slicer.git
cd PDF-Slicer

# 2. Install the required dependency
pip install pypdf

# 3. Run the application
python .idea\Slicer.py
