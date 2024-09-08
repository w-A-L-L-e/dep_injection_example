#!/usr/bin/env python

# Author:       Walter Schreppers
# Description:  Tiny metaclass example. 
#               The meta class needs to derive from type
class Meta(type):
    def __new__(cls, class_name, base_classes, attrs):
        print(f'{cls=}, {class_name=}, {base_classes=}, {attrs=}')

        mod_attrs = {}
        for name, val in attrs.items():
            if name.startswith('__'): # dunder method we leave alone
                mod_attrs[name] = val
            else:
                # change method name to uppercase
                mod_attrs[name.upper()] = val

        return type(class_name, base_classes, mod_attrs)

# The using class derives from Meta like so and thus gets modifications from above Meta
class Square(metaclass = Meta):
    x=5
    y=10
    width=8

    def area(self):
        return f"AREA = {self.WIDTH * self.WIDTH}"


def main():
    # because we used the custom metaclass now all locals and methods are uppercase
    # apart from the performance hit you probably get when doing this, in this case our linting in editor will also 
    # wrongly start to give warnings etc. In any case it's not encouraged to use meta classes unless you really have no other
    # alternative (and most of the time you do...)
    sqr = Square()

    # so we use WIDTH instead of width and AREA instead of area and this works because our metaclass changed it in mod_attrs above
    print("WIDTH = ", sqr.WIDTH)
    print(sqr.AREA())


if __name__ == '__main__':
    main()
