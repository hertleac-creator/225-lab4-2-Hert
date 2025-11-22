from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import unittest

class TestModels(unittest.TestCase):
    def setUp(self):
        # Setup Firefox options
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # Run in headless mode
        firefox_options.add_argument("--no-sandbox")
        firefox_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Firefox(options=firefox_options)

    def test_models_displayed(self):
        driver = self.driver
        driver.get("http://10.48.229.149")  # Replace with your actual URL

        # Define test models and their factions
        test_models = [
            {"name": f"Test Model {i}", "faction": f"Faction {i}"} for i in range(10)
        ]

        # Check that each model and faction is displayed on the page
        for model in test_models:
            assert model["name"] in driver.page_source, f"{model['name']} not found"
            assert model["faction"] in driver.page_source, f"{model['faction']} not found"

        print("All test models and factions verified successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
