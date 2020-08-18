import spidev
import time

class MotorController:
    
    def __init__(self):
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 500000
        self.spi.mode = 0b00
        self.spi.cshigh = True
        self.spi.lsbfirst = False
        time.sleep(1)
        self.ctrl = [0x0C, 0x10]
        print(self.ctrl)

    def __del__(self):
        self.spi.close()

    def enableMotor(self):
        self.spi.xfer2([0x4D, 0x10])
        self.ctrl = [0x0C, 0x01]
        self.sendCtrl()

    def clearStatus(self):
        self.spi.xfer2([0x70, 0x00])

    def checkStatus(self):
        self.print_bytes(self.spi.xfer2([0xF0, 0x00]))
        
    def readCtrl(self):
        self.print_bytes(self.spi.xfer2([0x80, 0x00]))

    def step(self, steps, stepTime):
        stepsToGo = abs(steps)
        while stepsToGo != 0:
            self.ctrl = [0x0C, 0x05] if steps > 0 else [0x0C, 0x07]
            self.sendCtrl()
            self.ctrl = [self.ctrl[0], self.ctrl[1] & 0xFB]
            stepsToGo -= 1
            time.sleep(stepTime)

    def sendCtrl(self):
        tempCtrl = self.ctrl[:]
        self.spi.xfer2(self.ctrl)
        self.ctrl = tempCtrl
    
    def print_bytes(self, val):
        for b in val:
            print(hex(b))

    def shoot(self, speed):
        if speed <= 1000:
            stepDelay = 60 / 200 / speed
            print(stepDelay)
            self.step(75, stepDelay)
