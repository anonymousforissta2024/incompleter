#Source: https://stackoverflow.com/questions/60068543/python-script-problems-with-type-error-type-object-is-not-iterable
from scraper.config import Config
# from scraper.google_plus import GooglePlus
from scraper.scraper import Scraper
from scraper.spokeo import Spokeo


class EmailChecker:
    def __init__(self):
        config = Config()

        # Open instance to chromedriver
        self.__scraper = Scraper()

    def check_email(self, email):
        config = Config()
        results = {}

        # for _ in (GooglePlus, Spokeo):
        for _ in (Spokeo):
            site = _(self.__scraper)

            try:
                result = site.search_for_email(email)
            except Exception:
                if config.debug:
                    raise
                result = None

            try:
                site.logout()
            except Exception:
                if config.debug:
                    raise
                pass

            results[_.__name__] = result

        try:
            self.__scraper.driver.close()
        except Exception:
            pass

        try:
            self.__scraper.driver.quit()
        except Exception:
            pass

        return results