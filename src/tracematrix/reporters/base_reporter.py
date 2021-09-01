from abc import ABC, abstractstaticmethod


class Reporter(ABC):
    @abstractstaticmethod
    def write(outputfile, testcases, requirements):
        pass
