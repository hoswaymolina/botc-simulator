"""
export_results.py

Serializes Blood on the Clocktower simulation results to JSON.

This is the staging step between running simulations (in memory) and
loading them into the SQLite pipeline. Keeping this step separate means
a bug in the SQLite loader never requires re-running simulations --
just re-run the loader against the JSON already on disk.
"""

import json
from enum import Enum
from pathlib import Path
from datetime import datetime


class SimEncoder(json.JSONEncoder):
    """
    JSON encoder that knows how to handle the object types this
    project produces:
      - Enum members (e.g. event types) -> their `.name` string
      - Plain objects with a `__dict__` -> that dict, recursively
      - datetime objects -> ISO 8601 strings
    """

    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.name
        if isinstance(obj, datetime):
            return obj.isoformat()
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        return super().default(obj)


def save_simulations(
    games: list, events: list, filepath: str = "data/simulations.json"
) -> Path:
    """
    Write simulation results to a single JSON file with two top-level
    keys, mirroring the `games` / `events` SQLite tables you've
    already planned.

    Parameters
    ----------
    games : list
        The GAME_END event objects returned by `simulate_games()`.
    events : list
        All other event objects returned by `simulate_games()`.
    filepath : str
        Where to write the file. Parent directories are created
        automatically if they don't exist.

    Returns
    -------
    Path
        The path the file was written to, for easy chaining/logging.
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    payload = {"games": games, "events": events}

    with path.open("w") as f:
        json.dump(payload, f, cls=SimEncoder, indent=2)

    print(
        f"Saved {len(games)} games and {len(events)} events to {path.resolve()}"
    )
    return path


if __name__ == "__main__":
    from simulate import simulate_games

    games, events = simulate_games(100)
    save_simulations(games, events)