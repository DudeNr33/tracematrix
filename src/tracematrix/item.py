from dataclasses import dataclass, field
from typing import Set


@dataclass(eq=False)
class TraceItem:
    """Represents an artifact which can be traced bidirectionally to other artifacts."""

    id: str  # pylint: disable=invalid-name
    traced_to: Set["TraceItem"] = field(default_factory=set)
