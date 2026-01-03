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

    def process(self, data: int) -> str:
        if not self.validate(data):
            raise ValueError("invalid data! must be list of numbers")
        else:
            format = f"Output: Processed {self.size} numeric values, sum={self.total_numbers}, avg={self.total_numbers / self.size}"
            print(format)
            self.format_output(format)

    def validate(self, data: int) -> bool:
        print("Validation: Numeric data verified")
        if not isinstance(data, list):
            return False
        try:
            for elem in data:
                int(elem)
                self.total_numbers += elem
                self.size += 1
        except Exception:
            return False
        return True
    
    def format_output(self, format) -> str:
        return format



class TextProcessor(DataProcessor):
    def __init__(self):
        self.characters = 0
        self.words = 0

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Inavlid!, must be string")
        else:
            self.words = len(data.split())
            for d in data.split():
                self.characters += len(d)
            format = f"Output: Processed text: {self.characters} characters, {self.words} words"
            print(self.format_output(format))

    def validate(self, data: str) -> bool:
        print("Validation: Text data verified")
        if not isinstance(data, str):
            return False
        return True

    def format_output(self, result: str) -> str:
        return (result)

class LogProcessor(DataProcessor):
    def __init__(self):
        pass

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError('INFO: System ready"')
        else:
            print("Output: [ALERT] ERROR level detected: Connection timeout")


    def validate(self, data: Any) -> bool:
        print("Validation: Log entry verified")
        if not isinstance(data, str):
            return False
        return True
    
    def format_output(self, result: str) -> str:
        pass

if __name__ == '__main__':
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    lst = [1, 2, 9, 4, 5]
    print(f"Processing data: {lst}")
    proc = NumericProcessor()
    proc.process(lst)
    print()
    
    print("Initializing Text Processor...")
    print("Processing data: \"Hello Nexus World\"")
    text = "Hello Nexus World"
    proc = TextProcessor()
    proc.process(text)
    print()

    print("Initializing Log Processor...")
    text = "\"ERROR: Connection timeout\""
    print(f"Processing data: {text}")
    proc = LogProcessor()
    proc.process(text)
    print()

    print("=== Polymorphic Processing Demo ===")
    # add a list for loop to polymorphic processing!



