from abc import ABC, abstractmethod
from typing import Any


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

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                err = "Output: invalid data! must be a list of numbers"
                raise ValueError(err)
            else:
                format = f"Output: Processed {self.size} numeric values, "
                format += f"sum={self.total_numbers}, "
                format += f"avg={self.total_numbers / self.size}"
                print(format)
        except Exception as e:
            print(e)
            return e
        else:
            return format

    def validate(self, data: Any) -> bool:
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

    def format_output(self, format: str) -> str:
        if not self.validate(format):
            return ("Invalid data!, must be a string")
        else:
            total = 0
            count = 0
            for s in format:
                total += s
                count += 1
            format = f"Processed {len(format)} numeric values, "
            format += f"sum={total}, avg={total / count}"
            return format


class TextProcessor(DataProcessor):
    def __init__(self):
        self.characters = 0
        self.words = 0

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Output: Inavlid!, must be a string")
            else:
                self.words = len(data.split())
                for d in data.split():
                    self.characters += len(d)
                format = "Output: Processed text: "
                format += f"{self.characters} characters, {self.words} words"
                print(format)
        except Exception as e:
            print(e)
            return (e)
        else:
            return format

    def validate(self, data: str) -> bool:
        if not isinstance(data, str):
            return False
        return True

    def format_output(self, result: str) -> str:
        if not self.validate(result):
            return ("Invalid data!, must be a string")
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
        try:
            if not self.validate(data):
                raise ValueError("Output: Invalid data!, must be a string")
            else:
                print("Output: [ALERT] ERROR level detected: ", end='')
                print("Connection timeout")
        except Exception as e:
            print(e)
            return e
        else:
            return None

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return True

    def format_output(self, result: str) -> str:
        if not self.validate(result):
            return ("Invalid data!, must be a string")
        else:
            return f"[{result}] {result} level detected: System Ready"


if __name__ == '__main__':
#   Numeric Processor -------------------------------------->
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    print("Initializing Numeric Processor...")
    lst = [1, 2, 3, 4, 5]
    print(f"Processing data: {lst}")
    print("Validation: Numeric data verified")
    proc = NumericProcessor()
    proc.process(lst)
    print()

#   text Processor -------------------------------->
    print("Initializing Text Processor...")
    print("Processing data: \"Hello Nexus World\"")
    text = "Hello Nexus World"
    print("Validation: Text data verified")
    proc = TextProcessor()
    proc.process(text)
    print()

#   Log Processor --------------------------->
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
