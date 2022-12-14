import machine
from machine import I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27
totalRows = 4
totalColumns = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400_000)
print(i2c.scan()) # 0x27
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

lcd.clear()
lcd.putstr("Hello\nWorld")


