from machine import Pin, ADC, I2C
import machine
import time
import neopixel

# Configuración del sensor MQ-2
detector_gas = ADC(Pin(13))
detector_gas.atten(ADC.ATTN_11DB)  # Ajuste para 3.3V

# Sensor de llama
sensor_llama = Pin(10, Pin.IN)

# LM75A - Sensor de temperatura I2C
I2C_SCL = Pin(6)
I2C_SDA = Pin(11)
i2c = I2C(0, scl=I2C_SCL, sda=I2C_SDA, freq=100000)
LM75A_ADDR = 0x4F

# Buzzer
buzzer = Pin(9, Pin.OUT)

# LEDs Neopixel
NUM_LEDS = 12
np = neopixel.NeoPixel(Pin(2), NUM_LEDS)

def leer_temperatura():
    temp_data = i2c.readfrom_mem(LM75A_ADDR, 0x00, 2)
    temp = (temp_data[0] << 8 | temp_data[1]) >> 7
    return temp * 0.5

def leer_gas():
    return detector_gas.read()

def encender_leds(color):
    for i in range(NUM_LEDS):
        np[i] = color
    np.write()

def apagar_leds():
    encender_leds((0, 0, 0))

def alerta_incendio():
    encender_leds((255, 0, 0))
    buzzer.value(1)
    time.sleep(0.5)
    buzzer.value(0)

while True:
    gas = leer_gas()
    llama = sensor_llama.value()
    temperatura = leer_temperatura()

    print(f"Gas: {gas}, Llama: {llama}, Temp: {temperatura:.2f}°C")

    if gas > 2000 or llama == 0 or temperatura > 50:
        alerta_incendio()
    elif gas > 1500 or temperatura > 40:
        encender_leds((255, 165, 0))  # Naranja para advertencia
    else:
        encender_leds((0, 255, 0))  # Verde para seguro

    time.sleep(0.5)
