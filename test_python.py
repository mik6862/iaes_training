from traits.api import HasTraits,Int,Str,Button

from traitsui.api import View,Item

class Trait_example(HasTraits):

    a = Int(0)
    b = Str('CIAO')
    print_str = Button('PRINT')

    traits_view = View(Item('a',label='Int value'),
                       Item('b',label='The string'),
                       Item('print_str',show_label=False))


    def _print_str_fired(self):
        print self.b,self.a

    
if __name__ == '__main__':

    te = Trait_example()
    te.configure_traits()
