import sys
import pybindgen

def generate(file_):
    mod = pybindgen.Module('mymodule')
    mod.add_include('"my-module.hpp"')

    vec2 = mod.add_struct('vec2')
    vec2.add_instance_attribute('x', 'float')
    vec2.add_instance_attribute('y', 'float')
    vec2.add_constructor([pybindgen.param('float', 'x'), pybindgen.param('float', 'y')])

    line = mod.add_struct('segment')
    line.add_instance_attribute('a', 'vec2')
    line.add_instance_attribute('b', 'vec2')
    line.add_constructor([pybindgen.param('vec2', 'a'), pybindgen.param('vec2', 'b')])

    mod.add_container('std::vector<segment>', 'segment', 'list')
    mod.add_container('std::vector<vec2>', 'vec2', 'list')

    mod.add_function('MyModuleDoAction',
                     pybindgen.retval('std::vector<vec2>'),
                     [
                         pybindgen.param('vec2', 'xy'),
                         pybindgen.param('std::vector<segment>', 'segments')
                     ])
    mod.generate(file_)

if __name__ == '__main__':
    generate(sys.stdout)
