from selenium import webdriver
from attest_selenium_python import Attest
import time

def test_google():
    driver = webdriver.Firefox()
    driver.get("https://google.com")
    
    attest = Attest(driver)
    # Inject axe-core javascript into page.
    attest.inject()
    # time.sleep(10)
    # Run axe accessibility checks.
    # results = attest.run(None, "{ runOnly: {type: 'tag', values: ['section508']}, 'rules': {'bypass': { enabled: false}} }")
    results = attest.run()
    # Write results to file
    attest.reporter(results, 'Google.com', 'Signon', 'html,xml,csv')

    driver.close()
    # Assert no violations are found
    # assert len(results["violations"]) == 0, attest.report(results["violations"])

test_google()