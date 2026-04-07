from abc import ABC, abstractmethod
from datetime import timedelta


class TransportLine(ABC):
    def __init__(self, name, origin, destination, expected_time):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.expected_time = expected_time


    @abstractmethod
    def get_transport_type(self):
        pass
        
    @abstractmethod
    def calculate_fare(self, distance):
        pass

class MTRLine(TransportLine):
    def __init__(self, name, origin, destination, expected_time, _light_rail-False):
        super(),__init__(name, origin, destination, expected_time_
        self._light_rail = _light_fail

    def get_transport_type(self):
        return "Light Rail" if self._light_rail else "MTR"

    def calucate_fare(self, distance):
        return 5.0 + (distance * 1.2)

class BusLine(TransportLine):
    def __init__(self, name, origin, destination, expected_time, is_express=False):
        super().__init__(name, origin, destnation, expected_time)
        self.is_express = is_express

    def get_transport_type(self):
        return "Express Bus" if self.is_express else "Regular Bus"

    def calculate_fare(self, distance):
        return 21 if self.is_express else 8.0 + (distance *0.8)

class MinibusLine(TransportLine):
    def get_transport_type(self):
        return "Minibus"

    def calculate_fare(self, distance):
        return 5.5
        
class Trip:
    def __init__(self, line, date, start_time):
        self.line = line
        self.date = date
        self.start_time = start_time
        self.expected_end = start_time + timedelta(minutes=line.expected_time)
        self.actual_end = self.expected_end
        self.delay_reason = None
        self.delay_minutes = 0

    def add_delay(self, reason, minutes):
        self.delay_reason = reason
        self.delay_minutes += minutes
        self.actual_end += timedelta(minutes=minutes)

    def get_actual_duration(self):
        return (self.actual_end - self.start_time).total_seconds() / 60

    def is_delayed(self, threshold=5):
        return self.delay_minutes > threshold

    def __str__(self):
        status =f"delayed by {self.delay_minutes} mins ({self.delay_reason})" if self.delay_minutes > 0 else "on time"
        return f"[{self.line.get_transport_type()}] {self.line.name} on {self.date.strftime('%Y-%m-%d')} {status}"

class User:
    def __init__(self, name, home, school):
        self.name = name
        self.home = home
        self.school = school
        self.trips = []

    def add_trip(self, trip):
        self.trips.append(trip)
