from pathlib import Path
from typing import Dict, List, Optional, Union

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
        self._row_registry: Dict[str, TraceItem] = {row.id: row for row in self.rows}
        self._column_registry: Dict[str, TraceItem] = {
            col.id: col for col in self.columns
        }

    def add_row(self, row_id: str) -> None:
        if row_id in self._row_registry:
            raise ValueError("A row with this id already exists.")
        new_row = TraceItem(row_id)
        self._row_registry[row_id] = new_row
        self.rows.append(new_row)

    def add_column(self, column_id: str) -> None:
        if column_id in self._column_registry:
            raise ValueError("A column with this id already exists.")
        new_column = TraceItem(column_id)
        self._column_registry[column_id] = new_column
        self.columns.append(new_column)

    def add_trace(self, row_id: str, column_id: str) -> None:
        """Create a bidirectional trace between a row and a column."""
        try:
            row_item = self._row_registry[row_id]
            column_item = self._column_registry[column_id]
        except KeyError as exc:
            raise KeyError("Could not find the specified row or column") from exc
        else:
            row_item.traced_to.add(column_item)
            column_item.traced_to.add(row_item)

    def write_matrix(self, outputfile: Union[Path, str]) -> None:
        """Create the matrix and write it to the given output file."""
        self.reporter.write(outputfile, self.rows, self.columns)
