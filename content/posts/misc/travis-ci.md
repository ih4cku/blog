title: Travis-CI
date: 2016-02-27 20:37:23
tags: travis

# Travis CI building lifecycle

- install: install dependencies
- script: build script

The complete process:

1. `before_install`
    - install native dependencies with `sudo apt-get install`
2. `install`
3. `before_script`
4. `script`
5. `after_success` or `after_failure`
6. optional `before_deploy`
7. optional `deploy`
8. optional `after_deploy`
9. `after_script`

The build process is broken when any of the first 4 steps return a non-zero exit code.

Skipping the install step: `install: true`


# Environment variables

- Environment variables can be accessed from any stage of the building process.
- Can be set in `.travis.yml` or web UI
- Can be encrypted with `travis encrypt MY_SECURE_ENV=<secure_value>` and put into `.travis.yml` after `secure:`