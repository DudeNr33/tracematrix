from typing import List

from tracematrix.item import TraceItem
from tracematrix.reporters import CsvReporter, Reporter


class TraceabilityMatrix:
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
        self.reporter.write(outputfile, self.testcases, self.requirements)
