#Source: https://stackoverflow.com/questions/77556031/getting-typeerror-expected-str-bytes-or-os-pathlike-object-not-int
class Testcase_DDT_Login:
    baseURL = ReadProperties.application_url()
    Path = ".//TestData/test-data.xlsx"
    logger = ReadLog.loggen()

    # Verifying Multiple Login Credential

    def test_multiple_login(self, setup):
        self.logger.info("[TestCase_002] : Verify multiple login credential form testdata file ")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.rows = XLUtils.getRowCount(self.Path, 'Sheet1')
        lst_status = []

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.Path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.rows, 'Sheet1', r, 2)
            self.exp_result = XLUtils.readData(self.rows, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clicklogin()
            time.sleep(10)
            act_result = "Order Info"
            exp_result_hp = self.lp.orderinfo()