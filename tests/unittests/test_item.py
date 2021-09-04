import pytest

from tracematrix.item import TraceItem

@pytest.fixture(autouse=True)
def clear_registry():
    """All tests should start with an empty registry of TraceItems."""
    TraceItem._registry.clear()  # pylint: disable=protected-access



class TestCreation:
    """Unit tests focussing on the way TraceItem instances can be created"""
    @staticmethod
    def test_direct_instantiation():
        item = TraceItem(id_="TEST1")
        assert item.id == "TEST1"
        assert len(item.traced_to) == 0

    @staticmethod
    def test_direct_instantiation_with_traced_items():
        traced = [TraceItem("T1"), TraceItem("T2")]
        item = TraceItem("R1", traced_to=traced)
        assert item.id == "R1"
        assert item.traced_to == traced


class TestRegistry:
    """Unit tests focussing on the behaviour of the registry and get_by_id method."""
    @staticmethod
    def test_create_new_if_not_found():
        item = TraceItem.get_by_id("REQ1")
        assert item.id == "REQ1"

    @staticmethod
    def test_get_existing_if_present1():
        """Case 1: the original instance was created using the ``get_by_id`` method"""
        original_req = TraceItem.get_by_id("REQ1")
        new_req = TraceItem.get_by_id("REQ1")
        assert new_req is original_req


class TestAddTrace:
    """Unit tests focussing on the ``add_trace`` method."""
    @staticmethod
    def test_adds_bidirectional_link():
        req = TraceItem.get_by_id("req")
        test = TraceItem.get_by_id("test")
        TraceItem.add_trace(req, test)
        assert req in test.traced_to
        assert test in req.traced_to
