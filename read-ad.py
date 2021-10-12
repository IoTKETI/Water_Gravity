import board
import busio
import time
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads,ADS.P0)

volt = chan.voltage+0.6
if(volt < 2.5):
  y = 3000.0
else:
  y = -1120.4*pow(volt,2) + 5742.3 *volt - 4353.8

print(round(y,3))

