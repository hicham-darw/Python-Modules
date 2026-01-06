from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """ abstract base class """
    def __init__(self, stream_id: str, type_stream: str) -> None:
        self.stream_id: str = stream_id
        self.type_stream: str = type_stream
        self.count_processed: int = 0
        self.count_errors: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data"""
        pass

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        """ filter data batch """
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """ get statistics """
        return {'processed': 0}


class SensorStream(DataStream):
    """ Sensor Stream """
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, " Environmental Data")
        self.total_temp: float = 0
        self.number_of_temp: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if isinstance(data_batch, list):
                self.count_processed = len(data_batch)
                for data in data_batch:
                    tmp: list[Any] = data.split(':')
                    if tmp[0] == 'temp':
                        self.total_temp += float(tmp[1])
                        self.number_of_temp += 1
                ret = f"Sensor analysis: {self.count_processed} "
                ret += "readings processed, avg temp: "
                ret += f"{self.total_temp / self.number_of_temp}°C\n"
                return ret
        except Exception:
            self.count_errors += 1
            return 'Error: Inavlid sensor data\n'

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            lst: list[Any] = [int(0)]
            if isinstance(data_batch, list):
                for data in data_batch:
                    tmp: list[Any] = data.split(':')
                    if tmp[0] == 'alert':
                        lst[0] += 1
            return lst
        except Exception:
            print("Invalid data!")
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: dict[str, Union[str, int, float]] = {}
        stats['processed'] = self.count_processed
        stats['stream_id'] = self.stream_id
        return stats


class TransactionStream(DataStream):
    """ transaction stream """
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")
        self.net_flow: int = 0
        self.count_operations: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if isinstance(data_batch, list):
                self.count_processed = len(data_batch)
                for data in data_batch:
                    tmp: list[Any] = data.split(':')
                    if tmp[0] == 'buy':
                        self.net_flow += float(tmp[1])
                    elif tmp[0] == 'sell':
                        self.net_flow -= float(tmp[1])
                    self.count_operations += 1
                sign: str = '+' if self.net_flow > 0 else '-'
                ret = f"Transaction analysis: {self.count_processed} "
                ret += f"operations, net flow: {sign}{self.net_flow} units\n"
                return ret
        except Exception:
            self.count_errors += 1
            return "Error: Invalid transaction data\n"

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        try:
            large_transaction: int = 0
            if isinstance(data_batch, list):
                for data in data_batch:
                    tmp: list[Any] = data.split(':')
                    if float(tmp[1]) > 200:
                        large_transaction += 1
            return [large_transaction]
        except Exception:
            print("Invalid data!")
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: dict[str, Union[str, int, float]] = {}
        stats['processed'] = self.count_processed
        stats['stream_id'] = self.stream_id
        return stats


class EventStream(DataStream):
    """ event stream """
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, 'System Events')
        self.count_events: int = 0
        self.error_detected: int = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if isinstance(data_batch, list):
                self.count_processed = len(data_batch)
                for event in data_batch:
                    if event == 'error':
                        self.error_detected += 1
                    self.count_events += 1
                ret = f"Event analysis: {self.count_events} events,"
                ret += f" {self.error_detected} error detected\n"
                return ret
        except Exception:
            self.count_errors += 1
            return 'Error: Invalid events data\n'

    def filter_data(self,
                    data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats: dict[str, Union[str, int, float]] = {}
        stats['processed'] = self.count_processed
        stats['stream_id'] = self.stream_id
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: list[DataStream] = []

    def append_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def all_stats(self) -> None:
        try:
            for stream in self.streams:
                if isinstance(stream, SensorStream):
                    result = stream.get_stats()
                    print(f"- Sensor data: {result['processed']}", end='')
                    print(" readings processed")
                elif isinstance(stream, TransactionStream):
                    result = stream.get_stats()
                    print(f"- Transaction data: {result['processed']}", end='')
                    print(" operations processed")
                elif isinstance(stream, EventStream):
                    result = stream.get_stats()
                    print(f"- Event data: {result['processed']}", end='')
                    print(" events processed")
        except Exception:
            print("Error: Invalid data!")

    def filter_all_streams(self,
                           criteria: str = "high-priority") -> Dict[str, int]:
        try:
            dic: Dict[str, int] = {}
            for stream in self.streams:
                if isinstance(stream, SensorStream):
                    result: list[Any] = stream.filter_data([
                        'temp:25.1',
                        'humidity:65',
                        'alert:True'], criteria)
                    if len(result) > 0:
                        dic['critical_alert'] = result[0]
                elif isinstance(stream, TransactionStream):
                    result = stream.filter_data(['buy:100',
                                                 'sell:1001'], criteria)
                    if len(result) > 0:
                        dic['large_transaction'] = result[0]
                    else:
                        dic['large_transaction'] = 0
            return dic
        except Exception:
            print("Error filter streams")
            return {}


if __name__ == '__main__':
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

#   processing Sensor data ---------------------------------
    print("Initializing Sensor Stream...")
    sensor_id = 'SENSOR_001'
    sensor_stream = SensorStream(sensor_id)
    print(f"Stream ID: {sensor_stream.stream_id}, ", end='')
    print(" Type: {sensor_stream.type_stream}")
    sensor_data = ['temp:22.5', 'humidity:65', 'pressure:1013']
    print(f"Processing sensor batch: {sensor_data}")
    print(sensor_stream.process_batch(sensor_data))

#   processing transaction data -------------------------
    print("Initializing Transaction Stream...")
    trans_id = 'TRANS_001'
    trans_stream = TransactionStream(trans_id)
    print(f"Stream ID: {trans_id}, Type: {trans_stream.type_stream}")
    trans_data = ['buy:100', 'sell:150', 'buy:75', 'buy: 175']
    print(f"Processing transaction batch: {trans_data}")
    print(trans_stream.process_batch(trans_data))

#   processing event data -----------------------------
    print("Initializing Event Stream...")
    event_id = 'EVENT_001'
    event_stream = EventStream(event_id)
    print(f"Stream ID: {event_stream.stream_id}, ", end='')
    print(f"Type: {event_stream.type_stream}")
    event_data = ['login', 'error', 'logout']
    print(f"Processing event batch: {event_data}")
    print(event_stream.process_batch(event_data))

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    stream_processor = StreamProcessor()
    stream_processor.append_stream(sensor_stream)
    stream_processor.append_stream(trans_stream)
    stream_processor.append_stream(event_stream)

    print("Batch 1 Results:")
    stream_processor.all_stats()
    print("\nStream filtering active: High-priority data only")
    result = stream_processor.filter_all_streams()
    print("Filtered results: ", end='')
    print(f"{result['critical_alert']} critical sensor alerts, ", end='')
    print(f"{result['large_transaction']} large transaction\n")

    print("All streams processed successfully. Nexus throughput optimal.")
