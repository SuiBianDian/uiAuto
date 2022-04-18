from time import sleep

import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()
class PageMpArticle(WebBase):
    # 点击内容管理
    def page_click_content_manage(self):
        self.base_click(page.web_content_manage)

    # 点击发布文章
    def page_click_publish_article(self):
        self.base_click(page.web_publish_article)

    # 输入标题
    def page_input_title(self, value):
        self.base_input(page.web_title, value)

    # 输入内容
    def page_input_content(self, value):
        # 切换frame
        el = self.base_find(page.web_iframe)
        self.driver.switch_to.frame(el)
        # 输入内容
        self.base_input(page.web_content,value)
        # 返回默认frame
        self.driver.switch_to.default_content()

    # 选择封面
    def page_choose_cover(self):
        self.base_click(page.web_cover)

    # 选择频道
    def page_choose_channel(self, click_text):
        self.web_base_click_element(click_text)

    # 点击发表
    def page_click_publish(self):
        self.base_click(page.web_publish)

    # 获取发表文章信息
    def page_get_publish_info(self):
        return self.base_get_txt(page.web_publish_info)

    # 组合业务
    def page_mp_article(self, title, content, click_text):
        log.info(f'正在执行组合业务，标题：{title}, 内容：{content}, 频道:{click_text}')
        self.page_click_content_manage()
        sleep(1)
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_choose_cover()
        self.page_choose_channel(click_text)
        self.page_click_publish()
