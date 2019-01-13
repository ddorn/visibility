#!/usr/bin/env python
import os
from distutils.core import setup, Extension
from mymodulegen import generate

try:
    os.mkdir("build")
except OSError:
    pass
module_fname = os.path.join("build", "my-module-binding.cpp")
with open(module_fname, "wt") as file_:
    print("Generating file {}".format(module_fname))
    generate(file_)

mymodule = Extension('mymodule',
                     sources = [module_fname, 'my-module.cpp'],
                     include_dirs=['.'])

setup(name='Visibility',
      version="0.0",
      description='binding to trylock visibility algorithm',
      author='ddorn',
      ext_modules=[mymodule],
     )

