from datetime import datetime
from models import TransportLine, Trip, User
from data import TripStats

def main():
    student = User("Peter", "Tuen Mun", "Kowloon Tong")

    mtr_route = TransportLine("Tuen Mun Line", "MTR", "Tuen Mun", "Nam Cheong", 30)
    bus_route = TransportLine("960", "Bus", "Tuen Mun", "Admiralty", 50)
    minibus_route = TransportLine("44", "Minibus", "Tuen Mun", "Mei Foo", 40)

    today = datetime.now()

    trip1 = Trip(mtr_route, today, today.replace(hour=7, minute=40, second=0))
    student.add_trip(trip1)

    trip2 = Trip(bus_route, today, today.replace(hour=8, minute=15, second=0))
    trip2.add_delay("Heavy traffic near tunnel", 18)
    student.add_trip(trip2)

    trip3 = Trip(minibus_route, today, today.replace(hour=7, minute=55, second=0))
    trip3.add_delay("Typhoon Signal No. 3 Rain delay", 30)
    student.add_trip(trip3)

    print("Peter's travel record")
    for trip in student.trips:
        print(trip)

    avg_time = TripStats.average_travel_time(student.trips)
    on_time = TripStats.on_time_ratio(student.trips)
    worst_trip = TripStats.most_delayed_trip(student.trips)

    print(f"\nAverage travel time: {avg_time:.1f} mins")
    print(f"On-time ratio: {on_time:.1f}%")

    if worst_trip is not None:
        print(f"Most delayed route: {worst_trip.line.name} ({worst_trip.delay_minutes} mins)")


if __name__ == "__main__":
    main()
