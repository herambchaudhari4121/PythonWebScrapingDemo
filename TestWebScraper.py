import unittest
from webscraper_demo import get_jobs, get_job_listing


class TestWebScarper(unittest.TestCase):

    def test_get_job_listing(self):
        job_details = get_jobs()
        self.assertTrue(len(job_details) > 0)

if __name__ == "__main__":
    unittest.main()
