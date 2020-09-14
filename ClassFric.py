#import numpy as np

class Friction():
    '''This is a docstring. I have created a new friction class'''
    def __init__(self, fric=1):
        self.friction = fric
    def __float__(self):
        return self.friction 
#    def Print(self):
 #       x = int(self.friction)
  #      while x < 5:
   #         self.outputs = x + 1

