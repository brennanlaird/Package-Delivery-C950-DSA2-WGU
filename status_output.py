'''
This module is used to output the package status given a particular time.
It writes the time and the package status to a text file.
The time used can be changed in the calling code.
'''



def print_status(trigger_time, pack_table, truck, trigger1, trigger2, trigger3):
    # print(trigger_time)
    status_list = []

    pc = 1
    while pc < 41:
        status_list.append(pack_table.searchPackage(pc))
        pc += 1

    # print(status_list)

