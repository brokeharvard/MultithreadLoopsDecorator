# multithread_loops_decorator
An easy and efficient decorator to cause a function to split the work of looping its iterable parameter into multiple threads.

# What?
- The decorator takes as its parameter: a function that loops its own iterable parameter and returns an iterable.
- The decorator makes the function split the work of looping its iterable (and doing whatever else the function does) into up to 15 threads.
- Once all the work is complete, the decorated function returns a map object.

# How?
Just put "@async" (without the quotation marks) before the function that you want to multithread.

# To Do
- Might be nice to add optimal max_workers parameter to change default of 15 max workers (threads)
