#Prueba unitaria LED's
from machine import Pin
import time
import neopixel

PIN = 5
NUM_LEDS = 12
np = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)

# Configuración del sensor de llama
sensor_llama = Pin(7, Pin.IN)
UMBRAL_LLAMA = 0  # 0 indica detección de llama

def detectar_incendio():
    return sensor_llama.value() == UMBRAL_LLAMA

def encender_leds():
    for i in range(NUM_LEDS):
        np[i] = (255, 0, 0)  # Rojo (R, G, B)
    np.write()

def apagar_leds():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)  # Apagar LEDs
    np.write()

while True:
    if detectar_incendio():
        encender_leds()
        print("¡Incendio detectado!")
    else:
        apagar_leds()
    
    time.sleep(0.25)  # Esperar un cuarto de segundo antes de la siguiente lectura
