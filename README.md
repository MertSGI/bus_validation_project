
# Bus Data Validation Script 🚌

This Python script validates and analyzes bus route data based on specific rules for input integrity, format, and logical consistency.

---

## 🚀 Features

- **Type and Required Field Validation**: Ensures that fields have the correct data types and required fields are populated.
- **Format Validation**: Checks field values against predefined patterns (e.g., stop name and time formats).
- **Stop Count by Bus Line**: Counts and displays the number of stops for each bus line.
- **Arrival Time Validation**: Ensures that arrival times are in ascending order for consecutive stops.
- **On-Demand Stop Validation**: Identifies misclassified on-demand stops.

---

## 🛠️ How to Use

1. **Run the Script**  
   Execute the script using Python:
   ```bash
   python bus_validation.py
   ```

2. **Provide Input**  
   The script expects a JSON string representing bus stop data. Example input:
   ```json
   [
       {"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Avenue", "next_stop": 3, "stop_type": "S", "a_time": "08:12"},
       {"bus_id": 128, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 5, "stop_type": "O", "a_time": "08:19"}
   ]
   ```

3. **Review Outputs**  
   The script will validate the input data and display results for each validation step.

---

## 📖 Validation Steps

1. **Type and Required Field Validation**  
   - Checks that all required fields are present and have the correct data type.

2. **Format Validation**  
   - Ensures the following formats:
     - `stop_name`: Must start with an uppercase letter and end with "Road", "Avenue", "Street", or "Boulevard".
     - `stop_type`: Can be empty or one of `S`, `O`, `F`.
     - `a_time`: Must be in HH:MM format.

3. **Stop Count by Bus Line**  
   - Outputs the number of stops for each bus line.

4. **Arrival Time Validation**  
   - Ensures arrival times are in ascending order.

5. **On-Demand Stop Validation**  
   - Identifies on-demand stops that are incorrectly classified.

---

## 🧪 Example Input/Output

### Input
```json
[
    {"bus_id": 128, "stop_id": 1, "stop_name": "Prospekt Avenue", "next_stop": 3, "stop_type": "S", "a_time": "08:12"},
    {"bus_id": 128, "stop_id": 3, "stop_name": "Elm Street", "next_stop": 5, "stop_type": "O", "a_time": "08:19"}
]
```

### Output
```
Type and required field validation: 0 errors
stop_name: 0
stop_type: 0
a_time: 0

Format validation: 0 errors
stop_name: 0
stop_type: 0
a_time: 0

Line names and number of stops:
bus_id: 128, stops: 2

Arrival time test:
OK

On demand stops test:
OK
```

---

## 📂 Project Structure

```
bus_validation_python_project/
├── bus_validation.py    # Main Python script
└── README.md            # Documentation
```

---

## 🛠️ Requirements

- Python 3.x

---

## 📬 Contributing

Contributions are welcome! If you find any issues or have ideas for new features, feel free to create an issue or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

### Thank you for using the Bus Validation Script! 😊
