import page
from base.base import Base


class PageMpLogin(Base):
    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.mp_username, username)

    # 输入验证码
    def page_input_code(self, code):
        self.base_input(page.mp_code, code)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.mp_login_btn)

    # 获取昵称
    def page_get_nickname(self):
        return self.base_get_txt(page.mp_nickname)

    # 组合业务
    def page_mp_login(self, username, code):
        """
        组合业务只能组合同页面的业务，多页面需要切换页面才能进行操作
        """
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()
