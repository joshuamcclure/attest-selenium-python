const fs = require('fs');
const attestNode = require('@deque/attest-node');
const attest = attestNode.buildAttestSource();

fs.writeFileSync('attest.js', attest.source);