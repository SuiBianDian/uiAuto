from selenium import webdriver


class GetDriver:
    # 1. 声明变量
    __web_driver = None

    # 2. 获取driver
    @classmethod
    def get_web_driver(cls, url):
        if cls.__web_driver is None:
            cls.__web_driver = webdriver.Chrome('D:\Python\chromedriver.exe')
            cls.__web_driver.maximize_window()
            cls.__web_driver.get(url)
        return cls.__web_driver

    # 3. 退出driver
    @classmethod
    def quit_web_driver(cls):
        if cls.__web_driver:
            cls.__web_driver.quit()
            cls.__web_driver = None
