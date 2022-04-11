from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化
    def __init__(self, driver):
        self.driver = driver

    # 查找
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        loc： 定位元素的方法+元素信息，是列表
        """
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入
    def base_input(self, loc, value):
        # 1. 定位
        el = self.base_find(loc)
        # 2. 清空  但是clear会失效
        sleep(0.5)
        ActionChains(self.driver).double_click(el).perform()
        # 3. 输入
        el.send_keys(value)

    # 点击
    def base_click(self, loc):
        # 1. 定位
        el = self.base_find(loc)
        # 2. 点击
        el.click()

    # 获取文本
    def base_get_txt(self, loc):
        return self.base_find(loc).text
