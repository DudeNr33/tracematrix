"""Definition of the TraceabilityMatrix."""
from typing import List, Optional

from tracematrix.item import TraceItem
from tracematrix.reporters import CsvReporter, Reporter


class TraceabilityMatrix:
    """Represents a traceability matrix which shows the traces between two sets of TraceItems."""
    def __init__(
        self,
        rows: Optional[List[TraceItem]] = None,
        columns: Optional[List[TraceItem]] = None,
        reporter: Reporter = CsvReporter,
    ):
        self.rows = rows or []
        self.columns = columns or []
        self.reporter = reporter()

    def write_matrix(self, outputfile):
        """Create the matrix and write it to the given output file."""
        self.reporter.write(outputfile, self.rows, self.columns)
