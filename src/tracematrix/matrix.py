import csv
from typing import List

from tracematrix.item import TraceItem


class TraceabilityMatrix:
    def __init__(self, testcases: List[TraceItem], requirements: List[TraceItem]):
        self.testcases = testcases
        self.requirements = requirements

    def write_matrix(self, outputfile):
        fieldnames = ["testcase"] + [req.id for req in self.requirements] + ["total"]
        with open(outputfile, "w", encoding="utf8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames, delimiter=";")
            writer.writeheader()
            for tc in self.testcases:
                rowdict = {"testcase": tc.id}
                for traced_req in tc.traced_to:
                    rowdict[traced_req.id] = "x"
                rowdict["total"] = len(tc.traced_to)
                writer.writerow(rowdict)
            result_row = {"testcase": "total"}
            for req in self.requirements:
                result_row[req.id] = len(req.traced_to)
            writer.writerow(result_row)
