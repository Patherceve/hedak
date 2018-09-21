from Servo import *
import time

art1 = Servo(0)
art2 = Servo(1)
art3 = Servo(2)
art4 = Servo(3)
art5 = Servo(4)
grip = Servo(5)

art1.setup()
art2.setup()
art3.setup()
art4.setup()
art5.setup()
grip.setup()

def loop():
    while True:
        art3.setAngle(0)
        time.sleep(1)
        art3.setAngle(180)
        time.sleep(1)
        art3.setAngle(0)
        time.sleep(1)
        art3.setAngle(180)
        time.sleep(1)
            
if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        art1.setup()
        art2.setup()
        art3.setup()
        art4.setup()
        art5.setup()
        grip.setup()
        