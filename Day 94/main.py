import pyautogui as bot
from PIL import Image

URL = 'https://elgoog.im/dinosaur-game/'
BOTTOM = 428, 778
DINO = 158, 778

bot.sleep(2)
bot.click(876, 58, duration=0.8)

bot.write(URL, interval=0.01)
bot.press('enter')
bot.sleep(2)

bot.press('space')
bot.sleep(2)

dino_color = bot.pixel(DINO[0], DINO[1])
bot.moveTo(BOTTOM)

counter = 0
while True:
    bottom = bot.pixelMatchesColor(BOTTOM[0], BOTTOM[1], dino_color, tolerance=10)
    if bottom:
        bot.press('space')

    counter += 1

    if counter > 500:
        print("Check")
        counter = 0
        try:
            bot.locateOnScreen('dino.png')
            break
        except bot.ImageNotFoundException:
            pass
