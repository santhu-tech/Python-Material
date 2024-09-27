def my_decorator(say_hello):
	def wrapper():
	    print("something is happening before func call")
	    say_hello() # call the function
	    print("something is happening after func call")
@my_decorator
def say_hello():  #decorated fun
	print("Hello")
say_hello() #calling decorated fun
