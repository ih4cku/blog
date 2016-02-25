title: git index meet merging conflict
date: 2016-02-25 12:31:06
tags: git

The content of `index` when merging conflict happened:

```bash
$ git ls-files -s
100644 ce013625030ba8dba906f756967f9e9ca394464a 1       a.txt
100644 94954abda49de8615a048f8d2e64b5de848e27a1 2       a.txt
100644 e9f71396d33d1553ccd46186d4c11363b6841f6f 3       a.txt

$ git cat-file -p ce013625030ba8dba906f756967f9e9ca394464a # :1:a.txt
hello

$ git cat-file -p 94954abda49de8615a048f8d2e64b5de848e27a1 # :2:a.txt
hello
world

$ git cat-file -p e9f71396d33d1553ccd46186d4c11363b6841f6f # :3:a.txt
hello
neurocoder
```
After solving the conflict, the file is added to `:0:a.txt` in `index`.