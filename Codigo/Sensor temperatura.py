#Prueba unitaria sensor de temperatura
from machine import Pin, ADC
import time

sensor_temp = ADC(Pin(10))  # Sensor de temperatura (ejemplo: termistor)
sensor_temp.atten(ADC.ATTN_11DB)  # Medir hasta 3.3V

# Umbral para detección de temperatura alta (ajustar según sensor)
UMBRAL_TEMP = 3000  

def leer_sensor(sensor):
    """Lee un sensor analógico y devuelve un valor entre 0 y 4095"""
    return sensor.read()

while True:
    temp = leer_sensor(sensor_temp)
    print(f"Temperatura: {temp}")

    if temp > UMBRAL_TEMP:
        print("¡Temperatura alta detectada!")

    time.sleep(0.25)  # Esperar un cuarto de segundo antes de la siguiente lectura
