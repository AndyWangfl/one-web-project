from selenium import webdriver

browser = webdriver.Firefox()

browser.get("http://127.0.0.1:8000")

assert 'Django' in browser.title



#browser.get("http://www.baidu.com")
#assert("百度" in browser.title)

