#Codigo final
from machine import Pin, ADC, PWM
import machine
import time
import neopixel

sensor_humo = ADC(Pin(34))  # Pin analógico para el sensor de humo MQ-2
sensor_humo.atten(ADC.ATTN_11DB)  # Rango de 0 a 3.3V

sensor_temp = ADC(Pin(35))  # Pin analógico para el sensor de temperatura (termistor)
sensor_temp.atten(ADC.ATTN_11DB)

sensor_llama = Pin(7, Pin.IN)  # Sensor de llama (entrada digital)

# Configurar actuadores (salida de información)
buzzer = PWM(Pin(3), freq=1000, duty_u16=0)  # Buzzer con PWM
PIN_LEDS = 5
NUM_LEDS = 12
np = neopixel.NeoPixel(Pin(PIN_LEDS), NUM_LEDS)

# Umbrales de detección (ajustar según pruebas)
UMBRAL_HUMO = 1000  # Valor del ADC para indicar alta presencia de humo
UMBRAL_TEMP = 2000  # Valor del ADC para indicar temperatura alta
UMBRAL_LLAMA = 0  # En la mayoría de los sensores de llama, 0 indica detección

def leer_sensor(sensor):
    """Lee un sensor analógico y devuelve un valor entre 0 y 4095"""
    return sensor.read()

def detectar_incendio():
    """Verifica si hay condiciones de incendio"""
    humo = leer_sensor(sensor_humo)
    temp = leer_sensor(sensor_temp)
    llama = sensor_llama.value()

    print(f"Humo: {humo}, Temperatura: {temp}, Llama: {llama}")

    if humo > UMBRAL_HUMO or temp > UMBRAL_TEMP or llama == UMBRAL_LLAMA:
        return True  # Se detecta incendio
    return False  # No hay incendio

def encender_leds():
    """Enciende los LEDs en color rojo"""
    for i in range(NUM_LEDS):
        np[i] = (255, 0, 0)  # Rojo (R, G, B)
    np.write()

def apagar_leds():
    """Apaga todos los LEDs"""
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()

def activar_buzzer():
    """Activa el buzzer con un sonido intermitente"""
    for _ in range(5):
        buzzer.duty_u16(30000)  # Sonido fuerte
        time.sleep(0.2)
        buzzer.duty_u16(0)  # Silencio
        time.sleep(0.2)

def activar_alarma():
    """Activa LED y buzzer en caso de incendio"""
    encender_leds()
    activar_buzzer()

def desactivar_alarma():
    """Apaga LED y buzzer"""
    apagar_leds()
    buzzer.duty_u16(0)

# Loop principal
while True:
    if detectar_incendio():
        print("¡Incendio detectado!")
        activar_alarma()
    else:
        desactivar_alarma()

    time.sleep(1)  # Esperar antes de la siguiente lectura
