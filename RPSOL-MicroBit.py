from microbit import *
import random

rock = Image("00000:"
             "09990:"
             "09990:"
             "09990:"
             "00000")

paper = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999")

scissors = Image("90009:"
                 "09090:"
                 "00900:"
                 "99099:"
                 "99099")

lizzard = Image("90000:"
                "90000:"
                "90000:"
                "90000:"
                "99999")

spock = Image("99999:"
              "90000:"
              "99999:"
              "00009:"
              "99999")

RPSLS = [rock, paper, scissors, lizzard, spock]

while True:
    if button_a.is_pressed():
        display.show(random.choice(RPSLS))