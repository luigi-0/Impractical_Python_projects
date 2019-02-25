"""Profiling the palingrams program."""

"""
Profiling is the art of optimizing your scripts so that they run faster
and are more efficient.

Here, we use a built in C extension to create a profile of the palingrams script.
Profiling involves creating runtime statistics for the entire script, but cProfile
allows you to also see a more detailed breakdown of how to program is being run.

Running this script in the terminal is the better way to go since you can kick out
the profile in a text file.

Another way to profile is using Python's time module. I will do this seperately.
"""

import cProfile
import palingrams
cProfile.run('palingrams.find_palingrams()')
