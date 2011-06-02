﻿# -*- coding: utf-8 -*-

#TODO:  wywoływanie update_node_status() gdy wszystkie bezpożrednie podzbiory są częste

min_supp_count = 1

class Node:
    def __init__(self, item, level, position):
        self.item = item
        self.counter = 0
        self.branches = {}
        self.large = None
        self.suspected = None
        self.large_subsets_counter = 0
        self.level = level
        self.beginning_position = position
        self.first_pass = True
        if level == 1:
            self.large = False
            self.suspected = True

    def increment(self, transaction, position):
        
        if position > self.beginning_position:
            self.first_pass = False
        if position == self.beginning_position and not self.first_pass:
            self.suspected = False
        finished = True
        
        if self.suspected:
            self.counter += 1
            if(self.large != True and self.counter >= min_supp_count):
                self.large = True
        if self.suspected != None and len(transaction) > 0:
            for i in range(len(transaction)):
               finished = finished and self.branches.setdefault(transaction[i], Node(transaction[i], self.level + 1, position)).increment(transaction[i+1:], position)
        return finished and self.suspected == False

    def print_node(self):
        for key in self.branches:
            for i in range(self.level):
                print "\t",
            print "%s: [%d, %s, %s]" % (key, self.branches[key].counter, self.branches[key].suspected, self.branches[key].large)
            self.branches[key].print_node()

    def update_node_status(self):
        self.large = False
        self.suspected = True


class Root(Node):
    def __init__(self):
        self.counter = 0
        self.branches = {}
        self.large = True
        self.suspected = False
        self.position = 0;
        self.level = 0
    
    def get_large_sets(self):
        large_sets = {}
        return large_sets
        


tree = Root()
tr = ['A', 'B', 'C']
