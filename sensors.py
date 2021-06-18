import Adafruit_DHT
import RPi.GPIO as GPIO


class DHT:
    sensor = Adafruit_DHT.DHT11
    humidity = None
    temperature = None

    def __init__(self, gpio_pin) -> None:
        self.gpio = gpio_pin

    def sense(self):
        try:

            self.humidity, self.temperature = Adafruit_DHT.read_retry(
                self.sensor, self.gpio)

            # TEST
            # self.humidity, self.temperature = 1, 0

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


class LED:
    led_status = None

    def __init__(self, gpio_pin) -> None:
        self.gpio = gpio_pin
        self.led_status = False

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio, GPIO.OUT)

    def on(self) -> bool:
        if not self.led_status:
            GPIO.output(self.gpio, GPIO.HIGH)
            self.led_status = True
        return self.led_status

    def off(self) -> bool:
        if self.led_status:
            GPIO.output(self.gpio, GPIO.LOW)
            self.led_status = False
        return self.led_status

    def status(self) -> dict:
        led_status = dict()
        led_status['status'] = 'ON' if self.led_status else 'OFF'
        led_status['pin'] = self.gpio

        return led_status
