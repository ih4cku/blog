title: c++ containers
date: 2016-02-27 23:52:26
tags: c++

# choose a container

![hello](http://homepages.e3.net.nz/~djm/containerchoice.png)

# hash table

- [Is there any advantage of using map over unordered_map in case of trivial keys?](http://stackoverflow.com/questions/2196995/is-there-any-advantage-of-using-map-over-unordered-map-in-case-of-trivial-keys)
- [When should I use unordered_map and not std::map](http://stackoverflow.com/questions/6173860/when-should-i-use-unordered-map-and-not-stdmap)

## `map`

 1. Usually implemented using [red-black tree][1].
 2. Elements are sorted.
 3. Relatively small memory usage (doesn't need additional memory for the hash-table).
 4. Relatively fast lookup: $O(\log N)$.

## `unordered_map`

 1. Usually implemented using [hash-table][2].
 2. Elements are not sorted.
 3. Requires additional memory to keep the hash-table. 
 4. Fast lookup O(1), but constant time depends on the [hash-function][3] which could be relatively slow. Also keep in mind that you could meet with the [Birthday problem](http://en.wikipedia.org/wiki/Birthday_problem).


  [1]: http://en.wikipedia.org/wiki/Red-black_tree
  [2]: http://en.wikipedia.org/wiki/Hash_table
  [3]: http://en.wikipedia.org/wiki/Hash_function
