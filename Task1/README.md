# HK Daily Commute Tracker

This is a Python project that simulates and analyzes a student's daily commute in Hong Kong using different transport routes (MTR, bus, minibus). It records several trips on the same day and then prints basic statistics like average travel time, on-time ratio, and the most delayed route.

## Features

- Define transport routes with expected travel time (MTR, bus, minibus).
- Record individual trips and add delays with reasons (e.g. tunnel traffic, typhoon rain).
- Compute average travel time across all trips.
- Calculate on-time percentage based on a delay threshold (default 5 minutes).
- Identify the single most delayed trip.

## Project Structure

- `models.py`  
  Contains the core data classes
  - `TransportLine` basic information about a route (name, type, origin, destination, expected_time).
  - `Trip` one commute instance on a particular date, including delay minutes and reasons.
  - `User` a simple user with home, school, and a list of trips.

- `data.py`  
  Provides the `TripStats` utility class for calculations
  - `average_travel_time(trips)`  
  - `on_time_ratio(trips, threshold=5)`  
  - `most_delayed_trip(trips)`

- `main.py`  
  Demo script that
  - Creates one user (Peter) commuting from Tuen Mun to Kowloon Tong.
  - Sets up three routes (MTR, bus, minibus) with different expected times.
  - Creates three trips, adds realistic delays to two of them, and prints summary statistics.

## Requirements

- Python 3.8 or above (tested with standard library only).

No external packages are required.

## How to Run

1. Make sure the files are in the same folder
   - `models.py`
   - `data.py` 
   - `main.py`

2. From that folder, run

   ```bash
   python main-3.py
