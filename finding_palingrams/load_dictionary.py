"""Load a text file as a list

Arguments:
-text file name (and directory path, if needed)

Exceptions:
-IOError if filename not found.

Returns:
-A list of all words in a text file in lower case.

Requires-import.sys

"""
import sys

# When importing any external file it is best practice to place
# the execution in a try/except block so that you can catch
# errors before the script runs.

# Using the with statement will ensure that the file is closed
# once you the nested block of code is executed.

# You can also name specific error codes in the except statement
# and if the error matches then the except block will get run

def load(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file),
              file=sys.stderr)
        sys.exit(1)
