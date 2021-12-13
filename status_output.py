'''
This module is used to output the package status given a particular time.
It writes the time and the package status to a text file.
The time used can be changed in the calling code.
'''
import testCode


def print_status(trigger_time, pack_table):
    print(trigger_time)
    testCode.package_print(pack_table)
