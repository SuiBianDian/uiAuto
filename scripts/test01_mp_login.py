
from time import sleep
import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml


log = GetLog.get_logger()

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

    # def setup(self):
    #     self.mp.driver.get(page.mp_url)   # 重新打开页面，防止成功后无法继续测试

    # 测试
    @pytest.mark.parametrize('username,code,expect,success', read_yaml('mp_data.yaml'))
    def test_mp_login(self, username, code, expect, success):
        # 1.调用登陆方法
        log.info(f'正在执行组合业务，用户名：{username}, 密码：{code}')
        self.mp.page_mp_login(username, code)
        if success:
            try:
                # 2. 断言
                assert expect == self.mp.page_get_nickname()
            except AssertionError as e:
                log.error(f'断言出错，错误信息为：{e}')
                self.mp.base_get_img()
            self.mp.base_find(page.mp_xx,3).click()
            self.mp.base_find(page.mp_touxiang, 3).click()

            sleep(1)
            """必须等待，应为他是一个动态的出现过程，找到了还不能立刻点击"""
            self.mp.base_find(page.mp_exit, 3).click()
        else:
            try:
            # 2. 断言
                assert expect == self.mp.base_get_txt(page.mp_err_code)
            except AssertionError as e:
                log.error(f'断言出错，错误信息为：{e}')
                self.mp.base_get_img()

