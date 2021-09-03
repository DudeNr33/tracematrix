"""Definition of trace items."""
from typing import Dict, Set


class TraceItem:
    """Represents an artifact which can be traced bidirectionally to other artifacts."""

    _registry: Dict[str, "TraceItem"] = {}

    def __init__(self, id_: str, traced_to: Set["TraceItem"] = None):
        self.id = id_  # pylint: disable=invalid-name
        self.traced_to = traced_to or set()

    @classmethod
    def get_by_id(cls, id_):
        """
        Retrieve an existing TraceItem by its id, or create a new instance if no TraceItem with this id exists.
        """
        if id_ in cls._registry:
            item = cls._registry[id_]
        else:
            item = cls(id_)
            cls._registry[id_] = item
        return item

    @staticmethod
    def add_trace(first: "TraceItem", second: "TraceItem"):
        """Add a bidirectional trace between the two items."""
        first.traced_to.add(second)
        second.traced_to.add(first)
