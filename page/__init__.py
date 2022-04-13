"""以下数据为自媒体模块配置数据"""
from selenium.webdriver.common.by import By
# 前台url
mp_url = 'http://pc-toutiao-python.itheima.net/#/login'
# 用户名
mp_username = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
# 验证码
mp_code = (By.CSS_SELECTOR, '[placeholder="验证码"]')
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR, '.el-button--primary')
# 密码错误
mp_err_code = (By.CSS_SELECTOR, '.el-message__content')
# 昵称
mp_nickname = (By.CSS_SELECTOR, '.user-name')
# xx
mp_xx = (By.CSS_SELECTOR, '.el-icon-close')
# 头像
mp_touxiang = (By.CSS_SELECTOR, '.user-name')
# 退出
mp_exit = (By.CSS_SELECTOR, '.el-dropdown-menu__item--divided')