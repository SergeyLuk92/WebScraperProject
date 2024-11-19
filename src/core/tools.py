from os import makedirs, path
from csv import writer
import csv

from loguru import logger

from config import settings


def save_csv(data_list: list) -> None:
    makedirs(settings.OUTPUT_PATH, exist_ok=True)
    output_path: str = path.join(settings.OUTPUT_PATH, settings.CSV_FILE_NAME)  # noqa
    with open(output_path, 'w', encoding='utf-8', newline='') as csvfile:
        csv_writer: csv.writer = writer(csvfile)
        csv_writer.writerow(["Title", "Link"])
        for data in data_list:
            csv_writer.writerow([data["Title"], data["Link"]])
    logger.info("Data successfully saved to CSV")
