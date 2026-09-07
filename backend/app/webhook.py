import json
import logging
import os
import urllib.error
import urllib.request

logger = logging.getLogger("webhook")


def trigger_github_rebuild(event_type: str = "cms_post_published", payload: dict | None = None) -> bool:
    github_token = os.getenv("GITHUB_TOKEN")
    github_repo = os.getenv("GITHUB_REPO", "RJ-Rishi91/onerishi-website")

    if not github_token:
        logger.info("GITHUB_TOKEN not set. Skipping GitHub Actions rebuild dispatch.")
        return False

    url = f"https://api.github.com/repos/{github_repo}/dispatches"
    data = json.dumps({
        "event_type": event_type,
        "client_payload": payload or {}
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"Bearer {github_token}",
            "User-Agent": "OneRishi-CMS",
            "Content-Type": "application/json",
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status in (200, 204):
                logger.info("Triggered GitHub Actions rebuild successfully.")
                return True
            else:
                logger.warning(f"GitHub dispatch returned status {response.status}")
                return False
    except Exception as e:
        logger.error(f"Failed to dispatch GitHub rebuild: {e}")
        return False
