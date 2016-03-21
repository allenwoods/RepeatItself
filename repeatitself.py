# Author: Allen Woods
# Date: 2016-03-21

import os
import sys


def repeat(itself):
    src = open(itself).read()
    print(src)


if __name__ == '__main__':
    cwd = os.getcwd()
    itself = os.path.join(cwd, sys.argv[0])
    repeat(itself)
