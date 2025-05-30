from utils.file_parser import detect_format, extract_content

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, filepath, file_format, content):
        intent = "Unknown"
        text_content = ""
        sender = None
        subject = None
        urgency = "Normal"

        if file_format == 'Email':
            # content here is the full email text
            text_content = content if isinstance(content, str) else ""
            lines = text_content.splitlines()

            # simple extraction for From and Subject
            for line in lines:
                if line.lower().startswith("from:"):
                    sender = line[5:].strip()
                elif line.lower().startswith("subject:"):
                    subject = line[8:].strip()

            text = text_content.lower()
            if "invoice" in text:
                intent = "Invoice"
            elif "rfq" in text or "request for quote" in text:
                intent = "RFQ"
            elif "complaint" in text:
                intent = "Complaint"
            elif "urgent" in text:
                intent = "Urgent"
                urgency = "High"
            else:
                intent = "General"

        elif file_format == 'PDF':
            text_content = content if isinstance(content, str) else ""
            text = text_content.lower()
            if "invoice" in text:
                intent = "Invoice"
            elif "rfq" in text or "request for quote" in text:
                intent = "RFQ"
            elif "complaint" in text:
                intent = "Complaint"
            elif "urgent" in text:
                intent = "Urgent"
            else:
                intent = "General"

        elif file_format == 'JSON':
            if isinstance(content, dict):
                if 'invoice_number' in content:
                    intent = "Invoice"
                elif 'rfq_id' in content:
                    intent = "RFQ"
                else:
                    intent = "General"

        # Log to shared memory
        self.memory.log_entry({
            "filepath": filepath,
            "format": file_format,
            "intent": intent,
            "sender": sender,
            "subject": subject,
            "urgency": urgency,
            "content_excerpt": text_content[:200] if text_content else str(content)[:200]
        })

        # Structured result output
        result = {
            "filepath": filepath,
            "format": file_format,
            "intent": intent,
            "sender": sender,
            "subject": subject,
            "urgency": urgency,
            "excerpt": text_content[:500] if text_content else str(content)[:500]
        }

        return result
