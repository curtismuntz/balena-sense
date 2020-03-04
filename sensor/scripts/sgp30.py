""" Example for using the SGP30 with CircuitPython and the Adafruit library"""

import time
import board
import busio
import adafruit_sgp30

class SGP30():
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
        # Create library object on our I2C port
        self.sensor = adafruit_sgp30.Adafruit_SGP30(i2c)
        self.sensor.iaq_init()
        self.sensor.set_iaq_baseline(0x8973, 0x8aae)
        print("SGP30 serial #", self.get_id())

    def get_id(self):
        return [hex(i) for i in self.sensor.serial]

    def get_readings(self, sensor):
        eco2 = self.sensor.eCO2
        tvoc = self.sensor.TVOC
        return [
            {
                'measurement': 'balena-sense',
                'fields': {
                    'eCO2': float(eco2),
                    'TVOC': float(tvoc)
                }
            }
        ]
