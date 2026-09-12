import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

IPU_NOTICES_URL = "https://www.ipu.ac.in/notices.php"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/131.0.0.0 Safari/537.36"
    )
}

EXCLUDE_KEYWORDS = [
    "refund policy",
    "instruction medium",
    "public self disclosure",
    "self disclosure",
]


def fetch_live_notices(limit=20):
    """
    Fetch current notices directly from the official IPU website.
    """

    response = requests.get(
        IPU_NOTICES_URL,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    notices = []
    seen_urls = set()

    for a in soup.find_all("a"):
        title = a.get_text(" ", strip=True)
        href = a.get("href")

        if not title or not href:
            continue

        if ".pdf" not in href.lower():
            continue

        title_lower = title.lower()

        if any(keyword in title_lower for keyword in EXCLUDE_KEYWORDS):
            continue

        pdf_url = urljoin(IPU_NOTICES_URL, href)

        if pdf_url in seen_urls:
            continue

        seen_urls.add(pdf_url)

        notices.append({
            "title": title,
            "url": pdf_url
        })

        if len(notices) >= limit:
            break

    return notices


if __name__ == "__main__":
    notices = fetch_live_notices(10)

    print(f"Found {len(notices)} live notices:\n")

    for i, notice in enumerate(notices, 1):
        print(f"{i}. {notice['title']}")
        print(f"   {notice['url']}")
        print()
