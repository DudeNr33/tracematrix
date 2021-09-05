"""
Definition of the reporter interface.
"""

from abc import ABC, abstractmethod
from typing import List

from tracematrix.item import TraceItem


class Reporter(ABC):
    """
    Abstract base class from which all reporters should inherit from.
    """
    @staticmethod
    @abstractmethod
    def write(
        outputfile: str, rows: List[TraceItem], columns: List[TraceItem]
    ) -> None:
        """Create the output file and save it to disk."""
