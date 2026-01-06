from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol
import collections

#   abstract base class --------------------->
class ProcessingPipeline(ABC):
    """ Processing pipeline """
    @abstractmethod
    def process(self, data: Any) -> Any:
        """ Processing data """
        pass
    pass




#   Data Adapter ----------------------------->
class JSONAdapter(ProcessingPipeline):
    
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        pass

    """ JSON Adapter inherit processPipeline"""
    def process(self, data: Any) -> Any:
        """ Processing data """
        pass

    pass


class CSVAdapter(ProcessingPipeline):
    """ CSV Adapter inherit processPipeline"""
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id: str = pipeline_id
        pass

    def process(self, data: Any) -> Any:
        """ Processing data """
        pass

    pass


class StreamAdapter(ProcessingPipeline):
    """ Stream Adapter inherit processPipeline"""
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        pass
    
    def process(self, data: Any) -> Any:
        """ Processing data """
        pass
    pass


#   Processing stages ----------------------------->
class InputStage(Protocol):
    """ input stage """

    def process(self, data: Any) -> Any:
        """ Processing input stage """
        pass

    pass


class TransformStage(Protocol):
    """ transform stage """
    def process(self, data: Any) -> Any:
        """ Processing transfrom stage """
        pass

    pass


class OutputStage(Protocol):
    """ output stage """
    def process(self, data: Any) -> Any:
        """ Processing output stage """
        pass

    pass