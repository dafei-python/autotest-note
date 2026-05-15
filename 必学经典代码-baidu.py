# 基础十二行代码（自动化测试经典项目）

# 打开Chrome浏览器，并输入“python”，点击“搜索”
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# 启动浏览器驱动
driver = webdriver.Chrome()

# 输入百度地址
driver.get("https://www.baidu.com")
sleep(1)

# 输入python
driver.find_element(By.ID, "chat-textarea").send_keys("python")
sleep(1)

# 点击百度一下按钮
driver.find_element(By.ID, "chat-submit-button").click()
sleep(2)

# 关闭浏览器
driver.quit()
