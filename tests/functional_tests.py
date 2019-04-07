from selenium import webdriver
import unittest
import time


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "http://0.0.0.0:8000"

    def test_include_items(self):
        self.driver.get(self.base_url)
        items = ['Face Comparison', 'Bank Card Detection', ' Objects Prediction', 'Gesture Detection']
        self.assertIn('然小狼 | ranxiaolang', self.driver.title)
        product = self.driver.find_elements_by_xpath('/html/body/main/section[1]/p[1]')
        for item in items:
            self.assertIn(item, product[0].text)

    def test_gesture_detection(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_xpath('/html/body/main/section[1]/p[1]/a[4]').click()
        self.driver.find_element_by_name("image_file").send_keys('/Users/ziran/Develop/Git_file/AI-plateform-server/tests/images/Gesture7.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(10)
        gesture_res = self.driver.find_element_by_xpath('//*[@id="showgesture"]')
        self.assertIn('Gesture: Hand open', gesture_res.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCase("test_include_items"))
    suite.addTest(TestCase("test_gesture_detection"))
    # 执行测试
    runner = unittest.TextTestRunner(warnings='ignore')
    runner.run(suite)
