# -*- coding: utf-8 -*-

from controller.automataController import *
import time
from service.regexService import *
if __name__ == '__main__':
    t = time.time()
    dfa = NFAToDFA()
    simple_dfa(dfa)
    print "\nExecution time: ", time.time() - t, "seconds"
