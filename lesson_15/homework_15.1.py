#Завдання 1:

#Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv

import csv
from pathlib import Path

project_folder = Path(__file__).parents[1]
csv_folder = project_folder / "ideas_for_test" / "work_with_csv"

first_file = csv_folder / "random.csv"
second_file = csv_folder / "rmc.csv"
result_file = Path(__file__).parent / "result_Detsyk.csv"

unique_rows = set()

for file in (first_file, second_file):
    with open(file, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)

        for row in reader:
            unique_rows.add(tuple(row))

with open(result_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(sorted(unique_rows))

print(f"Saved at: {result_file}")