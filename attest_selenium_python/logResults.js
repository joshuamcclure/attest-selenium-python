const AttestReporter = require('@deque/attest-reporter').default;
const fs = require('fs');

const jsonPath = process.argv[2];
const reportName = process.argv[3];
const id = process.argv[4];
const reportTypes = process.argv[5].split(',');

const filedata = fs.readFileSync(jsonPath, "utf8");
const results = JSON.parse(filedata);

let reporter = new AttestReporter(reportName, './a11y-results');
reporter.logTestResult(id, results);

reportTypes.map(type => {
    switch (type) {
        case 'html':
            return reporter.buildHTML('./a11y-results');

        case 'xml':
            return reporter.buildJUnitXML('./a11y-results');
        
        case 'csv':
            return reporter.buildCSV('./a11y-results');
    }
})

Promise.all(reportTypes)
    .then(() => true)
    .catch(() => false);