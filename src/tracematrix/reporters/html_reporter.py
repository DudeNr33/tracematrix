"""
Reporter for HTML output.
"""
from typing import List
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from tracematrix.item import TraceItem
from tracematrix.reporters.base_reporter import Reporter


class HtmlReporter(Reporter):
    """Creates report in .html format"""
    env = Environment(
        loader=FileSystemLoader(Path(__file__).parent),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("template.html")

    @classmethod
    def write(
        cls, outputfile: str, testcases: List[TraceItem], requirements: List[TraceItem]
    ) -> None:
        with open(outputfile, "w", encoding="utf8") as outfile:
            outfile.write(
                cls.template.render(testcases=testcases, requirements=requirements)
            )
