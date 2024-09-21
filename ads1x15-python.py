# sudo pip install adafruit-circuitpython-ads1x15
# sudo pip install board
# sudo pip install adafruit-blinka

"""
El ADS1115 tiene diferentes configuraciones de ganancia (PGA - Programmable Gain Amplifier) 
que determinan el rango máximo de entrada. 
Choose a gain of 1 for reading voltages from 0 to 4.09V.
Or pick a different gain to change the range of voltages that are read:
  - 2/3 = +/-6.144V
  -   1 = +/-4.096V
  -   2 = +/-2.048V
  -   4 = +/-1.024V
  -   8 = +/-0.512V
  -  16 = +/-0.256V

Para medir voltajes de hasta 5V, debes establecer la ganancia en 2/3, que te permitirá medir hasta ±6.144V. 
Ten en cuenta que, aunque esta ganancia permite un rango más amplio, reduce la resolución efectiva del ADC
 para valores más pequeños.

ads.gain = 2/3 establece la ganancia para permitir la medición de voltajes hasta ±6.144V. 
Esto asegura que puedas medir valores hasta 5V.

Precisión: Ajustar la ganancia a 2/3 disminuirá la precisión en voltajes más bajos. 
Si solo necesitas medir temperaturas comunes (por ejemplo, de 0 a 100°C), 
puedes usar una ganancia menor, como 1 (±4.096V).

Note you can change the I2C address from its default (0x48), and/or the I2C

"""

import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)
ads.gain = 1

# Create single-ended input on channel 0, 1, 2, and 3
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

# Print title for columns
print("{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}\t{:>5}".format(
    'Raw 0', 'V 0', 'Raw 1', 'V 1', 'Raw 2', 'V 2', 'Raw 3', 'V 3'))

while True:
    # Print raw and voltage readings for all channels
    print("{:>5}\t{:>5.3f}\t{:>5}\t{:>5.3f}\t{:>5}\t{:>5.3f}\t{:>5}\t{:>5.3f}".format(
        chan0.value, chan0.voltage, 
        chan1.value, chan1.voltage,
        chan2.value, chan2.voltage,
        chan3.value, chan3.voltage))
    time.sleep(0.5)

