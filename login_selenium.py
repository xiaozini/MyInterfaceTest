from common.BasePageObject import BasePage


# driver = webdriver.Chrome(r'F:\yy\appDemo\selenium_test\chromedriver.exe')
# driver.implicitly_wait(10)
# driver.get("https://h5-qa.admin.yuedaowang.com/#/driverSettle")
# eles = driver.find_elements_by_css_selector("div input[name='name']")
# eles[0].send_keys('nxk')
# eles[1].send_keys("123")
# driver.find_element_by_css_selector('button[type="button"] span').click()
# time.sleep(3)
# logout = driver.find_element_by_css_selector('button[type="button"] span')
# if logout != "":
#     print('登录成功')

class SearchPage(BasePage):
    def __init__(self,driver,base_url="https://h5-qa.admin.yuedaowang.com/#/driverSettle"):
        BasePage.__init__(driver,base_url)

