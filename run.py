
from python_class import lesson_6   #导入函数文件
from test_data import test_data     #导入测试数据 文件
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#调用函数——1、先参数取出来 2、传参到函数调用里
url=test_data.url["url"]                #取值url
user =test_data.login_date["username"]  #取值登录用户名
pwd =test_data.login_date["password"]   #取值登录密码
s_key = test_data.s_key["s_key"]        #取值搜索的关键字
print(url,user,pwd,s_key)
#函数的调用-传参
#给函数定义了一个返回值——调用时用一个变量接收返回值：
result=lesson_6.search_key(driver=driver,url=url,username=user,password=pwd,s_key=s_key)
if s_key in result:
    print("搜索结果正确")
else:
    print("用例测试不通过")

