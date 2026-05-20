# 该代码主要演示pytest在自动化测试中的应用

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    print("前置：打开浏览器")
    driver = webdriver.Chrome()
    # 打开浏览器后，去执行测试用例
    yield driver
    print("后置：关闭浏览器")
    driver.quit()


# 打开百度，并断言
def test_baidu_title(browser):
    print("打开百度首页")
    browser.get("https://www.baidu.com")
    print("断言:是否存在'百度一下'文本")
    assert browser.find_element(By.CSS_SELECTOR, "#chat-submit-button").text == "百度一下"