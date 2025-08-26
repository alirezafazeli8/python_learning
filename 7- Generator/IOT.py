import random
import time


def home_sensors():
    sensor_data = {
        "temp": random.randint(0, 40),
        "pressure": random.randint(20, 200),
        "wet": random.randint(0, 100),
    }

    time.sleep(0.1)
    yield sensor_data


def consumer(sensors):

    while True:
        sensor_data = []

        temp = 0
        pressure = 0
        wet = 0

        for i in range(10):
            sensor_data.append(next(sensors()))

        for item in sensor_data:
            temp += item["temp"]
            pressure += item["pressure"]
            wet += item["wet"]

        sensor_array_len = len(sensor_data)

        temp /= sensor_array_len
        pressure /= sensor_array_len
        wet /= sensor_array_len

        print(
            f"""
              
              Temp : {round(temp)}
              Pressure : {round(pressure)}
              Wet : {round(wet)}
              
              """
        )

        time.sleep(5)


consumer(home_sensors)
