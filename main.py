import os
import argparse
import logging
from pathlib import Path
from config_io import load_rooms_data
from room_service import (
    create_valid_room_objects,
    filter_rooms_by_status,
    get_rooms_requiring_attention,
)
from report_builder import build_room_summary
from api_client import check_external_service
from system_check import run_python_system_check


current_folder = Path(__file__).parent

logs_folder = current_folder / "logs"
logs_folder.mkdir(exist_ok=True)

log_path = logs_folder / "pawstay.log"
rooms_path = current_folder / "data" / "rooms.json"

pawstay_log_level = os.getenv(
    "PAWSTAY_LOG_LEVEL",
    "INFO"
).strip().upper()

logging.basicConfig(
    level=pawstay_log_level,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(log_path, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)

def main() -> None:

    parser = argparse.ArgumentParser(
    description="Generate PawStay operations report."
    )

    parser.add_argument(
    "--report-name",
    default="pawstay_report.txt",
    help="Name of the generated report file.",
    )
    
    parser.add_argument(
        "--status",
        choices=["all", "healthy", "failed", "unknown"],
        default="all",
        help="Camera status to find.",
    )

    args = parser.parse_args()
    
    print(f"Selected status: {args.status}")

    environment_hotel_name = os.getenv(
    "PAWSTAY_HOTEL",
    "PawStay",
    )

    environment_mode = os.getenv(
    "PAWSTAY_ENVIRONMENT",
    "development",
    )

    max_rooms_text = os.getenv(
    "PAWSTAY_MAX_ROOMS",
    "10",
    )

    try:
        max_rooms = int(max_rooms_text)

    except ValueError:
        logger.warning(
            "Invalid PAWSTAY_MAX_ROOMS value: %s. Using default 10.",
            max_rooms_text,
        )

        max_rooms = 10
    
    external_service_url = os.getenv(
    "PAWSTAY_API_URL",
    "https://httpbin.org/status/200",
    )
    
    api_timeout_text = os.getenv(
    "PAWSTAY_API_TIMEOUT",
    "5",)

    try:
        api_timeout_seconds = float(api_timeout_text)
        
    except ValueError:
        logger.warning("Invalid PAWSTAY_API_TIMEOUT value: %s. Using default 5.",
                       api_timeout_text)
        api_timeout_seconds = 5.0
        
    system_check_passed = run_python_system_check()

    print(f"Hotel: {environment_hotel_name}")
    print(f"Environment: {environment_mode}")
    print(f"Log level: {pawstay_log_level}")
    print(f"API timeout: {api_timeout_seconds} seconds")
    print(f"Maximum rooms: {max_rooms}") 

    raw_rooms = load_rooms_data(rooms_path)

    if raw_rooms is None:
        logger.error("Room data unavailable.")

    else:
        room_objects = create_valid_room_objects(raw_rooms)
        current_room_count = len(room_objects)

        if current_room_count > max_rooms:
            logger.warning(
                "Hotel capacity exceeded: %s rooms, maximum is %s.",
                current_room_count,
                max_rooms,
            )
        else:
            logger.info(
                "Hotel capacity check passed: %s/%s rooms.",
                current_room_count,
                max_rooms,
            )

        selected_room_objects = filter_rooms_by_status(
            room_objects,
            args.status,
        )

        attention_rooms = get_rooms_requiring_attention(
            selected_room_objects
        ) 
        
        for attention_room in attention_rooms:
            logger.warning(
                "Room %s requires attention: %s",
                attention_room.room_number,
                attention_room.camera_status
            )
        external_service_available = check_external_service(
            external_service_url,
            timeout_seconds=api_timeout_seconds,
        )
        
        report_text = build_room_summary(
            environment_hotel_name,
            selected_room_objects,
            attention_rooms,
            external_service_available,
            system_check_passed,
        )
        


        print(report_text)

        reports_folder = current_folder / "reports"
        reports_folder.mkdir(exist_ok=True)

        pawstay_report_path = reports_folder / args.report_name

        pawstay_report_path.write_text(report_text, encoding="utf-8")

        logger.info(
            "Report saved: %s",
            pawstay_report_path
        )

if __name__ == "__main__":
    main()