import json


def load_rooms_data(rooms_path) -> list[dict] | None:
    try:
        with open(rooms_path, "r", encoding= "utf-8") as rooms_file:
            loaded_rooms = json.load(rooms_file)
        return loaded_rooms

    except FileNotFoundError:
        print(f"Rooms file not found: {rooms_path}")
        return None

    except json.JSONDecodeError:
        print(f"Invalid JSON: {rooms_path}")
        return None
    

