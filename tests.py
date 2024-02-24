import unittest
from src.scraper import Scraper


class utilsTests(unittest.TestCase):

    def test_function_name(self):

        pass


class scraperTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.scraper = Scraper()

    def test_title_scraper_empty_filters(self):
        result = self.scraper.title_scraper(
            {"title": "", "release_date": "", "genre": "", "role": ""}
        )
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)

    def test_title_scraper_with_all_filters(self):
        result = self.scraper.title_scraper(
            {
                "title": "Funny Guy",
                "release_date": "2020",
                "genre": "comedy",
                "role": "adam sandler",
            }
        )
        self.assertGreater(len(result), 0)

    def test_title_scraper_with_partial_filters(self):
        result = self.scraper.title_scraper(
            {"title": "", "release_date": "", "genre": "biography", "role": ""}
        )
        self.assertGreater(len(result), 0)

    def test_real_name_scrpaer(self):
        result = self.scraper.name_scraper("Adam Sandler")
        self.assertIsNotNone(result)

    def test_empty_name_scrpaer(self):
        result = self.scraper.name_scraper("")
        self.assertIs(result, "")


if __name__ == "__main__":
    unittest.main()
