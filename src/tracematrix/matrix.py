"""Definition of the TraceabilityMatrix."""
from typing import List

from tracematrix.item import TraceItem
from tracematrix.reporters import CsvReporter, Reporter


class TraceabilityMatrix:
    """Represents a traceability matrix which shows the traces between two sets of TraceItems."""
    def __init__(
        self,
        testcases: List[TraceItem],
        requirements: List[TraceItem],
        reporter: Reporter = CsvReporter,
    ):
        self.testcases = testcases
        self.requirements = requirements
        self.reporter = reporter()

    def write_matrix(self, outputfile):
        """Create the matrix and write it to the given output file."""
        self.reporter.write(outputfile, self.testcases, self.requirements)
