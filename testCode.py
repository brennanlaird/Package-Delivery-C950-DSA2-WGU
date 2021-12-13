'''
This module contains functions used to test the output of the main program.
The code is separated out into this module to keep the main program readable.
'''

from packHash import *
from packClass import *
from graphClass import *
from truckClass import *
from distanceLookup import *


def graph_print(graph):
    print("Graph Adjaceny List:")
    print(graph.adjacency_list)
    print("Graph Edge Weight List:")
    print(graph.edge_weights)


def dictionary_print(dictionary):
    print("The Address Dictionary:")
    for i in dictionary:
        print(i, " ", dictionary.get(i))


def package_print(packtable):
    print("The Package List:")
    pc = 1
    while pc < 41:
        print(packtable.searchPackage(pc))
        pc += 1

def package_deadline(packtable, pc):
    # Create a list of packages to be loaded based on a nested set of functions
    i = 1

    loaded_list = []

    # Search through the package table for a 9 AM delivery
    while i <= pc:
        cp = packtable.searchPackage(i)
        if cp[5] == '9:00 AM':
            loaded_list.append(cp)
            # packtable.insertPackage
            ad_id = cp[10]
            same_address(packtable, pc, ad_id)
        i += 1
    print(loaded_list)
    # If a 9 AM delivery is found, search for packages with the same address

    # if a same address is found, check the restrictions

def same_address(packtable, pc, id):

    j = 1
    while j <= pc:
        cp = packtable.searchPackage(j)
        if id == cp[10]:
            print("Same address for for package id", cp)
        j += 1