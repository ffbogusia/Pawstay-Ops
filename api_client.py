import logging

import requests

import time


logger = logging.getLogger(__name__)

def check_external_service(
    service_url: str,
    timeout_seconds: float = 5.0,
    max_attempts: int = 3,
    delay_seconds: float = 2.0,
) -> bool:

    for attempt_number in range(1, max_attempts + 1):
        logger.info(
            "API attempt %s/%s",
            attempt_number,
            max_attempts,
        )

        try:
            api_response = requests.get(
                service_url,
                timeout=timeout_seconds,
            )

            logger.info(
                "External API status: %s",
                api_response.status_code,
            )

            api_response.raise_for_status()
            return True

        except requests.exceptions.RequestException as error:
            logger.warning(
                "API attempt %s failed: %s",
                attempt_number,
                error,
            )
        if attempt_number < max_attempts:
            logger.info(
                "Waiting %s seconds before retry.",
                delay_seconds,
            )

            time.sleep(delay_seconds)

    logger.error("All API attempts failed.")
    return False