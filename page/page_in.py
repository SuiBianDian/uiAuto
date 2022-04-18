from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取 page_mp_login对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)
