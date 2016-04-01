title: Symmetry breaking
data: 2016-04-01 23:02:55
tags: machine learning
category: academic

# Symmetry breaking

Saw this word in many deep learning papers, and find it's a general rule for developing better machine learning algorithms. ( see [Asymmophobia](http://hunch.net/?p=632), a great post by John Langford)

## Why symmetry is bad?

> If all weights start with equal values and if the solution requires that unequal weights be developed, the system can never learn.

see [this answer](http://stats.stackexchange.com/a/45092/12667), [cs231n lecture](http://cs231n.github.io/neural-networks-2/) and [Hinton's lecture, p10](http://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf).


> Empirically, breaking symmetry well seems to yield great algorithms.

As summarized in the post, **randomization** in neural networks is a method of symmetry breaking.