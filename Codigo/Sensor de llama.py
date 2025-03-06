#Prueba unitaria sensor de llama
from machine import Pin
import time
import neopixel

sensor_llama = Pin(7, Pin.IN)  

buzzer = Pin(3, Pin.OUT)  # Buzzer
buzzer.value(0)  # Inicialmente apagado

PIN = 5
NUM_LEDS = 12  # LED indicador de incendio
np = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)

# Umbral para detección de incendio
UMBRAL_LLAMA = 0  

def detectar_incendio():
    llama = sensor_llama.value() - 1
    print(f"Llama: {llama}")
    return llama == UMBRAL_LLAMA

def activar_alarma():
    for i in range(NUM_LEDS):
        np[i] = (255, 0, 0)  # Rojo
    np.write()
    buzzer.value(1)

def desactivar_alarma():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)  # Apagar LEDs
    np.write()
    buzzer.value(0)

while True:
    if detectar_incendio():
        print("¡Incendio detectado!")
        activar_alarma()
    else:
        desactivar_alarma()
    
    time.sleep(0.25)  # Esperar antes de la siguiente lectura
