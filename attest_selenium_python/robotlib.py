from robot.api.deco import keyword
from attest import Attest
from robot.libraries.BuiltIn import BuiltIn

class robotlib(object):
    """ Test library for the Deque Attest library. """

    def __init__(self, reportName, testCaseName, reportTypes='html,xml,csv', reportDir='./a11y-results', axeConfig=None):
        self.reportName = reportName
        self.testCaseName = testCaseName
        self.reportTypes = reportTypes
        self.reportDir = reportDir
        self.axeConfig = axeConfig
    
    def get_browser(self):
        return BuiltIn().get_library_instance('SeleniumLibrary').driver

    def run_accessibility_tests(self):
        """
        Run accessibility tests on a given page/scope
        """
        driver = self.get_browser()
        attest = Attest(driver)
        attest.inject()
        results = attest.run()
        attest.reporter(results, self.reportName, self.testCaseName, self.reportTypes, self.reportDir)

    def does_not_contain_accessibility_violations(self):
        """
        Run accessibility tests on a given page/scope and fail the test case if violations are found
        """
        driver = self.get_browser()
        attest = Attest(driver)
        attest.inject()
        results = attest.run()
        attest.reporter(results, self.reportName, self.testCaseName, self.reportTypes, self.reportDir)
        if len(results["violations"]) > 0:
            raise AssertionError('Accessibility violations found: expected 0 found %s.' % (str(len(results["violations"]))))