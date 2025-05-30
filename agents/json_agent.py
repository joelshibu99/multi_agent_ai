class JSONAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, content, intent):
        required_fields = ["invoice_id", "amount", "date"]
        missing = [f for f in required_fields if f not in content]
        values = {"fields": content, "missing": missing, "intent": intent}
        self.memory.log("JSON", "JSON", intent, values, thread_id="json-thread-1")
        return values
