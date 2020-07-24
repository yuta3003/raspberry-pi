import RPi.GPIO as GPIO
import tkinter as tk

GPIO.setmode(GPIO.BOARD)

LED = 11
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

def func():
    # 入力値を反転して出力
    GPIO.output(LED, not GPIO.input(LED))

root = tk.Tk()

label = tk.Label(root, text='press button')
label.pack()

button = tk.Button(root, text='LED', command=func)
button.pack()

root.mainloop()

GPIO.cleanup()