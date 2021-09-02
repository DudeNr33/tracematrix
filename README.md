# tracematrix
A Python tool to create a traceability matrix.

## Scope
This package focuses on generating the traceability matrix itself.
As the APIs and export formats of different test management and/or requirement management tools can be very different, the data acquisition and conversion is not in the scope of this package. However, it aims to provide a convenient way to create the individual items (e.g. requirements, testcases or any other traceable item) and traces between them.

## How to use this package
Currently it is only possible to use this package programmatically in your own script.

All traceable items have a unique ``id`` and a set of other items that they are traced to.

To get an existing or create a new item, you can use the class method ``get_by_id(id_)``.
It will only create a new instance if no existing item with this ``id`` could be found.
This means that you don't have to keep track if you already processed this item, because
some items could appear more than once in your data (i.e. a requirement could appear on multiple test cases).

```python
from tracematrix.item import TraceItem

req1 = TraceItem.get_by_id("REQ_1")
testcase1 = TraceItem.get_by_id("TC_1")
```

Creating links between to items is done by simply passing the two items to ``TraceItem.add_trace(first, second)``.
This will create a bidirectional link between these elements and update the ``traced_to`` attribute on both.

```python
TraceItem.add_trace(req1, testcase1)
```

Currently two output formats are supported - CSV and HTML.
Default is CSV, but you can specify the reporter when creating the ``TraceabilityMatrix``:

```python
from tracematrix.reporters import HtmlReporter

matrix = TraceabilityMatrix(testcases, requirements, reporter=HtmlReporter)
matrix.create_matrix("RequirementsTraceabilityMatrix.html")
```
