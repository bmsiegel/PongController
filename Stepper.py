import spidev
import RPi.GPIO as GPIO
import math

class DRV8711SPI:

    def __init__(self):
        self.spi = spidev.SpiDev()

    def setChipSelectPin(self, pin):
        self.csPin = pin

    def readReg(self, address):
        self.selectChip()
        dataOut = self.transfer((0x8 | (address & 0b111)) << 12)
        print(dataOut)
        self.deselectChip()
        return dataOut & 0xFF
    
    def writeReg(self, address, value):
        self.selectChip()
        self.transfer(((address & 0b111) << 12) | (value & 0xFFF))
        self.deselectChip()

    def transfer(self, value):
        a = value.to_bytes(2, 'big')
        to_send = [a[0], a[1]]
        a = self.spi.xfer(to_send)
        return a

    def selectChip(self):
        self.spi.open(0, 0)
        self.spi.mode = 0b00
        self.spi.max_speed_hz = 500000

    def deselectChip(self):
        self.spi.close()

class HighPowerStepperDriver:

    def __init__(self):
        self.ctrl = 0xC10
        self.torque = 0x1FF
        self.off = 0x030
        self.blank = 0x080
        self.decay = 0x110
        self.stall = 0x040
        self.drive = 0xA59
        GPIO.setmode(GPIO.BCM)
        self.driver = DRV8711SPI()

    def __del__(self):
        GPIO.cleanup()

    def setChipSelectPin(self, pin):
        self.driver.setChipSelectPin(pin)

    def resetSettings(self):
        self.ctrl = 0xC10
        self.torque = 0x1FF
        self.off = 0x030
        self.blank = 0x080
        self.decay = 0x110
        self.stall = 0x040
        self.drive = 0xA59
        self.applySettings()

    def applySettings(self):
        self.writeTorque()
        self.writeOff()
        self.writeBlank()
        self.writeDecay()
        self.writeDrive()
        self.writeStall()
        self.writeCtrl()

    def enableDriver(self):
        self.ctrl |= (1 << 0)
        self.writeCtrl()

    def disableDriver(self):
        self.ctrl &= ~(1 << 0)
        self.writeCtrl()

    def setDirection(self, value):
        if value:
            self.ctrl |= (1 << 1)
        else:
            self.ctrl &= ~(1 << 1)
        self.writeCtrl()

    def getDirection(self):
        return self.ctrl >> 1 & 1

    def step(self):
        driver.writeReg(0x00, self.ctrl | (1 << 2))

    def setStepMode(self, mode):
        sm = 0b0010
        if mode == 1: 
            sm = 0b0000
        elif mode == 2:
            sm = 0b0001
        elif mode == 4:
            sm = 0b0010
        elif mode == 8:
            sm = 0b0011
        elif mode == 16:
            sm = 0b0100
        elif mode == 32:
            sm = 0b0101
        elif mode == 64:
            sm = 0b0110
        elif mode == 128:
            sm = 0b0111
        elif mode == 256:
            sm = 0b1000
        
        self.ctrl = (self.ctrl & 0b111110000111) | (sm << 3)
        self.writeCtrl()

    def setCurrentMilliamps(self, current):
        if current > 8000:
            current = 8000

        isgainBits = 0b11
        torqueBits = int((768 * current) / 6875)

        while torqueBits > 0xFF:
            isgainBits -= 1
            torqueBits >>= 1

        self.ctrl = (self.ctrl & 0b110011111111) | (isgainBits << 8)
        self.writeCtrl()
        self.torque = (self.torque & 0b111100000000) | torqueBits
        self.writeTorque()

    def setDecayMode(self, mode):
        self.decay = (self.decay & 0b000111111111) | ((mode & 0b111) << 8)
        self.writeDecay()

    def readStatus(self):
        return self.driver.readReg(0x07)

    def clearStatus(self):
        self.driver.writeReg(0x07, 0)

    def readFaults(self):
        return self.readStatus() & 0b00111111

    def clearFaults(self):
        self.driver.writeReg(0x07, ~0b00111111)

    def writeCtrl(self):
        self.driver.writeReg(0x00, self.ctrl)

    def writeTorque(self):
        self.driver.writeReg(0x01, self.torque)

    def writeOff(self):
        self.driver.writeReg(0x02, self.off)
    
    def writeBlank(self):
        self.driver.writeReg(0x03, self.blank)

    def writeDecay(self):
        self.driver.writeReg(0x04, self.decay)

    def writeStall(self):
        self.driver.writeReg(0x05, self.stall)

    def writeDrive(self):
        self.driver.writeReg(0x06, self.drive)
