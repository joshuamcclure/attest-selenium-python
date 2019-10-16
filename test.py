from selenium import webdriver
from attest_selenium_python import Attest

def test_google():
    driver = webdriver.Firefox()
    driver.get("http://www.google.com")
    attest = Attest(driver)
    # Inject axe-core javascript into page.
    attest.inject()
    # Run axe accessibility checks.
    results = attest.run()
    
    # Write results to file
    attest.write_results(results)
    attest.reporter()

    driver.close()
    # Assert no violations are found
    # assert len(results["violations"]) == 0, attest.report(results["violations"])

test_google()