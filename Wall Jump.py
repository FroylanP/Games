from microbit import *
import random

display.scroll("Get Ready...")

DELAY = 20
FRAMES_PER_WALL_SHIFT = 20
FRAMES_PER_NEW_WALL = 100
FRAMES_PER_SCORE = 50

y = 50
speed = 0
score = 0
frame = 0

def make_pipe():
  i = Image("00003:00003:00003:00003:00003")
  gap = random.randint(0,3)
  i.set_pixel(4, gap, 0)
  i.set_pixel(4, gap+1, 0)
  return i

i = make_pipe()

while True:
  frame += 1
  display.show(i)

  if button_a.was_pressed():
    speed = -8
  if button_b.was_pressed():
    display.scroll("Score:" + str(score))

  speed += 1
  if speed > 2:
    speed = 2

  y += speed
  if y > 99:
    y = 99
  if y < 0:
    y = 0

  led_y = int(y / 20)
  display.set_pixel(1, led_y, 9)

  if i.get_pixel(1, led_y) != 0:
    display.show(Image.SAD)
    sleep(500)
    display.scroll("Score: " + str(score))
    break

  if(frame % FRAMES_PER_WALL_SHIFT == 0):
    i = i.shift_left(1)

  if(frame % FRAMES_PER_NEW_WALL == 0):
    i = make_pipe()

  if(frame % FRAMES_PER_SCORE == 0):
    score += 1

  sleep(20)