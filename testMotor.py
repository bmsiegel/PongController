from MotorController import MotorController
import time

m = MotorController(1)
m.enableMotor()

while 1:
    m.testShoot(int(input('Number of Steps:')), int(input('Speed:')))
    time.sleep(1)
    m.sleep()
    input()
    m.wake()
