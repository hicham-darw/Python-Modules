import sys
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


# Base class ------------->
class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass


    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass


    def format_output(self, result: str) -> str:
        pass


# specialized classes ----------------->
class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self.total_numbers = 0
        self.average = 0
        self.size = 0
        print("Initializing Numeric Processor...")

    def process(self, data: int) -> str:
        try:
            int(data)
            self.total_numbers += data
            self.size += 1
        except Exception:
            return "Not valide"
        else:
            return "valide"
    def fromat_output(self, result: str) -> str:
        return (str)


    def validate(self, data: int) -> bool:
        pass

class TextProcessor(DataProcessor):
    def __init__(self):
        self.characters = 0
        self.words = 0

    def process(self, data: str) -> str:
        pass

    def fromat_output(self, result: str) -> str:
        pass


    def validate(self, data: str) -> bool:
        pass


class LogProcessor(DataProcessor):
    def process(self, data: str) -> str:
        pass


    def fromat_output(self, result: str) -> str:
        pass


    def validate(self, data: str) -> bool:
        pass

if __name__ == '__main__':
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    numeric_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()

    lst = [1, 2, "hicham", 4, 5]
    for num in lst:
        if numeric_proc.process(num) != 'Valide':
            print(f"Processing data: \"ERROR: not valide number\"")
            break
    




