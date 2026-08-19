from datetime import datetime
import logging


NEEDED_KEY = "Key TSTFEED0300|7E3E|0400"

logging.basicConfig(
    filename="hb_test.log",
    filemode="w",
    level=logging.WARNING,
    format="%(levelname)s - %(message)s"
)


def read_log(filename):
    result = []

    with open(filename, "r", encoding="utf-8") as log_file:
        for row in log_file:
            if NEEDED_KEY in row:
                result.append(row)

    return result


def parse_time(row):
    start = row.find("Timestamp ") + len("Timestamp ")
    value = row[start:start + 8]

    return datetime.strptime(value, "%H:%M:%S")


def check_heartbeat(logs):
    for current_row, previous_row in zip(logs, logs[1:]):
        current_time = parse_time(current_row)
        previous_time = parse_time(previous_row)

        difference = (current_time - previous_time).total_seconds()

        if difference >= 33:
            logging.error(
                f"Heartbeat delay {difference} sec at "
                f"{current_time.strftime('%H:%M:%S')}"
            )
        elif difference > 31:
            logging.warning(
                f"Heartbeat delay {difference} sec at "
                f"{current_time.strftime('%H:%M:%S')}"
            )


logs = read_log("hblog.txt")
check_heartbeat(logs)