import os
import json
import csv

def load_json_data(file_name):
	"""
	Load test data from a JSON file located in the 'data/' directory.
	"""
	file_path = os.path.join(os.path.dirname(__file__), "..", "fixtures", file_name)
	with open(file_path, "r") as f:
		return json.load(f)

def load_csv_data(file_name):
	"""
	Load test data from a CSV file located in the 'fixtures/' directory.
	Returns a list of dictionaries, one per row.
	"""
	file_path = os.path.join(os.path.dirname(__file__), "..", "fixtures", file_name)
	with open(file_path, newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		return list(reader)
