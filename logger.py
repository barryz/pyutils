#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: barryz
@mail: barryzxb@gmail.com
"""

import logging


def set_logger(level="DEBUG", filename="options.log", logger="root"):
    """
        Args:
        level: string
        filename: absolute path of the log file
    """
    log_level_map = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARN,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }
    logger_f = logging.getLogger(logger)
    logger_f.setLevel(logging.DEBUG)
    fh = logging.FileHandler(filename)
    fh.setLevel(log_level_map.get(level, logging.DEBUG))
    formatter = logging.Formatter("%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    logger_f.addHandler(fh)
    return logger_f


if __name__ == "__main__":
    logger = set_logger(level="INFO", filename="./test.log", logger="mytest")
    logger.info("info test")
    logger.critical("critical test")
