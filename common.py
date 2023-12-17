from pathlib import Path

AH_API_BASE_URL: str = "https://api.ah.nl/mobile-services"
DATE_FORMAT: str = "%Y-%m-%dT%H:%M:%SZ"
OUTPUT_PATH: Path = Path("data/output")
REQUEST_HEADERS: dict[str, str] = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "User-Agent": "Appie/8.22.3",
    "Content-Type": "application/json",
    "X-Application": "AHWEBSHOP"
}
