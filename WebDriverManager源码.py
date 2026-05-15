# WebDriverManager使用手记(小白简单上手版本)   项目仅供测试使用，请勿商用
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 创建 Service 对象，自动下载并指定 chromedriver 路径
service = Service(ChromeDriverManager().install())

# 启动浏览器
driver = webdriver.Chrome(service=service)

# 打开百度
driver.get("https://www.baidu.com")
time.sleep(2)

# 输入‘大飞记Python’，点击搜索
driver.find_element(By.ID, "chat-textarea").send_keys("大飞记Python")
time.sleep(2)
driver.find_element(By.ID, "chat-submit-button").click()

# 等待3秒
time.sleep(2)

# 关闭浏览器
driver.quit()