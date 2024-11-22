
import json
import re

# Function to validate types and required fields
def validate_type_and_required_fields(data, key_types, allow_empty, value_choices):
    errors = {key: 0 for key in key_types.keys()}
    total_errors = 0

    for item in data:
        if not isinstance(item, dict):
            continue
        for key, value in item.items():
            if any([
                not isinstance(value, key_types.get(key)),
                not value and not allow_empty.get(key),
                value_choices.get(key) and value not in value_choices.get(key)
            ]):
                errors[key] += 1
                total_errors += 1

    print(f"Type and required field validation: {total_errors} errors")
    for key, count in errors.items():
        print(f"{key}: {count}")

# Function to validate formats
def validate_format(data, format_rules):
    errors = {key: 0 for key in format_rules.keys()}
    total_errors = 0

    for item in data:
        for key, rule in format_rules.items():
            if not (rule['req'] and not item[key]) and re.fullmatch(rule['format'], str(item[key])) is None:
                errors[key] += 1
                total_errors += 1

    print(f"Format validation: {total_errors} errors")
    for key, count in errors.items():
        print(f"{key}: {count}")

# Function to count stops per bus line
def count_stops_per_line(data):
    stop_counts = {}
    for stop in data:
        bus_id = stop['bus_id']
        if bus_id not in stop_counts:
            stop_counts[bus_id] = 0
        stop_counts[bus_id] += 1

    print("Line names and number of stops:")
    for bus_id, count in stop_counts.items():
        print(f"bus_id: {bus_id}, stops: {count}")

# Function to validate arrival times
def validate_arrival_times(data):
    print("Arrival time test:")
    errors = 0
    stops_per_line = {}

    for stop in data:
        stops_per_line.setdefault(stop['bus_id'], []).append(stop)

    for bus_id, stops in stops_per_line.items():
        stops = sorted(stops, key=lambda x: x['stop_id'])
        for i in range(len(stops) - 1):
            if stops[i]['a_time'] >= stops[i + 1]['a_time']:
                print(f"bus_id line {bus_id}: wrong time on station {stops[i + 1]['stop_name']}")
                errors += 1
                break

    if errors == 0:
        print("OK")

# Function to check on-demand stops
def validate_on_demand_stops(data):
    print("On demand stops test:")
    all_stops = {}
    for stop in data:
        all_stops.setdefault(stop['bus_id'], []).append(stop)

    all_stop_names = {stop['stop_name'] for stops in all_stops.values() for stop in stops}
    transfer_stops = {stop['stop_name'] for stops in all_stops.values() for stop in stops if stop['stop_type'] in ['S', 'F']}
    on_demand_stops = {stop['stop_name'] for stops in all_stops.values() for stop in stops if stop['stop_type'] == 'O'}
    invalid_stops = on_demand_stops & (transfer_stops | {stop for stop in all_stop_names if list(all_stop_names).count(stop) > 1})

    if invalid_stops:
        print(f"Wrong stop type: {sorted(invalid_stops)}")
    else:
        print("OK")

# Main script
if __name__ == "__main__":
    json_str = input("Enter JSON data:
")
    bus_data = json.loads(json_str)

    key_types = {
        'bus_id': int,
        'stop_id': int,
        'stop_name': str,
        'next_stop': int,
        'stop_type': str,
        'a_time': str
    }
    allow_empty = {
        'bus_id': False,
        'stop_id': False,
        'stop_name': False,
        'next_stop': True,
        'stop_type': True,
        'a_time': False
    }
    value_choices = {
        'bus_id': None,
        'stop_id': None,
        'stop_name': None,
        'next_stop': None,
        'stop_type': ['', 'S', 'O', 'F'],
        'a_time': None
    }
    format_rules = {
        'stop_name': {'type': str, 'req': True, 'format': r'^[A-Z].*? (Road|Avenue|Street|Boulevard)$'},
        'stop_type': {'type': str, 'req': False, 'format': r'^[SOF]?$'},
        'a_time': {'type': str, 'req': True, 'format': r'^([0-1][0-9]|2[0-3]):[0-5][0-9]$'}
    }

    # Perform validations and checks
    validate_type_and_required_fields(bus_data, key_types, allow_empty, value_choices)
    validate_format(bus_data, format_rules)
    count_stops_per_line(bus_data)
    validate_arrival_times(bus_data)
    validate_on_demand_stops(bus_data)
