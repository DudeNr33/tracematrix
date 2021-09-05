"""Functional tests for creating traceability matrices"""
import pytest
from tracematrix import reporters

from tracematrix.matrix import TraceabilityMatrix


@pytest.mark.parametrize(
    "reporter,filename",
    [
        (reporters.CsvReporter, "tracematrix.csv"),
        (reporters.HtmlReporter, "tracematrix.html"),
    ],
)
def test_matrix_creation(tmpdir, datadir, reporter, filename):
    matrix = TraceabilityMatrix(reporter=reporter)
    for testcase_id in ("TC_1", "TC_2", "TC_3"):
        matrix.add_row(testcase_id)
    for requirement_id in ("REQ_1", "REQ_2", "REQ_3", "REQ_4"):
        matrix.add_column(requirement_id)
    matrix.add_trace("TC_1", "REQ_1")
    matrix.add_trace("TC_2", "REQ_2")
    matrix.add_trace("TC_2", "REQ_3")
    actual_output = tmpdir / filename
    expected_output = datadir / filename
    matrix.write_matrix(actual_output)

    assert actual_output.read_text(encoding="utf8") == expected_output.read_text(
        encoding="utf8"
    )
