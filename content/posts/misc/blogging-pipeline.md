title: My bloging pipeline
date: 2016-02-25 15:13:49
tags: pelican

1. write posts
2. local test
```bash
$ make html && make serve
```
3. commit modification
```bash
$ git add .
$ git commit -m 'new post'
```
4. push to github
```bash
$ make github
```