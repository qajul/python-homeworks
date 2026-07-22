#Завдання 2:

#Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
# результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

import json
import logging
from pathlib import Path

# Task 2

project_folder = Path(__file__).parents[1]
json_folder = project_folder / "ideas_for_test" / "work_with_json"

log_file = Path(__file__).parent / "json__Detsyk.log"

logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format="%(levelname)s: %(message)s"
)

for file in json_folder.glob("*.json"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError:
        logging.error(f"{file.name} is not a valid JSON")

print(f"Log saved at: {log_file}")