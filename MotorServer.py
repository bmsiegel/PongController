from flask import Flask, request
from PongController import PongController

app = Flask(__name__)

p = PongController(200, 19, 13, 6, 5, 26, 1)

@app.route('/spin')
def spin():
    steps = int(request.args.get('steps'))
    p.spinSteps(steps)
    return 'Spun {} steps'.format(steps)

@app.route('/shoot')
def shoot():
    speed = int(request.args.get('rpm'))
    p.shoot(speed)
    return 'Shot with speed {}'.format(speed)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6625)
