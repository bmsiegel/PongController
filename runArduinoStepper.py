from ArduinoStepper import ArduinoStepper

a = ArduinoStepper(200, 19, 13, 6, 5, 26)

a.setSpeed(40)
while 1:
    a.step(int(input()))

