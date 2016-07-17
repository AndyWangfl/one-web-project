from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class  NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):

        #访问应用的首页
        self.browser.get("http://127.0.0.1:8000")

        #网页的标题和头部含有“To-Do”这个词
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #应用邀请她输入一个代办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #她在一个文本框中输入了“Buy peacock feathers”
        #她的爱好是使用假绳做诱饵钓鱼
        inputbox.send_keys("Buy peacock feathers")

        #她按回车后，页面跟新了
        #代办事项表格中显示了“1：Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == "1: Buy peacock feathers" for row in rows)
        )
        #页面中又显示了一个文本框，可以输入其他的代办事项
        #她输入了“Use peacock feathers to make a fly”
        self.fail('Finish the test!')

        #页面再次跟新，她的清单中显示了这两个代办事项
        [...]
if __name__ == '__main__':
    unittest.main(warnings='ignore')

