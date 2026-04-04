from datetime import timedelta


class TransportLine:
    def __init__(self, name, transport_type, origin, destination, expected_time):
        self.name = name
        self.transport_type = transport_type
        self.origin = origin
        self.destination = destination
        self.expected_time = expected_time


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
        if self.delay_minutes > 0:
            return f"{self.line.name} on {self.date.strftime('%Y-%m-%d')}: delayed by {self.delay_minutes} mins ({self.delay_reason})"
        return f"{self.line.name} on {self.date.strftime('%Y-%m-%d')}: on time"


class User:
    def __init__(self, name, home, school):
        self.name = name
        self.home = home
        self.school = school
        self.trips = []

    def add_trip(self, trip):
        self.trips.append(trip)
