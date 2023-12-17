from src import ah, receipts
from datetime import datetime
import src.wie_betaalt_wat as wbw
from config import BEARER_TOKEN
from common import REQUEST_HEADERS, OUTPUT_PATH


def main(retrieval_date: datetime):
    #headers: dict[str, str] = REQUEST_HEADERS.copy()
    #headers.update({"Authorization": f"Bearer {BEARER_TOKEN}"})

    #ah.get_data("v1/receipts", headers, f"{OUTPUT_PATH}/receipts.json")

    #transaction_ids: list[str] = receipts.get_transaction_ids(f"{OUTPUT_PATH}/receipts.json", retrieval_date)

    #for transaction_id in transaction_ids:
    #    ah.get_data(f"v2/receipts/{transaction_id}", headers, f"{OUTPUT_PATH}/receipt.json")

    cookies = wbw.login()

    if cookies is not None:
        wbw.create_transaction(cookies)


if __name__ == "__main__":
    main(datetime(2023, 11, 2))