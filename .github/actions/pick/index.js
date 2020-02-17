const core = require('@actions/core');
const last = require('last-successful-gh-commit').default;
try {
  var parts = core.getInput('repo').split('/', 2);
  last({
    owner: parts[0],
    name: parts[1],
    token: core.getInput('token'),
  })
  .then(commit => core.setOutput('sha', commit.node.oid))
  .catch(error => {
    console.error(error);
    core.setFailed(error.message);
  });
} catch (error) {
  console.error(error);
  core.setFailed(error.message);
}
