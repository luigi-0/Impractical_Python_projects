"""importing in pseudonums.py to see how the __name__ and __main__ variables work."""
from pseudonyms import main

"""By using __name__ and __main__ setup here is what is going on:

__name__: 
Is a built-in variable that allows python to know whether a program
is being run by itself, or as an imported module.

"__main__":
Is a hard-coded string that is set by python as a program gets run.

Process:
When you run pseudonyms.py by itself, before executing any code python
will set __name__ = "__main__"

this means that 
if __name__ == "__main__":
    main()
will evaluate to TRUE and the body will get executed

When you import pseudonyms.py as module python will set __name__ = "main"

this means that if __name__ == "__main__" will evaluate to FALSE and   
nothing will happen in name_generator until you call main() 

This type of setup is really only useful when its one module that you are
importing. This looks like a nice setup to have if your're unit testing.
"""
main()
