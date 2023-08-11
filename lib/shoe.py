#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size = ''):
        self.brand = brand
        self.size = size

    def set_size(self):
        return self._size
    
    def get_size(self, size):
        if type(size) != int:
            print("size must be an integer")
        else: 
            self._size = size
    
    size = property(set_size, get_size)
    def cobble(self):
        print("Your shoe is as good as new!")

    condition = "New"
