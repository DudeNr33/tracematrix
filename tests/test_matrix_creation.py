"""Functional tests for creating traceability matrices"""
from pathlib import Path

import pytest

from tracematrix.item import TraceItem
from tracematrix.matrix import TraceabilityMatrix


@pytest.fixture
def example_matrix():
    tc1 = TraceItem("TC_1")
    tc2 = TraceItem("TC_2")
    tc3 = TraceItem("TC_3")
    req1 = TraceItem("REQ_1")
    req2 = TraceItem("REQ_2")
    req3 = TraceItem("REQ_3")
    TraceItem.add_trace(tc1, req1)
    TraceItem.add_trace(tc2, req2)
    TraceItem.add_trace(tc2, req3)
    return TraceabilityMatrix((tc1, tc2, tc3), (req1, req2, req3))


@pytest.fixture
def example_output():
    data_dir = Path(__file__).parent / "data"
    return data_dir / "example_output.csv"


def test_matrix_creation(tmpdir, example_matrix, example_output):
    outputfile = tmpdir / "rtm.csv"
    example_matrix.write_matrix(outputfile)

    assert outputfile.read_text(encoding="utf8") == example_output.read_text(encoding="utf8")
