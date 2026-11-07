from models import Room


def build_room_summary(
    hotel_name: str,
    all_rooms: list[Room],
    attention_rooms: list[Room],
    external_service_available: bool,
    system_check_passed: bool,
) -> str:
    report_lines = [
        "PawStay Operations Report",
        f"Hotel: {hotel_name}",
        f"External service available: {external_service_available}",
        f"Total rooms: {len(all_rooms)}",
        f"Rooms requiring attention: {len(attention_rooms)}",
        f"System check passed: {system_check_passed}",
    ]
    report_lines.append("Attention details:")
    if len(attention_rooms) == 0:
        report_lines.append("None")
        
    else:
            
        for attention_room in attention_rooms:
                
            room_line = (
                f"Room {attention_room.room_number}: "
                f"{attention_room.camera_status}"
            )

            report_lines.append(room_line)

            
    return "\n".join(report_lines)