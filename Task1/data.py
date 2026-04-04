class TripStats:
    @staticmethod
    def average_travel_time(trips):
        if len(trips) == 0:
            return 0
        total = 0
        for trip in trips:
            total += trip.get_actual_duration()
        return total / len(trips)

    @staticmethod
    def on_time_ratio(trips, threshold=5):
        if len(trips) == 0:
            return 0
        on_time = 0
        for trip in trips:
            if not trip.is_delayed(threshold):
                on_time += 1
        return on_time / len(trips) * 100

    @staticmethod
    def most_delayed_trip(trips):
        if len(trips) == 0:
            return None
        return max(trips, key=lambda trip: trip.delay_minutes)
