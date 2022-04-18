import time
from time import sleep

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

log = GetLog.get_logger()


class Base:
    # 初始化
    def __init__(self, driver):
        log.info(f'正在初始化driver：{driver}')
        self.driver = driver

    # 查找
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        loc： 定位元素的方法+元素信息，是列表
        """
        log.info(f'正在定位元素：{loc}')
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入
    def base_input(self, loc, value):
        # 1. 定位
        el = self.base_find(loc)
        # 2. 清空  但是clear会失效
        sleep(1)
        log.info(f'正在对{loc}进行清空')
        ActionChains(self.driver).double_click(el).perform()
        # 3. 输入
        log.info(f'正在输入信息：{value}')
        el.send_keys(value)

    # 点击
    def base_click(self, loc):
        # 1. 点击
        log.info(f'正在点击：{loc}')
        self.base_find(loc).click()

    # 获取文本
    def base_get_txt(self, loc):
        log.info(f'正在获取{loc}的文本')
        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        log.error(f'断言出错，正在执行截图操作！')
        # self.driver.get_screenshot_as_file(f'./image/{time.strftime("%Y%m%d %H%M%S")}.png')
        self.driver.get_screenshot_as_file(f'./image/error.png')
        # 调用 图片写入报告方法
        log.error('断言出错，正在将图片写入allure报告')
        self.__base_write_img()

    # 将图片写入报告 (私有)
    def __base_write_img(self):
        # 1.获取文件流
        with open('./image/error.png', 'rb') as f:
            # 2.调用 allure.attach将图片贴入报告
            allure.attach(f.read(), '错误原因', allure.attachment_type.PNG)
