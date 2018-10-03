from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import subprocess
import operator


music_driver = webdriver.Chrome()
music_driver.get('https://www.youtube.com/watch?v=xeEKETt9MTU')

time.sleep(5)

volume_down = """
return (function(v) {
document.getElementsByTagName('video')[0].volume=v;
})(arguments[0]);
"""

for i in range(0,10):
    vol = 1-i/10
    time.sleep(.8)
    music_driver.execute_script(volume_down,vol)

time.sleep(5)
music_driver.quit()
