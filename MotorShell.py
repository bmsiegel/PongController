import time
from PongController import PongController

p = PongController(200, 19, 13, 6, 5, 26, 1)

print("""Welcome to The Pong Control Shell, this is where you can use the robot with a shell and test out different inputs, or just play around with the robot! Enter commands for a list of commands""")

while 1:
    command = input('Please Enter a Command: ')
  
    if command:
        command = command.lower()

        if command == 'spin':
            degrees = int(input('Enter degrees to spin: '))
            direction = input('Enter direction to spin (R or L): ')
            if direction.lower() == 'l':
                p.spin(-1*degrees)
            else:
                p.spin(degrees)

        elif command == 'shoot':
            speed = int(input('Enter shot speed: '))
            p.shoot(speed)
            print('Please reset motor arm before send another shoot command') 

        elif command == 'commands':
            print("""spin: Spin catapult\nshoot: Shoot catapult\n""")
