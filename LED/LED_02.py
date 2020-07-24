import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# デューティー比のリストを作成
dc = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 20, 30, 50, 70, 100]

LED = 11
# 初期値設定
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

p = GPIO.PWN(LED, 100)
p.start(0)

try:
    while True:
        for val in dc:
            p.ChangeDutyCycle(val)
            time.sleep(0.1)
        dc.reverse()
        time.sleep(0.1)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()