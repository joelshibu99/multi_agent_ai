# Multi-Agent AI File Processor

## Objective

This project implements a multi-agent AI system that processes files in **PDF**, **JSON**, and **Email (TXT/EML)** formats. The system detects file types and classifies intent (e.g., *Invoice*, *Request for Quote (RFQ)*, *Complaint*) before routing the file content to a dedicated processing agent.

It includes a shared memory system for logging and coordination between agents, enabling traceability and batch or web-based processing.

---

## Overview

### Agents

- **Classifier Agent**  
  Identifies the file format and intent, and dispatches the content to the appropriate agent.

- **JSON Agent**  
  Processes structured JSON files by validating required fields and detecting missing ones.

- **Email Agent**  
  Extracts metadata (sender, urgency) and identifies the intent from raw email text.

### Shared Memory

- A lightweight SQLite-based logging system that stores:
  - File metadata
  - Extracted content
  - Format and intent classification
  - Thread IDs for contextual continuity

---

## Features

- Automatic format detection (PDF, JSON, Email)
- Intent classification using keyword heuristics and field matching
- Modular agent-based architecture
- SQLite logging for auditability and debugging
- Batch processing via command line
- Flask-based web interface for real-time uploads and results
- Clean, structured JSON output

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/multi-agent-ai.git
cd multi-agent-ai
````

### 2. Create and activate a virtual environment

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Program

### Option 1: Batch Processing (Command Line)

1. Place test files (`.pdf`, `.json`, `.txt`, `.eml`) into the `data/` directory.
2. Run the batch processor:

```bash
python batch_process.py
```

This will display format, intent, and extracted information in the console.

---

### Option 2: Web Interface (Flask App)

1. Start the Flask development server:

```bash
python web/app.py
```

2. Open a browser and navigate to:

```
http://127.0.0.1:5000
```

3. Upload a file and view the structured result in the web interface.

---

## How It Works

1. The user uploads or provides a file path.
2. The **Classifier Agent** determines the format and classifies the intent.
3. Based on the result, the file is routed to:

   * `JSONAgent` for structured validation
   * `EmailAgent` for text parsing
   * PDF content is extracted using `PyMuPDF` and then classified
4. Extracted data is logged in the SQLite database.
5. Output is returned as structured JSON.

---

## Dependencies

* Python 3.x
* Flask
* PyMuPDF (`fitz`)
* SQLite3 (default in Python)
* Standard Python libraries: `json`, `os`, `tempfile`, `sqlite3`, etc.

Install them via:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
multi-agent-ai/
├── agents/
│   ├── classifier_agent.py
│   ├── email_agent.py
│   └── json_agent.py
├── memory/
│   └── shared_memory.py
├── utils/
│   └── file_parser.py
├── data/
│   ├── sample_email.txt
│   ├── sample_invoice.pdf
│   └── sample_data.json
├── web/
│   ├── app.py
│   └── templates/
│       └── index.html
├── batch_process.py
├── requirements.txt
└── README.md
```

---

## Notes

* Ensure test files are placed in the `data/` folder before batch execution.
* The SQLite database `shared_memory.db` is created on the first run automatically.
* The system is modular and can be extended by adding new agents or refining intent detection logic.

---

