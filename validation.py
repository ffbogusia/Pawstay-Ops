def is_valid_room_data(candidate_room: dict) -> bool:
    dog_name = candidate_room.get("dog_name")
    room_number = candidate_room.get("room_number")
    camera_status = candidate_room.get("camera_status")
    occupied = candidate_room.get("occupied")

    if type(room_number) is not int:
        return False

    if room_number <= 0:
        return False

    if type(occupied) is not bool:
        return False

    if type(camera_status) is not str:
        return False
    
    clean_camera_status = camera_status.lower().strip()

    if clean_camera_status not in ("healthy", "failed", "unknown"):
        return False

    if occupied is True:
        if type(dog_name) is not str:
            return False

        clean_dog_name = dog_name.strip()

        if clean_dog_name == "":
            return False

    else:
        if dog_name is not None:
            return False

    return True