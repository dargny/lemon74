import time
def login_page(username,password,driver):   #形参  -参数化 --提高代码复用率
    driver.find_element_by_id("username").send_keys(username)  # 找到了有username这个id的元素--点击，输入内容
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()

def open_url(url,driver):   #打开网页
    driver.get(url)
    driver.maximize_window()

def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login_page(username,password,driver)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    driver.switch_to.frame(1)
    driver.find_element_by_id("searchNumber").send_keys(s_key)
    # 点击查询
    driver.find_element_by_id("searchBtn").click()
    time.sleep(1)#强制等待和自动等待经常混合使用
    # 找到单据编号
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text#按层级
    return num
