#Завдання 3:

#Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number
#і повернення значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо

import xml.etree.ElementTree as ET
import logging
from pathlib import Path

# Task 3

project_folder = Path(__file__).parents[1]
xml_file = project_folder / "ideas_for_test" / "work_with_xml" / "groups.xml"

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


def find_incoming(group_number):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")

        if number is not None and number.text == str(group_number):
            incoming = group.find("timingExbytes/incoming")

            if incoming is not None:
                return incoming.text

    return None


result = find_incoming(1)
logging.info(f"Incoming value: {result}")