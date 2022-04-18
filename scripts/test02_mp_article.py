from time import sleep

import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog().get_logger()
class TestMpArticle:
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_web_driver(page.mp_url)
        # 通过统一入口类获取对象
        self.page = PageIn(self.driver)
        # 获取PageMpLogin，调用成功登录
        self.page.page_get_PageMpLogin().page_mp_login_success()
        # 获取PageMpArticle
        self.web = self.page.page_get_PageMpArticle()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    def setup(self):
        self.driver.get(page.web_url)
        """
        下面这一个也可以用refresh代替，但是refresh是瞬间刷新，可能还没登陆上来就触发刷新了，这时会刷新登录页面了
        """
        self.driver.get(page.web_url)

    @pytest.mark.parametrize('title,content,click_text,expect', read_yaml('mp_article.yaml'))
    def test_mp_article(self, title, content, click_text, expect):
        # 调用发布文章业务方法
        self.web.page_mp_article(title, content, click_text)
        # 查看断言
        try:
            sleep(0.5)
            assert expect == self.web.page_get_publish_info()
            log.info(f'断言成功：{expect} == {self.web.page_get_publish_info()}')
        except AssertionError as e:
            log.error(f'断言失败，错误信息为{e}')
            sleep(0.5)
            self.web.base_get_img()
