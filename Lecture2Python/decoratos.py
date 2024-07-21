def announce(f):
   def wrapper():
      print("About to run the function...")
      f()
      print("The functions has been run.")
   return wrapper

@announce
def hello():
   print("Hello, World!")

hello()
