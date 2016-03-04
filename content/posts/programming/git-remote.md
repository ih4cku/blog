title: git remote notes
date: 2016-02-24 14:51:31
tags: git
status: draft

# READ

- http://stackoverflow.com/questions/292357/what-are-the-differences-between-git-pull-and-git-fetch
- http://longair.net/blog/2009/04/16/git-fetch-and-merge/
- https://www.atlassian.com/git/tutorials/syncing/git-push
- http://stackoverflow.com/questions/3258243/check-if-pull-needed-in-git

# questions

- Q: What is a `local tracking branch`?
    + A: When merging new commits of a `remote tracking branch`, it merges to the `local tracking branch`.
- Q: Which branches does `git fetch` fetch?
- Q: How is file system `rm` different with `git rm`?
    + `git rm` removes a file from both the repo and the working directory
- Q: How is the order of *parent commit* determined?
- Q: When merge conflict happened, how does git record I am merging?

# relative git commit names
- `^` means a commit ahead
- `^2` means the 2nd parent commit of the commit ahead
