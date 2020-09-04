const AttestReporter = require("attest-reporter-async");
const fs = require('fs');

const jsonPath = process.argv[2];
const reportName = process.argv[3];
const id = process.argv[4];
const reportTypes = process.argv[5].split(',');
const reportDir = process.argv[6] || './a11y-results';

const filedata = fs.readFileSync(jsonPath, "utf8");
const results = JSON.parse(filedata);

(async () => {
    AttestReporter.reportingSetup(reportDir, reportName);
    AttestReporter.logTestResult(id, results);
    await AttestReporter.buildReports(reportDir, reportTypes);
})();