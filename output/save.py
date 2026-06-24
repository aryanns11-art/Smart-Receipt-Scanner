import csv
import os


def save_receipt(store, date, total):
    file_path = "output/receipts.csv"

    os.makedirs("output", exist_ok=True)

    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:              ## Write header only once
            writer.writerow(["Store", "Date", "Total"])

        writer.writerow([store, date, total])

    print("\nReceipt saved successfully!")