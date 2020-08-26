#coding:utf-8

import RPi.GPIO as GPIO

import tkinter as tk

GPIO.setmode(GPIO.BOARD)

SW = 15
LED = 11

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(SW, GPIO.IN)

root = tk.Tk()

c = tk.Canvas(root, width=200, height=200)
c.pack()

cc = c.create_oval(50, 50, 150, 150, fill='')


def check_SW(channel):
    key_in = GPIO.input(channel)
    if key_in==0:
        GPIO.output(LED, GPIO.HIGH)
        c.itemconfig(cc, fill='red')
    else:
        GPIO.output(LED, GPIO.LOW)
        c.itemconfig(cc, fill='')

GPIO.add_event_detect(SW, GPIO.BOTH, callback=check_SW)

root.mainloop()

GPIO.cleanup()
