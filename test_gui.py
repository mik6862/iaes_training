# -*- coding: utf-8 -*-
from traits.api import HasTraits,Float,Button
from traitsui.api import View,Item

class Calculator(HasTraits):

    a = Float(0)
    b = Float(0)
    c = Float(0)
    plus = Button('+')
    minus = Button('-')
    multiply = Button('*')
    divide = Button('/')
    traits_view = View(Item('a', label = 'First'),
                       Item('b', label = 'Second'),
                       Item('c', label = 'Result'),
                       Item('plus', show_label = False),
                       Item('minus', show_label = False),
                       Item('multiply', show_label = False),
                       Item('divide', show_label = False))

    def _plus_fired(self):
        self.c = self.a + self.b
        print self.c
        
    def _minus_fired(self):
        self.c = self.a - self.b
        print self.c
        
    def _multiply_fired(self):
        self.c = self.a * self.b
        print self.c
        
    def _divide_fired(self):
        self.c = self.a / self.b
        print self.c
          
if __name__ == '__main__':
   cl = Calculator()
   cl.configure_traits()