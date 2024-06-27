import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time
import os
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 600))
display.start()

chromedriver_autoinstaller.install()
# 创建一个 Chrome 浏览器实例
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920x1080')
options.add_experimental_option('detach', True)  # 不自动关闭浏览器
browser = webdriver.Chrome(options=options)

# 打开网页
url = 'https://vip.taoqitu.pro/index.html'  # 替换成你要签到的网站地址
browser.get(url)
time.sleep(5)
now = datetime.datetime.now()
timestamp = now.strftime('%Y%m%d_%H%M%S')
filename = timestamp + '.png'
browser.save_screenshot(filename)

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")
browser.find_element(By.ID, 'regusername').send_keys(username)
browser.find_element(By.ID, 'regpassword').send_keys(password)
browser.find_element(By.CLASS_NAME, 'loginbutton').click()
time.sleep(5)

now = datetime.datetime.now()
timestamp = now.strftime('%Y%m%d_%H%M%S')
filename = timestamp + '.png'
browser.save_screenshot(filename)

# if browser.find_element(By.CLASS_NAME, 'gonggao_tan_button')!=[]:
#     browser.find_element(By.CLASS_NAME, 'gonggao_tan_button').click()
#
# if browser.find_element(By.CLASS_NAME, 'qiandao')!=[]:
#     browser.find_element(By.CLASS_NAME, 'qiandao').click()
# time.sleep(5)
#
# if browser.find_element(By.CLASS_NAME, 'invite_get_amount')!=[]:
#     browser.find_element(By.CLASS_NAME, 'invite_get_amount').click()
# now = datetime.datetime.now()
# timestamp = now.strftime('%Y%m%d_%H%M%S')
# filename = timestamp + '.png'
# browser.save_screenshot(filename)
browser.quit()
display.stop()
