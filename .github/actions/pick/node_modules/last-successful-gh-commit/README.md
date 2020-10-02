<div align="center">
  <a href="https://www.npmjs.com/package/last-successful-gh-commit">
    <img src="https://img.shields.io/npm/v/last-successful-gh-commit.svg?maxAge=86400" alt="Last npm Registry Version">
  </a>
  <a href="https://travis-ci.org/ramasilveyra/last-successful-gh-commit?branch=master">
    <img src="https://travis-ci.org/ramasilveyra/last-successful-gh-commit.svg?branch=master" alt="Build Status">
  </a>
  <a href="https://codecov.io/github/ramasilveyra/last-successful-gh-commit?branch=master">
    <img src="https://img.shields.io/codecov/c/github/ramasilveyra/last-successful-gh-commit.svg?branch=master" alt="Code coverage">
  </a>
</div>


<h1 align="center">Get last successful GitHub commit</h1>

<p align="center"><b>last-successful-gh-commit</b></p>

<p align="center"><b>To achieve something similar to <code>GIT_PREVIOUS_SUCCESSFUL_COMMIT</code> env var defined by <a href="https://wiki.jenkins.io/display/JENKINS/Git+Plugin">Git Plugin</a> on Jenkins.</b></p>

<h2 align="center">Table of Contents</h2>

- [Install](#install)
- [Example](#example)
- [Usage](#usage)
- [Contribute](#contribute)
- [License](#license)

<h2 align="center">Install</h2>

**Node.js v6.5 or newer** is required.

Via the yarn client:

```bash
$ yarn add --dev last-successful-gh-commit
```

Via the npm client:

```bash
$ npm install --save-dev last-successful-gh-commit
```

<h2 align="center">Example</h2>

```js
import getLastSuccessfulGHCommit from 'last-successful-gh-commit';

const owner = 'ramasilveyra';
const name = 'last-successful-gh-commit';
const token = process.env.GH_TOKEN;

getLastSuccessfulGHCommit({ owner, name, token })
  .then(commit => {
    console.log('Last successful commit: ', commit);
  })
  .catch(err => {
    console.error('No successful commit found', err);
  });
```

<h2 align="center">Usage</h2>

### getLastSuccessfulGHCommit(options)

### options

Type: `Object`<br>
**Required**

### options.owner

Type: `string`<br>
**Required**

Owner of the repository.

### options.name

Type: `string`<br>
**Required**

Name of the repository.

### options.token

Type: `string`<br>
**Required**

GitHub token with `repo` scope.

<h2 align="center">Contribute</h2>

Feel free to dive in! [Open an issue](https://github.com/ramasilveyra/last-successful-gh-commit/issues/new) or submit PRs.

last-successful-gh-commit follows the [Contributor Covenant](http://contributor-covenant.org/version/1/3/0/) Code of Conduct.

<h2 align="center">License</h2>

[MIT](LICENSE.md)
