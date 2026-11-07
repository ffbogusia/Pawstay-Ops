from models import Room
from room_service import filter_rooms_by_status
import pytest

@pytest.fixture
def sample_rooms() -> list[Room]:
    return [
        Room(12, "Astrid", "healthy", True),
        Room(14, "Haggen", "failed", True),
        Room(18, None, "unknown", False),
    ]
    

def test_filter_rooms_by_failed_status(
    sample_rooms: list[Room],
) -> None:

    filtered_rooms = filter_rooms_by_status(
        sample_rooms,
        "failed",
    )

    assert len(filtered_rooms) == 1
    assert filtered_rooms[0].room_number == 14
    assert filtered_rooms[0].camera_status == "failed"
    
    
def test_filter_rooms_by_all_status(
    sample_rooms: list[Room],
) -> None:
    
    filtered_rooms = filter_rooms_by_status(
        sample_rooms,
        "all",
    )

    assert len(filtered_rooms) == 3
    assert filtered_rooms == sample_rooms