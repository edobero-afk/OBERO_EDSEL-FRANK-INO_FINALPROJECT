"""Handles saving and loading scan history."""

import json
import os


class HistoryManager:
    """Manages URL scan history."""

    def __init__(self, filename):
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump([], file)

    def save_scan(self, url, result):
        history = self.load_history()
        history.append({"url": url, "result": result})

        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

    def load_history(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return json.load(file)