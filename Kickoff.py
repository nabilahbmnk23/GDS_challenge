import unittest
import time
from appium import webdriver


class AppTest(unittest.TestCase):

    def setUp(self):
        capabilities = {
         'deviceName': "LHS7N1892001371",
         'platformName': 'android',
         'appPackage': 'sg.gov.tech.bluetrace.staging',
         'appActivity': 'sg.gov.tech.bluetrace.SplashActivity',
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        " Tear down the test"
        self.driver.quit()

    def test_happyFlow(self):
        mobilenum = "83673418"
        el1 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[2]')
        el1.click()
        print('中文 Selected')
        el2 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[3]')
        el2.click()
        print('Melayu Selected')
        el4 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[4]')
        el4.click()
        print('தமிழ் Selected')
        el5 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[5]')
        el5.click()
        print('বাংলা Selected')
        el6 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[6]')
        el6.click()
        print('हिन्दी Selected')
        el7 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[7]')
        el7.click()
        print('ဗမာ Selected')
        el8 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[8]')
        el8.click()
        print('ไทย Selected')
        el9 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[1]')
        el9.click()
        print('EN Selected')
        letter = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/img_with_love')
        letter.click()
        next1 = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/img_next')
        next1.click()
        print('next image success')
        next2 = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/btn_right_action_how_it_works')
        next2.click()
        print('next image success')
        next3 = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/btn_right_action_how_it_works')
        next3.click()
        print('next image success')
        mobile = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/et_phone_number')
        print('Key in mobile number')
        mobile.send_keys(mobilenum)
        print('Mobile number entered')
        ver_otp = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/btn_verify_by_otp')
        ver_otp.click()
        print('Getting OTP and wait 30 seconds')
        time.sleep(30)
        print('OTP Auto-filled')

        el6 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView')
        el6.click()
        el7 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView')
        el7.click()
        el8 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView')
        el8.click()
        el9 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[4]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView')
        el9.click()
        el10 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[5]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView')
        el10.click()
        el11 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[6]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView')
        el11.click()
        el12 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView')
        el12.click()
        el13 = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/btn_next')
        el13.click()
        el14 = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/et_name')
        el14.click()
        el15 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.FrameLayout/android.widget.EditText')
        el15.click()
        el16 = self.driver.find_element_by_id('android:id/button1')
        el16.click()
        el17 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.widget.FrameLayout/android.widget.EditText')
        el17.click()
        el18 = self.driver.find_element_by_id('android:id/button1')
        el18.click()
        el19 = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/how_to_find')
        el19.click()
        el20 = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/close')
        el20.click()
        el21 = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/declaration_txt')
        el21.click()
        el22 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.widget.Button')
        el22.click()
        el23 = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[2]/android.view.View/android.view.View/android.widget.Button')
        el23.click()
        el24 = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/close')
        el24.click()
        el25 = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/declaration')
        el25.click()
        el26 = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/btn_register')
        el26.click()
        el27 = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/permission_bt_btn_allow')
        el27.click()
        el28 = self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        el28.click()
        # el29 = self.driver.find_element_by_id('android:id/button1')
        # el29.click()
        el30 = self.driver.find_element_by_id('sg.gov.tech.bluetrace.staging:id/btn_yes')
        el30.click()

    # def test_mobileNumberValidity(self):
    #     print("mobile")
    #
    # def test_OTPfail(self):
    #     print("OTP")
    #
    # def test_form(self):
    #     print("form")


if __name__ == '__main__':
    unittest.main()


