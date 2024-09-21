
"""
El ADS1115 tiene diferentes configuraciones de ganancia (PGA - Programmable Gain Amplifier) que determinan el rango máximo de entrada. 
Aquí están las configuraciones más comunes:

1 = ±4.096V (default)
2/3 = ±6.144V
2 = ±2.048V
4 = ±1.024V
8 = ±0.512V
16 = ±0.256V

Para medir voltajes de hasta 5V, debes establecer la ganancia en 2/3, que te permitirá medir hasta ±6.144V. Ten en cuenta que, aunque esta ganancia permite un rango más amplio, reduce la resolución efectiva del ADC para valores más pequeños.

ads.gain = 2/3 establece la ganancia para permitir la medición de voltajes hasta ±6.144V. Esto asegura que puedas medir valores hasta 5V.

Precisión: Ajustar la ganancia a 2/3 disminuirá la precisión en voltajes más bajos. Si solo necesitas medir temperaturas comunes (por ejemplo, de 0 a 100°C), 
puedes usar una ganancia menor, como 1 (±4.096V).

Alimentación: Asegúrate de que el LM35 esté alimentado correctamente con 5V

"""

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Configurar la comunicación I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Crear el objeto ADS usando I2C y ajustar la ganancia para medir hasta 6.144V
ads = ADS.ADS1115(i2c)
ads.gain = 2/3  # Configurar ganancia para medir voltajes entre 0-5V (rango completo ±6.144V)

# Crear un canal de entrada analógica (conectado al pin A0 del ADS1115)
chan = AnalogIn(ads, ADS.P0)

# Función para convertir la lectura del LM35 a grados Celsius
def lm35_to_celsius(voltage):
    # El LM35 proporciona 10mV por cada grado Celsius.
    # Multiplicamos el voltaje por 100 para obtener la temperatura en grados Celsius.
    return voltage * 100

try:
    while True:
        # Leer el voltaje en el canal A0
        voltage = chan.voltage
        
        # Convertir el voltaje a temperatura
        temperature = lm35_to_celsius(voltage)
        
        # Mostrar la temperatura
        print(f"Temperatura: {temperature:.2f}°C (Voltaje: {voltage:.4f} V)")
        
        # Esperar 1 segundo antes de la siguiente lectura
        time.sleep(1)

except KeyboardInterrupt:
    print("Lectura interrumpida por el usuario.")
