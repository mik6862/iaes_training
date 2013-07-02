__author__ = 'kostua'

from traits.api import HasTraits, Float, Button
from traitsui.api import Item, Group, View, HGroup, VGroup


class test_gui(HasTraits):
    a = Float()
    b = Float()
    r = Float()
    plus = Button(label='+')
    minus = Button(label='-')
    multi = Button(label='*')
    sub = Button(label='/')

    values = VGroup(Item('a', label='First'),
                    Item('b', label='Second'),
                    Item('r', label='Result'),
                    label='Data',
                    show_border=True)

    buttons = HGroup(Item('plus', show_label=False),
                     Item('minus', show_label=False),
                     Item('multi', show_label=False),
                     Item('sub', show_label=False),
                     label='Buttons',
                     show_border=True)

    main_gr = Group(values, buttons)

    view = View(main_gr,
                title='Simple calulator')

    def _plus_fired(self):
        self.r = self.a + self.b

    def _minus_fired(self):
        self.r = self.a - self.b

    def _multi_fired(self):
        self.r = self.a * self.b

    def _sub_fired(self):
        try:
            self.r = self.a / self.b
        except Exception:
            self.r = 0.0

    def __init__(self):
        self.configure_traits()


if __name__ == "__main__":
    test_gui()


