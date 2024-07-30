class home_page(object):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def check_home_page(self):
        url=self.driver.current_url
        if 'false' in url:
            assert 1==1