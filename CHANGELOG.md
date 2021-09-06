
# Changelog

## V1.0.1
### Fixes
* Remove empty lines in CSV output on windows
  Closes #2

## V1.0.0
### API changes:
* ``TraceItem`` has been degraded to a simple dataclass. The methods ``get_by_id`` and ``add_trace`` have been removed. Adding items (rows or columns) to a ``TraceabilityMatrix`` is now done by using ``TraceabilityMatrix.add_row(row_id)`` and ``TraceabilityMatrix.add_column(column_id)``. Traces between rows and columns are created by calling ``TraceabilityMatrix.add_trace(row_id, column_id)``. To all these methods, the ``id`` is passed as a string. The end user does not need to work with the ``TraceItem`` class any more.
