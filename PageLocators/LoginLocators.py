from selenium.webdriver.common.by import By

class LoginLocator:
    #用户名 密码
    eles = (By.CSS_SELECTOR, "div input[name='name']")
    #点击按钮
    button = (By.CSS_SELECTOR, 'button[type="button"] span')
    #退出按钮
    logout = (By.CSS_SELECTOR, 'button span')
    #提示信息
    text = (By.CSS_SELECTOR,"p[class='el-message__content']")
