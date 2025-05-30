# Multi-Agent AI File Processor

## Objective

Build a multi-agent AI system that accepts files in **PDF**, **JSON**, or **Email (text)** formats, automatically classifies the format and intent, and routes the input to the appropriate specialized agent for processing. The system maintains shared context (e.g., sender, topic, last extracted fields) for chaining, traceability, and logging.

This system is designed to simplify and automate document processing workflows, making it easier to extract relevant data and organize unstructured inputs efficiently.

---

## Overview

The system includes three main agents:

- **Classifier Agent:** Detects the file format and intent (e.g., Invoice, RFQ, Complaint) and routes the content to the correct agent.
- **JSON Agent:** Processes structured JSON files, validates required fields, and flags anomalies.
- **Email Agent:** Extracts sender, subject, urgency, and intent from email content.

A lightweight shared memory module (using SQLite) stores logs and extracted data for traceability and multi-agent coordination.

---

## Features

- Automatic detection of input format (PDF, JSON, Email).
- Intent classification based on keywords or JSON fields.
- Modular agents specialized in handling different data types.
- Persistent shared memory for logging and context retention.
- Batch processing of files from a directory.
- Web interface for uploading and processing files interactively.
- Structured JSON output of extracted data.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/multi-agent-ai.git
cd multi-agent-ai
Create and activate a virtual environment:


python -m venv venv
source venv/bin/activate    
Install required dependencies:


pip install -r requirements.txt
Place your files (PDF, JSON, Email .txt) in the data/ folder.

Run the batch processing script:

python batch_process.py
The system will classify and process each file, then print structured results to the console.

Start the Flask server:

python web/app.py
Open your browser and go to: http://127.0.0.1:5000
Upload a file and view the extracted information instantly.

How It Works

User uploads a file.
The Classifier Agent detects file format and intent.

The file content is routed to the appropriate agent:

JSON Agent processes structured JSON.
Email Agent parses emails for sender, urgency, and intent.
PDF files are extracted as text and classified.
Extracted data and logs are stored in the Shared Memory SQLite database.
Results are returned in a clear, structured JSON format.

Dependencies

Python 3.x
Flask
PyMuPDF (fitz) for PDF extraction
SQLite3 (built-in with Python)
Other standard libraries (json, os, tempfile)

Project Structure

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

Notes
Ensure sample files are placed in data/ for testing.

The SQLite database shared_memory.db is created automatically on first run.

The web interface provides an easy way to upload and test single files interactively.

The system is extensible: you can add more agents or intents as needed.

Enjoy using the Multi-Agent AI File Processor for your document automation needs!