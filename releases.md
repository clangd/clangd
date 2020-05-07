# Binary releases

This repository has automation to build binary releases of clangd for the most
common platforms. This doesn't cover as many systems as the official releases
from http://releases.llvm.org/, and distro packages etc. The main advantages
is being able to cut releases easily whenever we want.

The releases are just a zip archive containing the `clangd` binary, and the
clang builtin headers. They should be runnable immediately after extracting the
archive. The linux binary has `libstdc++` and other dependencies statically
linked for maximum portability, and requires glibc 2.18 (the first version with
`thread_local` support).

## Creating a release manually

In GitHub, click the "Releases" tab and create a new release.
The tag name is significant, it's used in the directory name (`clangd_tagname`).

Because clangd sources don't live in this repository, the release description
must contain a magic string indicating the revision to build at, e.g.

   Built at llvm/llvm-project@0399d5a9682b3cef71c653373e38890c63c4c365

This must be a full SHA, not a short-hash, a tag or branch name, etc.
The release must **not** be a draft release, as that won't trigger automation.

## Building release binaries

Creating the release will trigger the `autobuild` workflow, visible under the
"Actions" tab. This runs a sequence of steps:

- First, the release is marked as a draft, so it's invisible to non-owners.
- Next, the sources are checked out and built on each of {mac, windows, linux}.
  These run in parallel, and the results are zipped and added to the release.
- If all builds succeeded, the release is published (marked as non-draft)

## Automatic snapshot releases

The `periodic` workflow runs on a weekly schedule and creates a release based
on the last green revision at llvm/llvm-project.
This in turn triggers the `autobuild` workflow above to produce binaries.

These snapshot releases are marked as "pre-release" - they don't undergo any
serious testing and so aren't particularly stable. However they're useful for
people to try the latest clangd.

## Credentials

Rather than the default GitHub Actions access token, these actions use a
Personal Access Token added to the repository as a secret. This is because:

- The default access token expires after an hour. Builds take longer than that.
- Releases created using the default access token don't trigger workflows.

If you fork the repository, you must provide the `RELEASE_TOKEN` secret.
