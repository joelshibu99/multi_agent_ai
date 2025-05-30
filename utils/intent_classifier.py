def classify_intent(content):
    if isinstance(content, str):
        if "quote" in content.lower():
            return "RFQ"
        if "complaint" in content.lower():
            return "Complaint"
        if "invoice" in content.lower():
            return "Invoice"
    elif isinstance(content, dict):
        if "invoice_id" in content:
            return "Invoice"
    return "Unknown"
