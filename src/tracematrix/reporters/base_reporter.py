from abc import ABC, abstractstaticmethod
from typing import List

from tracematrix.item import TraceItem


class Reporter(ABC):
    @abstractstaticmethod
    def write(
        outputfile: str, testcases: List[TraceItem], requirements: List[TraceItem]
    ) -> None:
        pass
