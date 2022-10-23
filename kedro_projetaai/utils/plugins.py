import importlib.metadata
from functools import lru_cache
from typing import Any, Dict, List


@lru_cache(maxsize=1)
def _get_entry_points() -> Dict[str, List[importlib.metadata.EntryPoint]]:
    # Loads and caches entry points from the current environment.
    return importlib.metadata.entry_points()


def get_plugins(entry_point: str) -> Dict[str, Any]:
    """Gets plugins from a given entry point.

    Args:
        entry_point (str): The entry point to get plugins from.

    Returns:
        Dict[str, Any]: A dictionary of plugins.
    """
    return {
        plugin.name: plugin.load()
        for plugin in _get_entry_points().get(entry_point, [])
    }
