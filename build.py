import os
import numpy as np
# See if Cython is installed
try:
    from Cython.Build import cythonize
# Do nothing if Cython is not available
except ImportError:
    # Got to provide this function. Otherwise, poetry will fail
    def build(setup_kwargs):
        pass
# Cython is installed. Compile
else:
    from setuptools import Extension
    from setuptools.dist import Distribution
    from distutils.command.build_ext import build_ext

    # This function will be executed in setup.py:
    def build(setup_kwargs):
        # The file you want to compile
        extensions = [
            Extension("betainc.betainc",
                sources=["betainc/betainc.pyx"],
                libraries=["m"],
                include_dirs=[np.get_include()], # Unix-like specific
                extra_compile_args = ["-O3","-ffast-math",'-fopenmp'],
                extra_link_args=['-fopenmp']
                )

        ]

        # gcc arguments hack: enable optimizations
        os.environ['CFLAGS'] = '-O3'

        # Build
        setup_kwargs.update({
            'ext_modules': cythonize(
                extensions,
                language_level=3,
                compiler_directives={'linetrace': False},
            ),
            'cmdclass': {'build_ext': build_ext}
        })