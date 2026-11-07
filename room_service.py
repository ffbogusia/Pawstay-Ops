from models import Room
from validation import is_valid_room_data


def create_room_from_data(room_data: dict) -> Room:
    room_number = room_data.get("room_number")
    dog_name = room_data.get("dog_name")
    camera_status = room_data.get("camera_status")
    occupied = room_data.get("occupied")

    camera_status_clean = camera_status.strip().lower()

    dog_name_clean = dog_name

    if dog_name is not None:
        dog_name_clean = dog_name.strip()

    return Room(
        room_number,
        dog_name_clean,
        camera_status_clean,
        occupied,
    )

def create_valid_room_objects(raw_room_entries: list[dict],) -> list[Room]:
    room_objects = []

    for raw_room_entry in raw_room_entries:
        valid_room = is_valid_room_data(raw_room_entry)

        if valid_room == True:
            room_entry_object = create_room_from_data(raw_room_entry)
            room_objects.append(room_entry_object)
            
    return room_objects

def get_rooms_requiring_attention(
    room_objects: list[Room],
) -> list[Room]:
    rooms_for_attention = []

    for room_object in room_objects:
        attention_room = room_object.requires_attention()
        if attention_room:
            rooms_for_attention.append(room_object)
    return rooms_for_attention


def filter_rooms_by_status(
    room_objects: list[Room],
    wanted_status: str,
) -> list[Room]:
    if wanted_status == "all":
        return room_objects
    
    filtered_rooms: list[Room] = []
    
    for current_room in room_objects:
        if current_room.camera_status == wanted_status:
            filtered_rooms.append(current_room)
    return filtered_rooms