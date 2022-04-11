
from time import sleep
import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml

class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.mp_url)
        # 2. 通过统一入口类，实例化PageMpLogin类对象
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 结束
    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 测试
    @pytest.mark.parametrize('username,code,expect', read_yaml('mp_data.yaml'))
    def test_mp_login(self, username, code, expect):
        # 1.调用登陆方法
        self.mp.page_mp_login(username, code)
        # 2. 断言
        assert expect == self.mp.page_get_nickname()

