from time import sleep

from selenium.webdriver.common.by import By

import page
from base.base import Base


class WebBase(Base):
    """web项目专属方法"""
    # 根据限制文本点击指定元素
    def web_base_click_element(self,  click_text):
        # 1. 点击复选框
        self.base_click(page.web_fuxuan)
        # 2. 暂停（因为是动态显示过程）
        sleep(1)
        # 3. 点击具体选项
        loc = (By.XPATH, f'//span[text()="{click_text}"]')
        self.base_click(loc)