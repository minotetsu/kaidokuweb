import json
import numpy as np

class ReadJson:
    def __init__(self, file_name):
        json_file = open(file_name, 'r', encoding="utf-8_sig")
        json_data = json.load(json_file)
        json_file.close
        self.question = np.array(json_data)
