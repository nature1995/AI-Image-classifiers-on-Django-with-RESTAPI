from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest
import time
import os


class TestCase(LiveServerTestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
#         self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = self.live_server_url

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
        self.driver.find_element_by_name("image_file").send_keys(os.path.abspath('.') + '/functional_tests/images/Gesture7.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        gesture_res = self.driver.find_element_by_xpath('//*[@id="showgesture"]')
        self.assertIn('Gesture: Hand open', gesture_res.text)

    def test_bank_card_detection(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_xpath('/html/body/main/section[1]/p[1]/a[2]').click()
        self.driver.find_element_by_name("image_file").send_keys(os.path.abspath('.') + '/functional_tests/images/card3.png')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        bank_card_res = self.driver.find_element_by_xpath('//*[@id="shownumber"]')
        self.assertIn('Card number: 4000123456789123', bank_card_res.text)

    def test_face_compare_detection(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_xpath('/html/body/main/section[1]/p[1]/a[1]').click()
        self.driver.find_element_by_name("image_file1").send_keys(os.path.abspath('.') + '/functional_tests/images/campare1.jpg')
        self.driver.find_element_by_name("image_file2").send_keys(os.path.abspath('.') + '/functional_tests/images/campare2.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        face_compare_res = self.driver.find_element_by_xpath('//*[@id="showconfidence"]')
        self.assertIn('Similarity：85', face_compare_res.text)

    def test_identification_detection(self):
        self.driver.get(self.base_url+'/predict/')
        time.sleep(10)
        self.driver.find_element_by_name("image").send_keys(os.path.abspath('.') + '/functional_tests/images/fox.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        r50_res_1 = self.driver.find_element_by_xpath('//*[@id="showprediction"]')
        self.assertIn('Prediction: red_fox', r50_res_1.text)
        self.driver.find_element_by_name("image").send_keys(os.path.abspath('.') + '/functional_tests/images/panda0.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        r50_res_2 = self.driver.find_element_by_xpath('//*[@id="showprediction"]')
        self.assertIn('Prediction: giant_panda', r50_res_2.text)

        self.driver.get(self.base_url+'/predict_MobileNet/')
        time.sleep(10)
        self.driver.find_element_by_name("image").send_keys(os.path.abspath('.') + '/functional_tests/images/fox.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        mn_res_1 = self.driver.find_element_by_xpath('//*[@id="showprediction"]')
        self.assertIn('Prediction: red_fox', mn_res_1.text)
        self.driver.find_element_by_name("image").send_keys(os.path.abspath('.') + '/functional_tests/images/panda0.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        mn_res_2 = self.driver.find_element_by_xpath('//*[@id="showprediction"]')
        self.assertIn('Prediction: giant_panda', mn_res_2.text)

        self.driver.get(self.base_url+'/predict_MobileNetV2/')
        time.sleep(10)
        self.driver.find_element_by_name("image").send_keys(os.path.abspath('.') + '/functional_tests/images/fox.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        mn2_res_1 = self.driver.find_element_by_xpath('//*[@id="showprediction"]')
        self.assertIn('Prediction: grey_fox', mn2_res_1.text)
        self.driver.find_element_by_name("image").send_keys(os.path.abspath('.') + '/functional_tests/images/panda0.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        mn2_res_2 = self.driver.find_element_by_xpath('//*[@id="showprediction"]')
        self.assertIn('Prediction: giant_panda', mn2_res_2.text)

        self.driver.get(self.base_url+'/predict_Xception/')
        time.sleep(10)
        self.driver.find_element_by_name("image").send_keys(os.path.abspath('.') + '/functional_tests/images/fox.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        mn2_res_1 = self.driver.find_element_by_xpath('//*[@id="showprediction"]')
        self.assertIn('Prediction: grey_fox', mn2_res_1.text)
        self.driver.find_element_by_name("image").send_keys(os.path.abspath('.') + '/functional_tests/images/panda0.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        mn2_res_2 = self.driver.find_element_by_xpath('//*[@id="showprediction"]')
        self.assertIn('Prediction: giant_panda', mn2_res_2.text)

        self.driver.get(self.base_url+'/predict_VGG16/')
        time.sleep(10)
        self.driver.find_element_by_name("image").send_keys(os.path.abspath('.') + '/functional_tests/images/fox.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        vgg16_res_1 = self.driver.find_element_by_xpath('//*[@id="showprediction"]')
        self.assertIn('Prediction: red_fox', vgg16_res_1.text)
        self.driver.find_element_by_name("image").send_keys(os.path.abspath('.') + '/functional_tests/images//panda0.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        vgg16_res_2 = self.driver.find_element_by_xpath('//*[@id="showprediction"]')
        self.assertIn('Prediction: giant_panda', vgg16_res_2.text)

        self.driver.get(self.base_url+'/predict_VGG19/')
        time.sleep(10)
        self.driver.find_element_by_name("image").send_keys(os.path.abspath('.') + '/functional_tests/images/fox.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        vgg19_res_1 = self.driver.find_element_by_xpath('//*[@id="showprediction"]')
        self.assertIn('Prediction: red_fox', vgg19_res_1.text)
        self.driver.find_element_by_name("image").send_keys(os.path.abspath('.') + '/functional_tests/images/panda0.jpg')
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/button').click()
        time.sleep(5)
        vgg19_res_2 = self.driver.find_element_by_xpath('//*[@id="showprediction"]')
        self.assertIn('Prediction: giant_panda', vgg19_res_2.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    # Test suite
    suite = unittest.TestSuite()
    suite.addTest(TestCase("test_include_items"))
    suite.addTest(TestCase("test_gesture_detection"))
    suite.addTest(TestCase("test_bank_card_detection"))
    suite.addTest(TestCase("test_face_compare_detection"))
    suite.addTest(TestCase("test_identification_detection"))
    # Run test
    runner = unittest.TextTestRunner()
    runner.run(suite)
