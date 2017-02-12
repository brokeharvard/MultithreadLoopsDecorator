import concurrent.futures as cf

### MULTITHREADING DECORATOR ###

def async(function): 
	def wrapped_function(*iterable):
		with cf.ThreadPoolExecutor(max_workers=15) as executor: 
			results = executor.map(function, *iterable) # This is a map object 
			#results = [result for result in executor.map(function, *iterable)] # Use this if you prefer 
				# function to return a list (but really no need to convert map object into list, because
				# map object is iterable)
		return results
	return wrapped_function


'''

### WHAT? ###

- The decorator takes as its parameter: a function that loops its own iterable parameter and returns an iterable.
- The decorator makes the function split the work of looping its iterable (and doing whatever else the function does) into up to 15 threads.
- Once all the work is complete, the decorated function returns a map object.

### HOW? ###

Just put "@async" (without the quotation marks) before the function that you want to multithread

### TO DO ###

- Might be nice to add optimal max_workers parameter to change default of 15 max workers (threads)

'''
