from Stepper import *
import time


sd = HighPowerStepperDriver()
csPin = 8
DirPin = 7
StepPin = 1

def setup():
    sd.setChipSelectPin(8)

    GPIO.setup(DirPin, GPIO.OUT)
    GPIO.setup(StepPin, GPIO.OUT)
    GPIO.output(DirPin, 0)
    GPIO.output(StepPin, 0)

    time.sleep(1)

    sd.resetSettings()
    sd.clearStatus()
    
    #sd.setDecayMode(0b101)

    #sd.setCurrentMilliamps(1000)

    #sd.setStepMode(32)

    sd.enableDriver()

if __name__ == '__main__':
    setup()
    time.sleep(0.000001)
    GPIO.output(DirPin, 1)
    time.sleep(0.000001)

    for c in range(0, 1000):
        GPIO.output(StepPin, 1)
        time.sleep(0.000003)
        GPIO.output(StepPin, 0)
        time.sleep(0.000003)
        rpm = 1
        time.sleep((60 * 1000 * 1000 / 200 / rpm)/1000000)
