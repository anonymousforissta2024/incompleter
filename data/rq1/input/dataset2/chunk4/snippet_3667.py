#Source: https://stackoverflow.com/questions/54243287/using-cythonized-code-causing-typeerror-hasattr-attribute-name-must-be-stri
from distutils.core import setup
from distutils.extension import Extension
import os
import sys

from Cython.Build import cythonize
from Cython.Distutils import build_ext
from Cython.Compiler import Options

Options.emit_code_commments = False
Options.generate_cleanup_code = True


TOP_DIR = "root"
NAME = "root"
PACKAGES = [
"root",
]
INCLUDE = []

file_ending = ".py"
COMPILE_ARGS = ["-O3", "-Wall"]
LINK_ARGS = ["-g"]


def get_extensions(directory):
    extensions = list()

    for f in os.listdir(directory):
        path = os.path.join(directory, f)
        if os.path.isfile(path) and path.endswith(file_ending):
            path_split = os.path.split(path)

            ext_name = path_split[0].replace(os.path.sep, ".")

            module_name = path_split[1][:-len(file_ending)]
            if module_name != "__init__":
                ext_name += "." + str(module_name)


            extensions.append(
                Extension(
                    ext_name,
                    [
                        path,
                    ],
                    include_dirs=[
                        ".",
                    ],
                    extra_compile_args=COMPILE_ARGS,
                    extra_link_args=LINK_ARGS,
                )
            )
        elif os.path.isdir(path):
            extensions.extend(get_extensions(path))

    return extensions


# Build Extension objects
extensions = get_extensions(TOP_DIR)

# Do setup
setup(
    name=NAME,
    packages=PACKAGES,
    ext_modules=cythonize(
        extensions,
        compiler_directives={
            "language_level": "3",
        },
    ),
    include_dirs=INCLUDE,
    cmdclass={
        "build_ext": build_ext,
    },
)