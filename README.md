# tracematrix
A Python tool to create a traceability matrix.

## Scope
This package focuses on generating the traceability matrix itself.
As the APIs and export formats of different test management and/or requirement management tools can be very different, the data acquisition and conversion is not in the scope of this package. However, it aims to provide a convenient way to create the individual items (e.g. requirements, testcases or any other traceable item) and traces between them.

## How to use this package
Currently it is only possible to use this package programmatically in your own script.

You start by creating an instance of ``TraceabilityMatrix``.
The output format is controlled by the ``reporter`` parameter.
By default ``CsvReporter`` is used, but you can also generate HTML output by passing ``HtmlReporter``.
```Python
from tracematrix.matrix import TraceabilityMatrix
from tracematrix.reporters import HtmlReporter

matrix = TraceabilityMatrix(reporter=HtmlReporter)
```

In the next step you add rows and columns to the ``matrix``. Rows and columns can represent anything
which may be traced against each other. Let's assume that we want to see traces between requirements and test cases.
This is where your own logic comes into play - the way you determine which items exist and what is traced against each other is up to you and what the source of your data is. For this example, we just use some hardcoded values.
```Python
for testcase_id in ("TC_1", "TC_2", "TC_3"):
    matrix.add_row(testcase_id)
for requirement_id in ("REQ_1", "REQ_2", "REQ_3", "REQ_4"):
    matrix.add_column(requirement_id)

matrix.add_trace("TC_1", "REQ_1")
matrix.add_trace("TC_2", "REQ_2")
matrix.add_trace("TC_2", "REQ_3")
```
Note that rows and columns must be unique - you cannot have two rows or two columns with the same ``id``.
When you add a trace between a row and a column, the ``TraceabilityMatrix`` will look up the corresponding
``TraceItem`` instances itself.

Finally, you can save the output to disk:
```Python
matrix.write_matrix("traceability_matrix.html)
```
