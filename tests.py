import unittest
from src.scraper import Scraper
from src.utils.winningMovie import find_winning_movie


class utilsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dummy_data = [
            {
                "title": "The Lord of the Rings: The Fellowship of the Ring",
                "year": "2001",
                "picture_url": "https://m.media-amazon.com/images/M/MV5BYzljODlmODMtZGJlMy00ZjgxLTliNmYtNGYzZGM2OGViNmU5XkEyXkFqcGdeQXVyMjMyMzI4MzY@._V1_QL75_UY207_CR4,0,140,207_.jpg",
            },
            {
                "title": "A Passage to Middle-earth: The Making of 'Lord of the Rings'",
                "year": "2001",
                "picture_url": "https://m.media-amazon.com/images/M/MV5BOTc3NjA5MDYxNF5BMl5BanBnXkFtZTcwMTY4MzEyMQ@@._V1_QL75_UX140_CR0,5,140,207_.jpg",
            },
            {
                "title": "National Geographic: Beyond the Movie - The Lord of the Rings: The Fellowship of the Ring",
                "year": "2001",
                "picture_url": "https://m.media-amazon.com/images/M/MV5BMThhMGMwZTItYzc1Yy00YzgyLWIxMGMtNDFjZWVjMjM1MjMwXkEyXkFqcGdeQXVyODc5Mjc4Nzg@._V1_QL75_UY207_CR10,0,140,207_.jpg",
            },
        ]

        cls.dummy_history = {
            "Madame Web": 1,
            "Deadpool & Wolverine": 1,
            "Poor Things": 1,
            "Wicked: Part One": 1,
            "Anyone But You": 1,
            "Dune: Part Two": 1,
            "Argylle": 1,
            "Twisters": 1,
            "The Beekeeper": 1,
            "The Lord of the Rings: The Fellowship of the Ring": 1,
            "The Lord of the Rings: The War of the Rohirrim": 1,
            "The Lord of the Rings: The Return of the King": 1,
            "The Lord of the Rings: The Two Towers": 1,
            "The Lord of the Rings": 1,
            "The Lord of the Rings: The Empire of Saruman": 1,
            "A Passage to Middle-earth: The Making of 'Lord of the Rings'": 1,
            "National Geographic: Beyond the Movie - The Lord of the Rings: Return of the King": 1,
        }

    def test_find_winning_movie_with_empty_history(self):
        result = find_winning_movie(self.dummy_data, {})
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

    def test_find_winning_movie_with_data_and_history(self):
        result = find_winning_movie(self.dummy_data, self.dummy_history)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)


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
