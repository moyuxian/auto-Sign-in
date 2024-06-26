from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 创建一个 Chrome 浏览器实例
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  # 不自动关闭浏览器
browser = webdriver.Chrome(options=options)

# 打开网页
url = ''  # 替换成你要签到的网站地址
browser.get(url)

username = ''
password = ''
browser.find_element(By.ID, 'regusername').send_keys(username)
browser.find_element(By.ID, 'regpassword').send_keys(password)
browser.find_element(By.CLASS_NAME, 'loginbutton').click()
time.sleep(5)
browser.find_element(By.CLASS_NAME, 'gonggao_tan_button').click()
browser.find_element(By.CLASS_NAME, 'qiandao').click()
time.sleep(5)
browser.find_element(By.CLASS_NAME, 'invite_get_amount').click()

browser.quit()
