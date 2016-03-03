title: smart pointers
date: 2016-02-26 23:04:16
tags: c++

> 2016-02-26 23:04:16

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

> 2016-03-03 21:12:19

# smart pointers in practice

- [GotW #91: Smart Pointer Parameters](http://herbsutter.com/2013/05/30/gotw-91-smart-pointer-parameters/)
- [GotW #91 Solution: Smart Pointer Parameters](http://herbsutter.com/2013/06/05/gotw-91-solution-smart-pointer-parameters/), Guidelines:
	- Don’t pass a smart pointer as a function parameter unless you want to use or manipulate the smart pointer itself, such as to share or transfer ownership.
	- Prefer passing objects by value, `*`, or `&`, not by smart pointer.
		- Non-owning raw `*` pointers and `&` references are okay to observe an object whose lifetime we know exceeds that of the pointer or reference, which is usually true for function parameters. 
		- As usual, use a `*` if you need to express null, otherwise prefer to use a `&`; and if the object is input-only, write `const widget*` or `const widget&`.
	- `void f( unique_ptr<widget> )`
		- Express a “sink” function using a by-value `unique_ptr` parameter.
		- Superior to raw pointer because it documents the **semantics** in code.
		- Because the callee will now own the object, usually there should be no `const` on the parameter because the const should be irrelevant.
	- `void f( unique_ptr<widget>& )`
	    - Use a non-const `unique_ptr&` parameter only to modify the `unique_ptr`.
        - Don’t use a const `unique_ptr&` as a parameter; use `widget*` instead.
	- `void f( shared_ptr<widget> )`
		- Passing `shared_ptr` by value implies taking shared ownership.
		- Express that a function will store and share ownership of a heap object using a by-value `shared_ptr` parameter.
	- `void f( shared_ptr<widget>& )`
		- Passing `shared_ptr&` is useful for in/out shared_ptr manipulation.
		- Use a non-const `shared_ptr&` parameter only to modify the `shared_ptr`.
		- Use a `const shared_ptr&` as a parameter only if you’re not sure whether or not you’ll take a copy and share ownership; otherwise use `widget*` instead (or if not nullable, a `widget&`).
- *Passing shared pointers as arguments* on SO
	- http://stackoverflow.com/questions/10826541/passing-shared-pointers-as-arguments
	- http://stackoverflow.com/questions/17368644/passing-smart-pointers-by-reference
	- http://stackoverflow.com/questions/9155928/how-to-pass-smart-pointers-in-function
	- http://stackoverflow.com/questions/12519812/how-do-i-pass-smart-pointers-into-functions
	- [C++中方法的参数和返回值、类成员变量什么时候该用原始指针什么时候该用智能指针？](https://www.zhihu.com/question/22821303)
- [Smart Pointer Guidelines](https://www.chromium.org/developers/smart-pointer-guidelines)
- [Ownership and Smart Pointers](https://google.github.io/styleguide/cppguide.html#Ownership_and_Smart_Pointers)
- [Smart Pointers Gotchas](http://www.codeproject.com/Articles/547276/Smart-Pointers-Gotchas)
