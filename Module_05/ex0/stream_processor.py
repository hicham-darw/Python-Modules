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

    def validate(self, data: int) -> bool:
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
        if not self.validate(format):
            return ("Invalid data!")
        else:
            total = 0
            count = 0
            for s in format:
                total += s
                count += 1
            format = f"Processed {len(format)} numeric values, sum={total}, avg={total / count}"
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
            print(format)

    def validate(self, data: str) -> bool:
        if not isinstance(data, str):
            return False
        return True

    def format_output(self, result: str) -> str:
        if not self.validate(result):
            return ("Invalid data!")
        else:
            words = len(result.split())
            chars = 0
            for s in result.split():
                chars += len(s)
            format = f"Processed text: {chars} characters, {words} words"
            return (format)



class LogProcessor(DataProcessor):
    def __init__(self):
        pass

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid!, must be string")
        else:
            print("Output: [ALERT] ERROR level detected: Connection timeout")

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return True

    def format_output(self, result: str) -> str:
        if not self.validate(result):
            return ("Invalid data!")
        else:
            return f"[{result}] {result} level detected: System Ready"


if __name__ == '__main__':
#   Numeric Processor
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    lst = [1, 2, 9, 4, 5]
    print(f"Processing data: {lst}")
    print("Validation: Numeric data verified")
    proc = NumericProcessor()
    proc.process(lst)
    print()

#   text Processor
    print("Initializing Text Processor...")
    print("Processing data: \"Hello Nexus World\"")
    text = "Hello Nexus World"
    print("Validation: Text data verified")
    proc = TextProcessor()
    proc.process(text)
    print()

#   Log Processor
    print("Initializing Log Processor...")
    text = "\"ERROR: Connection timeout\""
    print(f"Processing data: {text}")
    print("Validation: Log entry verified")

    proc = LogProcessor()
    proc.process(text)
    print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    proc_data = [[1, 2, 3], "Hello World!!", "INFO"]
    index = 0
    for proc, data in zip(processors, proc_data):
        print(f"Result {index}: ", end='')
        print(proc.format_output(data))
        index += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")
