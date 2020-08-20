from MotorController import * 

GPIO.setmode(GPIO.BCM)

m = MotorController(1)

m.enableMotor()
m.readCtrl()
m.checkStatus()
m.clearStatus()
time.sleep(1)
m.checkStatus()

while 1:
    m.shoot(int(input('Enter speed:\t')))
    time.sleep(1)
    m.sleep()
    input('Press Enter to Continue:')
    m.wake()
