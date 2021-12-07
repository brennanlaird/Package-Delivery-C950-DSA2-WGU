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