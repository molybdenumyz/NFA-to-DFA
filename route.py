# -*- coding: utf-8 -*-

from controller.automataController import *
import time
from service.regexService import *
if __name__ == '__main__':

    dfa = NFAToDFA()
    t = time.time()
    simple_dfa(dfa)
    print "\nExecution time: ", time.time() - t, "seconds"
