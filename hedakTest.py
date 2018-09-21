from Servo import *
import time

global fingers, pouce, index, majeur, annulaire, auriculaire

pouce = Servo(1)
index = Servo(2)
majeur = Servo(3)
annulaire = Servo(4)
auriculaire = Servo(5)
fingers = [pouce, index, majeur, annulaire, auriculaire]

def setup():
    for x in fingers:
        x.setup()

def loop():
    while True:
        for x in fingers:
            for y in range(0,181):
                x.setAngle(y)
                time.sleep(0.001)
        fingers.reverse()        
        for x in fingers:
            for y in range(180, -1, -1):
                x.setAngle(y)
                time.sleep(0.001)
        fingers.reverse()
            
if __name__ == '__main__':
    setup()
    try:
        loop()
    finally:
        for x in fingers:
            x.setAngle(0)
            time.sleep(0.5)
        time.sleep(1)
        setup()
        
