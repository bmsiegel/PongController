from MotorController import MotorController
from ArduinoStepper import ArduinoStepper
import time

class PongController:

    def __init__(self, steps, A1, A0, B1, B0, CC, sleepPin):
        self.m = MotorController(sleepPin)
        self.a = ArduinoStepper(steps, A1, A0, B1, B0, CC)
        time.sleep(1)
        self.m.enableMotor()
        self.a.setSpeed(25)
        time.sleep(1)

    def spinSteps(self, steps):
        self.a.step(steps)

    def spin(self, degrees):
        self.a.step(int(degrees/1.8))

    def shoot(self, speed):
        self.m.shoot(speed)

