from validation import is_valid_room_data


def test_valid_occupied_room() -> None:
    candidate_room = {
        "room_number": 12,
        "dog_name": "Astrid",
        "camera_status": "healthy",
        "occupied": True,
    }

    validation_result = is_valid_room_data(candidate_room)

    assert validation_result is True


def test_room_number_as_string_is_invalid() -> None:
    candidate_room = {
        "room_number": "12",
        "dog_name": "Astrid",
        "camera_status": "healthy",
        "occupied": True,
    }

    validation_result = is_valid_room_data(candidate_room)

    assert validation_result is False


def test_occupied_room_without_dog_is_invalid() -> None:
    candidate_room = {
        "room_number": 12,
        "dog_name": None,
        "camera_status": "healthy",
        "occupied": True,
    }

    validation_result = is_valid_room_data(candidate_room)

    assert validation_result is False
