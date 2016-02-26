title: smart pointers
date: 2016-02-26 23:04:16
tags: c++

# `shared_ptr`
- cycle problem

# `weak_ptr`
- just observe the object, doesn't affect the lifetime
- can only be created from a `shared_ptr` or another `weak_ptr`
- can't dereference 
- neither `*` nor `->` is defined
- can't access the raw pointer, no `get()` function
- can only be set to empty state with `reset()` not by assigning to `nullptr`
- can only be used as a `shared_ptr` by `lock()`

# `unique_ptr`?
- zero overhead
- unique ownership
    + can be transferred around but only be owned by one owner at a time
    + the unique ownership is enforced by disallowing copy and assignment
    + if used as function argument, must by reference
    + ownership can only be transfered with move semantics 
        * as an `rvalue` with `std::move()` or a returned value
        * after transferring, the original owner becomes `nullptr`

# references
- [EECS 381 - Object-Oriented and Advanced Programming - Winter 2016](http://www.umich.edu/~eecs381/)
- [Using C++11's Smart Pointers](http://www.umich.edu/~eecs381/handouts/C++11_smart_ptrs.pdf)
- [C++11: unique_ptr](http://www.drdobbs.com/cpp/c11-uniqueptr/240002708)