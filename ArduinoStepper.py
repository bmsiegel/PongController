import time
import RPi.GPIO as GPIO

class ArduinoStepper:

    def __init__(self, steps, A1, A0, B1, B0, CC):
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(A1, GPIO.OUT)
        GPIO.setup(A0, GPIO.OUT)
        GPIO.setup(B1, GPIO.OUT)
        GPIO.setup(B0, GPIO.OUT)
        GPIO.setup(CC, GPIO.OUT)

        GPIO.output(A1, 0)
        GPIO.output(A0, 0)
        GPIO.output(B1, 0)
        GPIO.output(B0, 0)
        GPIO.output(CC, 1)

        self.stepNum = 0
        self.stepCount = steps
        self.stepDelay = 0
        self.lastStepTime = 0

        self.A1 = A1
        self.A0 = A0
        self.B1 = B1
        self.B0 = B0
        self.CC = CC

    def __del__(self):
        GPIO.cleanup()


    def setSpeed(self, rpm):
        self.stepDelay = 60 * 1000 * 1000 / self.stepCount / rpm

    def step(self, stepsToDo):
        stepsLeft = abs(stepsToDo)

        direction = 1 if stepsToDo > 0 else 0

        while stepsLeft > 0:
            now = time.time() * 1000 * 1000
            if now - self.lastStepTime >= self.stepDelay:
                self.lastStepTime = now
                if direction is 1:
                    self.stepNum += 1
                    if self.stepNum == self.stepCount:
                        self.stepNum = 0
                else:
                    if self.stepNum == 0:
                        self.stepNum = self.stepCount
                    self.stepNum -= 1
                stepsLeft -= 1
                self.doStep(self.stepNum % 4)

    def doStep(self, stepIndex):
        if stepIndex == 0:
            GPIO.output(self.A1, 1)
            GPIO.output(self.A0, 0)
            GPIO.output(self.B1, 1)
            GPIO.output(self.B0, 0)
        elif stepIndex == 1:
            GPIO.output(self.A1, 0)
            GPIO.output(self.A0, 1)
            GPIO.output(self.B1, 1)
            GPIO.output(self.B0, 0)
        elif stepIndex == 2:
            GPIO.output(self.A1, 0)
            GPIO.output(self.A0, 1)
            GPIO.output(self.B1, 0)
            GPIO.output(self.B0, 1)
        elif stepIndex == 3:
            GPIO.output(self.A1, 1)
            GPIO.output(self.A0, 0)
            GPIO.output(self.B1, 0)
            GPIO.output(self.B0, 1)
