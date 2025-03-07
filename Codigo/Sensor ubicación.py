from machine import I2C, Pin
i2c = I2C(0, scl=Pin(6), sda=Pin(11), freq=100000)
devices = i2c.scan()

if devices:
    print("Direcciones I2C detectadas:")
    for device in devices:
        print(f"0x{device:02X}")
else:
    print("No se encontraron dispositivos I2C")