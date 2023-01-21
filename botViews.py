import threading
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

n=1
drivers = []
for i in range(n):
    drivers.append(webdriver.Firefox(executable_path = '/opt/homebrew/bin/geckodriver'))

video_link = "https://youtu.be/yv_3XfbbThI"

def view_Video(duration, tab):
    drivers[tab].get(video_link)
    time.sleep(5)
    video = drivers[tab].find_element('id', 'movie_player')
    video.send_keys(Keys.SPACE)  # hits space
    video.click()  # mouse click
    time.sleep(1)
    video.send_keys(Keys.SPACE)  # hits space
    video.click()  # mouse click
    time.sleep(1)

    time.sleep(duration)
    drivers[tab].close()
    return

m = 10
duration = 200
tab = 0

threads = []

for i in range(m):
    for j in range(n):
        temp_thread = threading.Thread(target=view_Video, args=(duration, tab,))
        threads.append(temp_thread)
        temp_thread.start()
        tab += 1



