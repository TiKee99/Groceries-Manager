import json
import requests
from config import WBW_USER_NAME, WBW_PASSWORD


def login():
    url: str = "https://app.wiebetaaltwat.nl/api/users/sign_in"
    payload: str = json.dumps(
        {
            "user": {
                "email": WBW_USER_NAME,
                "password": WBW_PASSWORD
            }
        }
    )
    headers: dict[str, str] = {
        "sec-ch-ua": "'Not_A Brand';v='8', 'Chromium';v='120', 'Microsoft Edge';v='120'",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        "x-app-react": "true",
        "content-type": "application/json",
        "accept": "application/json",
        "cache-control": "no-cache",
        "accept-version": "10",
        "baggage": "sentry-environment=production,sentry-release=1.0.140-production-04ef43a6,sentry-public_key=3b84c9bfdde845748bfb353bcea99938,sentry-trace_id=a77fa65995e14131810e446b1ab2a487",
        "sentry-trace": "a77fa65995e14131810e446b1ab2a487-89aaab32bae8c669-0",
        "sec-ch-ua-platform": "'Windows'",
        "host": "app.wiebetaaltwat.nl"
    }

    try:
        response = requests.post(url=url, headers=headers, data=payload)
        response.raise_for_status()
    except Exception as exception:
        print(f"WieBetaaltWat - An exeption occurred while loggin in: {exception}")
        return None

    if response.status_code == 201 or response.status_code == 200:
        print(f"WieBetaaltWat - Succesfully logged in in with {WBW_USER_NAME}")
        return response.cookies
    else:
        print(f"WieBetaaltWat - Failed to log in in with {WBW_USER_NAME}: Statuscode {response.status_code}")
        return None


def create_transaction(cookies=None):
    url: str = "https://app.wiebetaaltwat.nl/api/lists/d9352032-5d29-4052-943d-cc8b7a559171/expenses"
    payload: str = json.dumps(
        {
            "expense": {
                "id": "95492e69-5f97-4226-96be-f6204dcffbac",
                "name": "c een test",
                "payed_by_id": "ac323a19-0d64-47b6-962c-18273100dc07",
                "payed_on": "2023-12-17",
                "source_amount": {
                "fractional": 470,
                "currency": "EUR"
                },
                "amount": {
                "fractional": 470,
                "currency": "EUR"
                },
                "exchange_rate": 1,
                "shares_attributes": [
                {
                    "id": "ac323a19-0d64-47b6-962c-18273100dc07",
                    "member_id": "ac323a19-0d64-47b6-962c-18273100dc07",
                    "meta": {
                    "type": "factor",
                    "multiplier": 3
                    },
                    "amount": None,
                    "source_amount": {
                    "fractional": 470,
                    "currency": "EUR"
                    }
                }
                ]
            }
        }
    )
    headers: dict[str, str] = {
        "authority": "app.wiebetaaltwat.nl",
        "accept": "application/json",
        "accept-language": "nl",
        "accept-version": "10",
        "baggage": "sentry-environment=production,sentry-release=1.0.140-production-04ef43a6,sentry-public_key=3b84c9bfdde845748bfb353bcea99938,sentry-trace_id=0e4f29fd8e19479c90139f5ef492994e",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://app.wiebetaaltwat.nl",
        "referer": "https://app.wiebetaaltwat.nl/lists/d9352032-5d29-4052-943d-cc8b7a559171/transactions/create",
        "sec-ch-ua": "'Not_A Brand';v='8', 'Chromium';v='120', 'Microsoft Edge';v='120'",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "'Android'",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sentry-trace": "0e4f29fd8e19479c90139f5ef492994e-8a528b3919446235-0",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36 Edg/120.0.0.0",
        "x-app-react": "true"
    }

    if cookies is None:
        print("WieBetaaltWat - Log in before creating a transaction")

    response = requests.post(url=url, headers=headers, data=payload, cookies=cookies)
