from typing import Dict, List


class TraceItem:
    _registry: Dict[str, "TraceItem"] = {}

    def __init__(self, id_: str, traced_to: List["TraceItem"] = None):
        self.id = id_
        self.traced_to = traced_to or []

    @classmethod
    def get_by_id(cls, id_):
        if id_ in cls._registry:
            item = cls._registry[id_]
        else:
            item = cls(id_)
            cls._registry[id_] = item
        return item

    @staticmethod
    def add_trace(first: "TraceItem", second: "TraceItem"):
        first.traced_to.append(second)
        second.traced_to.append(first)
