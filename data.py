from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional, Any
import time

class EventType(Enum):
    NIGHT_KILL = auto()
    NOMINATION = auto()
    VOTE = auto()
    EXECUTION = auto()
    DEATH = auto()
    ABILITY_USE = auto()
    GAME_END = auto()

@dataclass
class Event:
    game_id: str
    day_number: int
    phase: str
    event_type: EventType
    actor: Optional[int] = None
    target: Optional[int] = None
    result: Optional[Any] = None
    metadata: dict = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)