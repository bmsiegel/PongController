import spidev
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 500000
spi.mode = 0b00
spi.cshigh = True
spi.lsbfirst = False
time.sleep(1)
ctrl = 0xC10

def step():
    spi.xfer2([0x0C, 0x05])

def print_bytes(l):
    for i in l:
        print(hex(i))

spi.xfer2([0x4D, 0x10])
spi.xfer2([0x70, 0x00])

#Enable Motor
spi.xfer2([0x0C, 0x01])
print_bytes(spi.xfer2([0x80, 0x00]))

time.sleep(1)

#Check Status
print_bytes(spi.xfer2([0xF0, 0x00]))
print_bytes(spi.xfer2([0x80, 0x00]))
now = time.time()
for i in range(101000):
    step()
    time.sleep(0.001)
print(time.time() - now)
