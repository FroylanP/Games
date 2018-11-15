from microbit import *
import random

Diamond = Image("00900:"
                "09090:"
                "90009:"
                "09090:"
                "00900")

SmallDiamond = Image("00000:"
                     "00900:"
                     "09090:"
                     "00900:"
                     "00000")

Skull = Image("09990:"
              "90909:"
              "99999:"
              "09990:"
              "09990")

Square = Image("99999:"
               "90009:"
               "90009:"
               "90009:"
               "99999")
Coinflip = [Skull, Square]

while True:
    sleep(1000)
    display.show(Diamond)
    sleep(1000)
    display.show(SmallDiamond)
    sleep(1000)
    display.show(Diamond)
    sleep(1000)
    display.show(SmallDiamond)

    if button_a.is_pressed():
        sleep(100)
        display.show(random.choice(Coinflip))


