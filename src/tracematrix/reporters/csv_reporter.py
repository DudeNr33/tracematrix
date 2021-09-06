"""
Reporter for CSV output that can be opened with MS Excel or other tools.
"""
import csv
from typing import List

from tracematrix.item import TraceItem
from tracematrix.reporters.base_reporter import Reporter


class CsvReporter(Reporter):
    """Creates reports in .csv format"""
    @staticmethod
    def write(
        outputfile: str, rows: List[TraceItem], columns: List[TraceItem]
    ) -> None:
        fieldnames = [""] + [req.id for req in columns] + ["total"]
        with open(outputfile, "w", encoding="utf8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames, delimiter=";")
            writer.writeheader()
            for testcase in rows:
                rowdict = {"": testcase.id}
                for traced_req in testcase.traced_to:
                    rowdict[traced_req.id] = "x"
                rowdict["total"] = len(testcase.traced_to)
                writer.writerow(rowdict)
            result_row = {"": "total"}
            for req in columns:
                result_row[req.id] = len(req.traced_to)
            writer.writerow(result_row)
