# multithread_loops_decorator
Provides easy and efficient decorator to cause function split work of looping iterable parameter (and doing whatever else the function does) into up to 15  threads. Once all work completed, returns map object.

WHAT IT DOES
- Takes as its parameter a function that loops its own iterable parameter and returns iterable
- Makes function split work of looping iterable (and doing whatever else the function does) into up to 15 threads
- Once all work completed, returns map object 

HOW IT WORKS
Just put "@async" (without the quotation marks) before the function that you want to multithread

TO DO
- Might be nice to add optimal max_workers parameter to change default of 15 max workers (threads)
