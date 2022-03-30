import sys
import numpy as np
from timeit import default_timer as timer

sys.setrecursionlimit(15000)


class Node:
    def __init__(self, key, color ="red"):
        self.key = key
        self.left = None
        self.right = None
        self.dad = None
        self.color = color

class ARN:
    def __init__(self):
        self.nil = Node(key="T.nil", color="black")
        self.root = self.nil

    def setRoot(self, key):
        self.root = Node(key)

    def insert(self, key):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if key <= x.key:
                x = x.left
            else:
                x = x.right
        node = Node(key)
        node.dad = y
        if y == self.nil:
            self.root = node
        elif key <= y.key:
            y.left = node
        else:
            y.right = node
        node.left = self.nil
        node.right = self.nil
        self.fixup(node)

    def fixup(self, current_node):
        while current_node.dad.color == "red":
            if current_node.dad == current_node.dad.dad.left:
                y = current_node.dad.dad.right
                if y.color == "red":
                    current_node.dad.color = "black"
                    y.color = "black"
                    current_node.dad.dad.color = "red"
                    current_node = current_node.dad.dad
                else:
                    if current_node == current_node.dad.right:
                        current_node = current_node.dad
                        self.left_rotate(current_node)
                    current_node.dad.color = "black"
                    current_node.dad.dad.color = "red"
                    self.right_rotate(current_node.dad.dad)
            else:
                y = current_node.dad.dad.left
                if y.color == "red":
                    current_node.dad.color = "black"
                    y.color = "black"
                    current_node.dad.dad.color = "red"
                    current_node = current_node.dad.dad
                else:
                    if current_node == current_node.dad.left:
                        current_node = current_node.dad
                        self.right_rotate(current_node)
                    current_node.dad.color = "black"
                    current_node.dad.dad.color = "red"
                    self.left_rotate(current_node.dad.dad)
        self.root.color = "black"

    def left_rotate(self, current_node):
        y = current_node.right
        current_node.right = y.left
        if y.left is not self.nil:
            y.left.dad = current_node
        y.dad = current_node.dad
        if current_node.dad is self.nil:
            self.root = y
        elif current_node == current_node.dad.left:
            current_node.dad.left = y
        else:
            current_node.dad.right = y
        y.left = current_node
        current_node.dad = y

    def right_rotate(self, current_node):
        y = current_node.left
        current_node.left = y.right
        if y.right is not self.nil:
            y.right.dad = current_node
        y.dad = current_node.dad
        if current_node.dad is self.nil:
            self.root = y
        elif current_node == current_node.dad.left:
            current_node.dad.left = y
        else:
            current_node.dad.right = y
        y.right = current_node
        current_node.dad = y

    def find(self, key):
        return self.findNode(self.root, key)

    def findNode(self, current_node, key):
        if current_node is self.nil:
            return False
        elif key < current_node.key:
            return self.findNode(current_node.left, key)
        else:
            return self.findNode(current_node.right, key)

    def inorder(self):
        def _inorder(v):
            if v is self.nil:
                return
            if v.left is not self.nil:
                _inorder(v.left)
            if v.right is not self.nil:
                _inorder(v.right)

        _inorder(self.root)


def crea_casualmente(abr, n):
    for x in range(0, n):
        abr.insert(np.random.randint(1,100))
        abr.inorder()


def crea_ordinati(abr, n):
    for x in range(0, n):
        abr.insert(x)
