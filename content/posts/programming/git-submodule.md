title: git submodule
date: 2016-02-25 14:57:08
tags: git

Using third-party libraries is very common in daily development.
Git submodule is cool to make the library related with its original remote repo.

When cloning or pulling a repo containing submodules, these will not be checkout out by default (except for using `--recursive` option). The `init` and `update` command will maintain submodules with appropriate revision.

The main repo record a `gitlink` tree entry in the commit and use that to indicate the revision record of the submodules when checking out.

A record file named `.gitmodules` is saved at the root of the source tree assigning a logical name of the submodule and the URL the submodule shall be cloned from.
