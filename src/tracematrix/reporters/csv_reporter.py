import csv
from typing import List

from tracematrix.item import TraceItem
from tracematrix.reporters.base_reporter import Reporter


class CsvReporter(Reporter):
    @staticmethod
    def write(
        outputfile: str, testcases: List[TraceItem], requirements: List[TraceItem]
    ) -> None:
        fieldnames = ["testcase"] + [req.id for req in requirements] + ["total"]
        with open(outputfile, "w", encoding="utf8") as outfile:
            writer = csv.DictWriter(outfile, fieldnames, delimiter=";")
            writer.writeheader()
            for tc in testcases:
                rowdict = {"testcase": tc.id}
                for traced_req in tc.traced_to:
                    rowdict[traced_req.id] = "x"
                rowdict["total"] = len(tc.traced_to)
                writer.writerow(rowdict)
            result_row = {"testcase": "total"}
            for req in requirements:
                result_row[req.id] = len(req.traced_to)
            writer.writerow(result_row)
