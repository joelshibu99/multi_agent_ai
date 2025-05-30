class EmailAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, content, intent):
        sender = self._extract_sender(content)
        urgency = self._detect_urgency(content)
        values = {"sender": sender, "urgency": urgency, "intent": intent}
        self.memory.log("Email", "Email", intent, values, thread_id="email-thread-1")
        return values

    def _extract_sender(self, text):
        return "example@example.com"  # Placeholder

    def _detect_urgency(self, text):
        return "High" if "urgent" in text.lower() else "Normal"
