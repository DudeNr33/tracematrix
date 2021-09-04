"""Functional tests for creating traceability matrices"""
import pytest
from tracematrix import reporters

from tracematrix.item import TraceItem
from tracematrix.matrix import TraceabilityMatrix


@pytest.mark.parametrize(
    "reporter,filename",
    [
        (reporters.CsvReporter, "tracematrix.csv"),
        (reporters.HtmlReporter, "tracematrix.html"),
    ],
)
def test_matrix_creation(tmpdir, datadir, reporter, filename):
    tc1 = TraceItem("TC_1")
    tc2 = TraceItem("TC_2")
    tc3 = TraceItem("TC_3")
    req1 = TraceItem("REQ_1")
    req2 = TraceItem("REQ_2")
    req3 = TraceItem("REQ_3")
    req4 = TraceItem("REQ_4")
    TraceItem.add_trace(tc1, req1)
    TraceItem.add_trace(tc2, req2)
    TraceItem.add_trace(tc2, req3)
    matrix = TraceabilityMatrix(
        (tc1, tc2, tc3), (req1, req2, req3, req4), reporter=reporter
    )
    actual_output = tmpdir / filename
    expected_output = datadir / filename
    matrix.write_matrix(actual_output)

    assert actual_output.read_text(encoding="utf8") == expected_output.read_text(
        encoding="utf8"
    )
