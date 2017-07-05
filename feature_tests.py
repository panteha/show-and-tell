from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_navigate_to_site_and_upload_a_pic(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('ShowNTell', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('ShowNTell', header_text
        uploadbox = self.browser.find_element_by_id("Uploader")
        uploadbox.send_keys(os.getcwd()+"/image.png")
        self.assertTrue(
           # expect current_path to be uploaded image link
           # expect page to have image content
        )
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
