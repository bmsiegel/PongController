from ArduinoStepper import ArduinoStepper

a = ArduinoStepper(200, 19, 13, 6, 5, 26)

a.setSpeed(75)
while 1:
    input()
    a.step(int(input()))

