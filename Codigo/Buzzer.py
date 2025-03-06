#Prueba unitaria buzzer
from machine import Pin
import time

# Configurar el buzzer
buzzer = Pin(3, Pin.OUT)
buzzer.value(0)  # Inicialmente apagado

def activar_alarma():
    buzzer.value(1)  # Encender el buzzer

def desactivar_alarma():
    buzzer.value(0)  # Apagar el buzzer

while True:
    activar_alarma()
    time.sleep(1)  # Sonar por 1 segundo
    desactivar_alarma()
    time.sleep(1)  # Pausa por 1 segundo
