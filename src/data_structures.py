# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:47:56 2018

@author: I329986
"""

class Node:
    def __init__ (self, data):
        self.value = data
        self.next = None;
class LL:
    def __init__(self):
        self.headval = None
    def addToLL(self, node):
        if self.headval == None:
            self.headval = node
        else:
            node.next=self.headval
            self.headval= node
    def removeFromLL(self):
        if self.headval == None :
            print( "Linked List is empty. No nodes in it to remove")
        else:
            self.headval = self.headval.next;
    def printLL (self):
        nodeTemp = self.headval
        if(nodeTemp == None):
            print( "Linked List is empty. No nodes in it to print")
        while nodeTemp is not None:
            print(nodeTemp.value +"  ")
            nodeTemp = nodeTemp.next;

node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
linkedList = LL()
linkedList.addToLL(node1)
linkedList.addToLL(node2)
linkedList.addToLL(node3)

print("Linkded List")
linkedList.printLL()

print("Poped from Linkded List")

linkedList.removeFromLL()
linkedList.printLL()

linkedList.removeFromLL()

print("Poped from Linkded List")

linkedList.printLL()

linkedList.removeFromLL()

print("Poped from Linkded List")


linkedList.printLL()

linkedList.removeFromLL()


        