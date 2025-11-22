import unittest
import urllib.request
import os

# Select correct URL based on ENV value passed in Jenkins
ENV = os.environ.get("ENVIRONMENT", "dev").lower()

if ENV == "prod":
    BASE_URL = "http://10.48.229.50"   # Production LoadBalancer
else:
    BASE_URL = "http://127.0.0.1:5000"  # Dev local access


class HttpLightTests(unittest.TestCase):

    def test_index_page_loads(self):
        """Ensure the index page loads successfully"""
        with urllib.request.urlopen(BASE_URL) as response:
            self.assertEqual(response.status, 200)


    def test_sample_warhammer_units_exist(self):
        """Validate that seeded Warhammer data appears on the home page"""
        with urllib.request.urlopen(BASE_URL) as response:
            html = response.read().decode('utf-8')

        # Warhammer units seeded by your data-gen.py file
        expected_units = [
            "Tactical Marine",
            "Terminator Squad",
            "Scout Sniper",
            "Dreadnought",
            "Devastator Squad"
        ]

        found = any(unit in html for unit in expected_units)
        self.assertTrue(found, "No Warhammer units found in the page source")


if __name__ == "__main__":
    unittest.main()
