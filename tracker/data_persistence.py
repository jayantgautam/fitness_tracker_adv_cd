
import json
import os

class DataPersistence:
    def __init__(self, file_path="fitness_data.json"):
        self.file_path = file_path

    def save_data(self, activity, duration):
        data = self.load_data()
        data.append({"Activity": activity, "Duration": duration})
        with open(self.file_path, "w") as file:
            json.dump(data, file)

    def load_data(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return []
