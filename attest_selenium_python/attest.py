# Source modified from axe-selenium-python
# Source repo: https://github.com/mozilla-services/axe-selenium-python

import json
import os
import shutil
from io import open

_DEFAULT_SCRIPT = os.path.join(
    os.path.dirname(__file__), "attest.js"
)

class Attest(object):
    def __init__(self, selenium, script_url=_DEFAULT_SCRIPT):
        self.script_url = script_url
        self.selenium = selenium


    def inject(self):
        """
        Recursively inject attest into all iframes and the top level document.
        """
        with open(self.script_url, "r", encoding="utf8") as f:
            self.selenium.execute_script(f.read())


    def run(self, context=None, options=None):
        """
        Run attest against the current page.

        :Args:
         - context [optional]: which page part(s) to analyze and/or what to exclude.
         - options [optional]: dictionary of attest options.
        """
        template = (
            "var callback = arguments[arguments.length - 1];"
            + "axe.run(%s).then(results => callback(results));"
        )
        args = ""

        # If context parameter is passed, add to args
        if context is not None:
            args += "%r" % context
        # Add comma delimiter only if both parameters are passed
        if context is not None and options is not None:
            args += ","
        # If options parameter is passed, add to args
        if options is not None:
            args += "%s" % options

        command = template % args
        response = self.selenium.execute_async_script(command)
        return response

    def reporter(self, data, reportName, testCaseName, reportTypes='html,xml,csv'):
        """
        Write JSON to file with the specified name.

        :Args:
         - data: results data generated from the accessibility scan
         - reportName: name of the item in scope
         - testCaseName: name of the test case
         - reportTypes [optional]: A comma seperated list of report types. options include: html, xml, or svc.
        """     

        if os.path.exists('./a11y-results'):
            shutil.rmtree('./a11y-results')

        if not os.path.exists('./a11y-results'):
            os.mkdir('./a11y-results')

        jsonPath = os.path.join("a11y-results","results.json")

        with open(jsonPath, "w", encoding="utf8") as f:
            try:
                f.write(unicode(json.dumps(data, indent=4)))
            except NameError:
                f.write(json.dumps(data, indent=4))

        self.runReporter(jsonPath, reportName, testCaseName, reportTypes)


    def runReporter(self, jsonPath, reportName, testCaseName, reportTypes):
        """
        Write JSON to file with the specified name.

        :Args:
         - data: results data generated from the accessibility scan
         - reportName: name of the item in scope
         - testCaseName: name of the test case
         - reportTypes: A comma seperated list of report types. options include: html, xml, or svc.
        """      
        path = os.path.join(
            os.path.dirname(__file__), "logResults.js"
        )
        log = 'node %s %s %s %s %s' % (path, jsonPath, reportName, testCaseName, reportTypes)
        os.system(log)
        os.remove(jsonPath)


    def buildReports(self):
        buildCmd = 'npx attest-reporter ./a11y-results --dest=./a11y-results --format=html'
        os.system(buildCmd)