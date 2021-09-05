from tracematrix.item import TraceItem


class TestItemCreation:
    """Unit tests focussing on the way TraceItem instances can be created"""

    @staticmethod
    def test_direct_instantiation():
        item = TraceItem(id="TEST1")
        assert item.id == "TEST1"
        assert len(item.traced_to) == 0

    @staticmethod
    def test_direct_instantiation_with_traced_items():
        traced = [TraceItem("T1"), TraceItem("T2")]
        item = TraceItem("R1", traced_to=traced)
        assert item.id == "R1"
        assert item.traced_to == traced
