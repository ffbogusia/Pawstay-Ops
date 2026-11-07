from dataclasses import dataclass

@dataclass
class Room:
    room_number: int
    dog_name: str | None
    camera_status: str
    occupied: bool

    def requires_attention(self) -> bool:
        if self.camera_status in ("failed", "unknown"):
            return True
        else:
            return False
    