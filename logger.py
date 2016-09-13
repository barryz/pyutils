#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: barryz
@email: barryzxb@gmail.com
"""

import os.path
import logging
import traceback
from logging import DEBUG, WARNING, ERROR, INFO


class Logger(object):
    show_source_location = True
    level_map = {
        "DEBUG": DEBUG,
        "WARNING": WARNING,
        "ERROR": ERROR,
        "INFO": INFO
    }

    def _raw_log(self, logfn, message, exc_info):
        cname = ""
        loc = ""
        fn = ""
        tb = traceback.extract_stack()
        if len(tb) > 2:
            if self.show_source_location:
                loc = '(%s:%d):' % (os.path.basename(tb[-3][0]), tb[-3][1])
            fn = tb[-3][2]
            if fn != '<module>':
                if self.__class__.__name__ != Logger.__name__:
                    fn = self.__class__.__name__ + "." + fn
                fn += "()"

        logfn(loc + cname + fn + ": " + message, exc_info=exc_info)

    def info(self, message, exc_info=False):
        self._raw_log(logging.info, message, exc_info)

    def debug(self, message, exc_info=False):
        self._raw_log(logging.debug, message, exc_info)

    def warning(self, message, exc_info=False):
        self._raw_log(logging.warning, message, exc_info)

    def error(self, message, exc_info=False):
        self._raw_log(logging.error, message, exc_info)

    def basicConfig(self, level="DEBUG", logfile="/tmp/test.log"):
        level = self.level_map[level]
        logging.basicConfig(level=level,
                            format='%(asctime)s,%(msecs)03d %(levelname)s %(message)s',
                            filename=logfile,
                            filemode="a",
                            datefmt='%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    logger = Logger()
    logger.basicConfig(level="INFO", logfile="./test.log")
    logger.warning("it is called", exc_info=False)
