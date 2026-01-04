from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id, type_stream):
        self.stream_id = stream_id
        self.type = type_stream

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):
    def __init__(self, stream_id,):
        super().__init__(stream_id, "Environmental Data")
        self.data_dic = {}
        self.alerts = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        data = self.filter_data(data_batch)
        if  len(data) < 1:
            return ("Invalid data!")
        return f"Sensor analysis: {len(self.data_dic)} readings processed, avg temp: {self.data_dic['temp']}°C"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        try:
            for val in data_batch:
                tmp = val.split(":")
                if tmp[0] not in ['temp', 'humidity', 'pressure']:
                    raise Exception
                self.data_dic[tmp[0]] = float(tmp[1])
                if (float(tmp[1]) > 50):
                    self.alerts += 1
        except Exception:
            return []
        else:
            return [self.data_dic]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        print(f"- Sensor data: {len(self.data_dic)} readings processed")
        return self.data_dic


class TransactionStream(DataStream):
    def __init__(self, stream_id):
        super().__init__(stream_id, "Financial Data")
        self.data_dic = {}
        self.large_transaction = 0
        self.flow = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        self.filter_data(data_batch)
        if len(self.data_dic) < 1:
            return "Transaction analysis: rejected!\n"
        else:
            return f"Transaction analysis: {len(trans_stream.data_dic)} operations, net flow: {trans_stream.flow} units\n"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        try:
            if not isinstance(data_batch, list):
                raise Exception
            for val in data_batch:
                tmp = val.split(":")
                if tmp[0] not in ['buy', 'sell']:
                    raise Exception
                self.data_dic[tmp[0]] = float(tmp[1])
                if tmp[0] == 'buy':
                    self.flow += float(tmp[1])
                elif tmp[0] == 'sell':
                    self.flow -= float(tmp[1])
                if float(tmp[1]) > 125:
                    self.large_transaction += 1
            return [self.dic]
        except Exception:
            return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        print(f"- Event data: {len(self.data_dic)} events processed")
        return self.data_dic


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "System Events")
        self.total_events = 0
        self.total_err = 0
    
    def process_batch(self, data_batch: List[Any]) -> str:
        if len(self.filter_data(data_batch)) < 1:
            return "corrupted data!\n"
        else:
            return f"Event analysis: {self.total_events} events, {self.total_err} error detected\n"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        try:
            if not isinstance(data_batch, list):
                raise Exception
            for d in data_batch:
                if d not in ['login', 'error', 'logout']:
                    raise Exception
                if d in ['error']:
                    self.total_err += 1
                self.total_events += 1
        except Exception:
            return []
        else:
            return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        print(f"- Sensor data: {self.total_events} readings processed")
        return {'total_events': self.total_events, 'total_events': self.total_err}


if __name__ == '__main__':
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    print("Initializing Sensor Stream...")
    sensor_id = "SENSOR_001"
    sensor_stream = SensorStream(sensor_id)
    print(f"Stream ID: {sensor_stream.stream_id}, Type: {sensor_stream.type}")
    sensor_lst = ['temp:22.5', 'humidity:65', 'pressure:1013']
    print(f"Processing sensor batch: {sensor_lst}")
    print(sensor_stream.process_batch(sensor_lst))
    print()

    print("Initializing Transaction Stream...")
    trans_id = "TRANS_001"
    trans_stream = TransactionStream(trans_id)
    print(f"Stream ID: {trans_stream.stream_id}, Type: {trans_stream.type}")
    trans_lst = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {trans_lst}")
    print(trans_stream.process_batch(trans_lst))

    print("Initializing Event Stream...")
    event_id = "EVENT_001"
    event_stream = EventStream(event_id)
    events_lst = ['login', 'error', 'logout']
    print(f"Processing event batch: {events_lst}")
    print(event_stream.process_batch(events_lst))
    
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    print("Batch 1 Results:")
    all_in = [sensor_stream, trans_stream, event_stream]
    for l in all_in:
        l.get_stats()            
    print()

    print("Stream filtering active: High-priority data only")
    print(f"Filtered results: {all_in[0].alerts} critical sensor alerts, {all_in[1].large_transaction} large transaction")
    print("\nAll streams processed successfully. Nexus throughput optimal.")