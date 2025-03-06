#Prueba unitaria sensor de humo
from machine import Pin, ADC
import time

sensor_humo = ADC(Pin())  # Sensor de humo (ejemplo: MQ-2)
sensor_humo.atten(ADC.ATTN_11DB)  # Medir hasta 3.3V

UMBRAL_HUMO = 400  # Valor de ADC para indicar alta presencia de humo

def leer_sensor(sensor):
    return sensor.read()

def detectar_humo():
    humo = leer_sensor(sensor_humo)
    print(f"Nivel de humo: {humo}")
    return humo > UMBRAL_HUMO

while True:
    if detectar_humo():
        print("¡Humo detectado!")
    else:
        print("Niveles normales de humo.")
    
    time.sleep(0.25)  # Esperar un cuarto de segundo antes de la siguiente lectura
