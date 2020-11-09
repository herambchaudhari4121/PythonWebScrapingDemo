import unittest
from webscraper_demo import get_jobs, get_job_listing, extract_qualification


class TestWebScarper(unittest.TestCase):

    def test_get_job_listing(self):
        job_details = get_jobs()
        self.assertTrue(len(job_details) > 0)

    def test_extract_qualificatioon(self):
        qual = extract_qualification('/careers/jobs/2537073536607922/')
        self.assertTrue(len(qual) > 0)

if __name__ == "__main__":
    unittest.main()
