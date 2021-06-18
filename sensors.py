# import Adafruit_DHT

class DHT:

    # sensor = Adafruit_DHT.DHT11
    humidity = None
    temperature = None

    def __init__(self, gpio) -> None:
        self.gpio = gpio

    def sense(self):
        try:

            # self.humidity, self.temperature = Adafruit_DHT.read_retry(
            #     self.sensor, self.gpio)

            # TEST
            self.humidity, self.temperature = 1, 0

        except Exception as e:
            print('Exception : DHT-sense'+str(e))

    def get_temperature(self):
        if self.temperature is not None:
            return self.temperature
        else:
            return -1

    def get_humidity(self):
        if self.humidity is not None:
            return self.humidity
        else:
            return -1

    def show(self):
        print(self.gpio)
        print(self.humidity)
        print(self.temperature)
        # print(self.sensor)
