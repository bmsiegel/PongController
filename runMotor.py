from MotorController import * 

GPIO.setmode(GPIO.BCM)

m = MotorController()

m.enableMotor()
m.readCtrl()
m.checkStatus()
m.clearStatus()
time.sleep(1)
m.checkStatus()

while 1:
    m.shoot(int(input('Enter speed:\t')))
