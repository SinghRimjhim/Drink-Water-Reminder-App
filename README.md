#  Water Reminder Desktop App

A simple desktop hydration reminder app built in Python using `plyer` for notifications.

##  Features
- Sends a desktop notification every hour
- Optional reminder sound
- Lightweight `.exe` version (Windows)

##  How It Works

```python
import time
from plyer import notification
import winsound

for _ in range(5):
    time.sleep(3600)
    winsound.PlaySound("sound.wav", winsound.SND_FILENAME)
    notification.notify(
        title="Time to Drink Water!",
        message="Hey Rimjhim! Stay hydrated 💦",
        timeout=3
    )
```

##  Build with PyInstaller

python -m PyInstaller --onefile --noconsole --icon=water.ico code.py

##  Requirements

pip install plyer
(Use winsound only for Windows)

##  Built by Rimjhim Singh
