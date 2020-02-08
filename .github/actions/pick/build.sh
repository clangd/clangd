#!/bin/bash -ex
# Rather than checking in node_modules, check in a standalone dist/index.js.
# Requires ncc: npm i -g @zeit/ncc
npm install
ncc build -m index.js
