import json
import requests
from pathlib import Path
from datetime import datetime
from common import DATE_FORMAT
from common import AH_API_BASE_URL


def get_data(endpoint: str, headers: dict[str, str], save_path: Path = None):
    url: str = f"{AH_API_BASE_URL}/{endpoint}"

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        print("Information succesfully retrieved")

        if save_path is not None:
            with open(save_path, "w") as f:
                json.dump(response.json(), f)

            print(f"Information stored at {save_path}")

    else:
        print(f"Information could not be retrieved. Response code: {response.status_code}")


def get_transaction_ids(receipts_path: Path, retrieval_date: datetime) -> list[str]:
    with open(receipts_path, "r") as f:
        receipts_json = json.load(f)

    transaction_ids: list[str] = list()

    for receipt in receipts_json:
        receipt_date: datetime = datetime.strptime(receipt["transactionMoment"], DATE_FORMAT)
        days_difference: int = (receipt_date - retrieval_date).days

        if days_difference > 0:
            continue
        elif days_difference < 0:
            break
        else:
            transaction_ids.append(receipt["transactionId"])

    return transaction_ids