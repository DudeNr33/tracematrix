from tracematrix import matrix, reporters
from tracematrix.item import TraceItem


class TestCreation:
    """Unit tests concerning the initialization of a TraceabilityMatrix object."""
    @staticmethod
    def test_defaults():
        mymatrix = matrix.TraceabilityMatrix()
        assert len(mymatrix.rows) == 0
        assert len(mymatrix.columns) == 0
        assert isinstance(mymatrix.reporter, reporters.CsvReporter)

    @staticmethod
    def test_explicit_reporter():
        mymatrix = matrix.TraceabilityMatrix(reporter=reporters.HtmlReporter)
        assert isinstance(mymatrix.reporter, reporters.HtmlReporter)

    @staticmethod
    def test_explicit_rows():
        rows = [
            TraceItem("TC1"),
            TraceItem("TC2"),
        ]
        mymatrix = matrix.TraceabilityMatrix(rows=rows)
        assert mymatrix.rows == rows
        assert len(mymatrix.columns) == 0

    @staticmethod
    def test_explicit_columns():
        cols = [
            TraceItem("REQ1"),
            TraceItem("REQ2"),
        ]
        mymatrix = matrix.TraceabilityMatrix(columns=cols)
        assert len(mymatrix.rows) == 0
        assert mymatrix.columns == cols
