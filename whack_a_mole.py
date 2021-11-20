"""
File: whack_a_mole.py
Name: Chia-Yu Chen
---------------------------
This program plays a game called "whack a mole" in which players 
clicking the popping moles on screen to gain scores 
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLabel
from campy.graphics.gimage import GImage
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause
import random

# Constants control the diameter of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Constant controls the pause time of the animation
DELAY = 700

# Global variables
score = 0
score_label = GLabel("Score: " + str(score))
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title="Whack a Mole")


def main():
    score_label.font = "-30"
    window.add(score_label, 10, score_label.height + 10)
    onmouseclicked(remove_mole)

    # randomly show the mole
    while True:
        img = GImage("mole.png")
        x_random = random.randint(0, window.width - img.width)
        y_random = random.randint(0, window.height - img.height)
        window.add(img, x_random, y_random)
        pause(DELAY)  # pause for a sec, otherwise will be flashing


def remove_mole(event):
    global score
    obj = window.get_object_at(event.x, event.y)

    # if hit a mole, score a point
    if obj is not None and obj is not score_label:
        window.remove(obj)
        score += 1
        score_label.text = "Score: " + str(score)


if __name__ == "__main__":
    main()
