import time
import winsound
from plyer import notification

timeHour = 1
for _ in range(5):
    time.sleep(3600 * timeHour) 
    winsound.PlaySound("sound.wav", winsound.SND_FILENAME)
    notification.notify(title = "Time to Drink Water!", 
                        message = "Hey Rimjhim!\nYour body and brain need a little boost — take a moment to drink some water 💦",
                        timeout = 3)
