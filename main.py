import os
from utils.file_parser import parse_file
from agents.classifier_agent import ClassifierAgent
from memory.shared_memory import SharedMemory

# Initialize agents and memory
memory = SharedMemory()
classifier = ClassifierAgent(memory)

# Process all files in data/
data_folder = 'data'

for filename in os.listdir(data_folder):
    filepath = os.path.join(data_folder, filename)
    print(f"\nProcessing: {filename}")

    fmt, content = parse_file(filepath)
    if fmt == 'Unknown':
        print("Unsupported format.")
        continue

    result = classifier.process(filepath, fmt, content)
    print("Result:", result)
