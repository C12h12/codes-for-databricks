import numpy as np


class SensorAnalyzer:

    # 1. Create Sensor Array
    def create_sensor_array(
        self,
        sensor_values: list
    ) -> np.ndarray:

        return np.array(sensor_values, dtype=float)


    # 2. Validate Sensor Array
    def validate_sensor_array(
        self,
        sensor_array: np.ndarray
    ) -> bool:

        if sensor_array.size == 0:
            return False

        if not np.issubdtype(sensor_array.dtype, np.number):
            return False

        return bool(np.all(sensor_array > 0))


    # 3. Compute Sensor Statistics
    def compute_sensor_statistics(
        self,
        sensor_array: np.ndarray
    ) -> tuple:

        total = np.sum(sensor_array)
        average = round(np.mean(sensor_array), 1)
        maximum = np.max(sensor_array)

        return (total, average, maximum)

    def filter_extreme_readings(self,sensor_array:np.ndarray)->np.ndarray:
        sensor_array=sensor_array.astype(float)
        new=[]
        for i in sensor_array:
            if i>=50.0:
                new.append(i-(i*0.1))
            else:
                new.append(i)

        return np.array(new,dtype=float)

    def label_high_sensors(self,sensor_array:np.ndarray)->np.ndarray:
        avg=float(np.mean(sensor_array))
        label=[]
        for i in sensor_array:
            if i > avg:
                label.append('High')
            else:
                label.append('Normal')
        return np.array(label)

    def format_sensor_readings(self,sensor_array:np.ndarray)->np.ndarray:
        return np.array([f"{x: .2f} units"  for x in sensor_array])

# Create object
analyzer = SensorAnalyzer()


print("===== SENSOR READING ANALYSIS TESTING =====")


# 1. Create Sensor Array
print("\n1. CREATE SENSOR ARRAY")

sensor_values = [28.5, 415.0, 30.7, 92.1]

sensor_array = analyzer.create_sensor_array(sensor_values)

print("Input :", sensor_values)
print("Output:", sensor_array)
print("Data Type:", sensor_array.dtype)


# 2. Validate Sensor Array
print("\n2. VALIDATE SENSOR ARRAY")

valid_array = np.array([20.0, 60.0, 40.0])
invalid_array = np.array([923.0, -40.0, 810.0])
empty_array = np.array([])

print("Valid data   :", analyzer.validate_sensor_array(valid_array))
print("Invalid data :", analyzer.validate_sensor_array(invalid_array))
print("Empty data   :", analyzer.validate_sensor_array(empty_array))


# 3. Compute Sensor Statistics
print("\n3. COMPUTE SENSOR STATISTICS")

stats_array = np.array([20.0, 60.0, 40.0])

print("Input :", stats_array)
print("Output:", analyzer.compute_sensor_statistics(stats_array))


# 4. Filter Extreme Readings
print("\n4. FILTER EXTREME READINGS")

extreme_array = np.array([100.0, 50.0, 40.0, 60.0])

print("Input :", extreme_array)
print("Output:", analyzer.filter_extreme_readings(extreme_array))


# 5. Label High Sensors
print("\n5. LABEL HIGH SENSORS")

high_array = np.array([100.0, 50.0, 60.0])

print("Input :", high_array)
print("Output:", analyzer.label_high_sensors(high_array))


# 6. Format Sensor Readings
print("\n6. FORMAT SENSOR READINGS")

format_array = np.array([55.0, 66.0])

print("Input :", format_array)
print("Output:", analyzer.format_sensor_readings(format_array))