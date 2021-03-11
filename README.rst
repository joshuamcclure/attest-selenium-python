*************
:warning: THIS REPOSITORY HAS BEEN DEPRECATED :warning:
*************

`axe DevTools Enterprise <https://www.deque.com/axe/devtools/>`__ has an officially support Python integration. Please use that instead. This integrations repository is no longer actively maintained.

attest-selenium-python
====================

attest-selenium-python integrates Attest HTML and selenium to enable automated web accessibility testing.

This project is a fork of the axe-selenium-python project, but uses Attest instead of Axe-core. Please see the sourced repo for more information: https://github.com/mozilla-services/axe-selenium-python.

THIS IS MEANT TO BE A SAMPLE/DEMONSTRATION INTEGRATION. Not approved for official production usage.

Requirements
------------

You will need the following prerequisites in order to use attest-selenium-python:

- selenium >= 3.0.0
- Python 2.7 or 3.6
- Attest HTML
- The appropriate driver for the browser you intend to use, downloaded and added to your path, e.g. geckodriver for Firefox:

  - `geckodriver <https://github.com/mozilla/geckodriver/releases>`_ downloaded and `added to your PATH <https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path#answer-40208762>`_

Installation
------------

To install attest-selenium-python:

.. code-block:: bash

  $ git clone git@github.com:joshuamcclure/attest-selenium-python.git
  $ cd attest-selenium-python
  $ pip install -r requirements.txt
  $ npm install
  $ python3 test.py 


Usage
------

.. code-block:: python

  # found in ./test.py

  from selenium import webdriver
  from attest_selenium_python import Attest

  def test_google():
      driver = webdriver.Firefox()
      driver.get("http://www.google.com")
      attest = Attest(driver)
      # Inject Attest javascript into page.
      attest.inject()
      # Run axe accessibility checks.
      results = attest.run()
      
      # Write results to file
      attest.write_results(results)
      attest.reporter()

      driver.close()
