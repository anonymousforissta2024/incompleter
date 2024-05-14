#Source: https://stackoverflow.com/questions/71450772/flask-pytest-failed-tests-test-data-response-pytest-post-data-response-type
@dataclass
class SeleniumElements:
    search_page: str
    response_page: str
    selenium_id: str
    selenium_class: str
    search_data: str
    driver: str
    
    def element_search_max_time(self,sec):
        return self.driver.implicitly_wait(sec)
  
    def get_data(self):
        self.driver.get(self.search_page)
        self.element_search_max_time(30)
        to_search = self.driver.find_element(By.ID, self.selenium_id)
        to_search.click()
        to_search.send_keys(self.search_data)
        submit = self.driver.find_element(By.CLASS_NAME,self.selenium_class)
        submit.click()
        self.element_search_max_time(30)
        fund_response = requests.get(self.search_page)
        assert fund_response.status_code == 200
        self.element_search_max_time(30)
        round_store_href_link = self.driver.find_element(
            By.XPATH, '//*[@id="main-content"]/div[4]/div/h1/a')
        round_store_href_link.click()
        self.element_search_max_time(30)
        rounds_response = requests.get(self.response_page)
        assert rounds_response.status_code == 200