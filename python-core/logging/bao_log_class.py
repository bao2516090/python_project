# -*- coding:utf-8 -*-
import os
import logging
import ctypes

FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01  # text color contains blue.
FOREGROUND_GREEN = 0x02  # text color contains green.
FOREGROUND_RED = 0x04  # text color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN

STD_OUTPUT_HANDLE = -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)


def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

class My_Logger:
    def __init__(self, path, Clevel = logging.DEBUG, Flevel = logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

        # 设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(Clevel)

        # 设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)

        # 添加handler到logger中
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message, color =FOREGROUND_GREEN):
        set_color(color)
        self.logger.info(message)

    def warn(self, message, color=FOREGROUND_YELLOW):
        set_color(color)
        self.logger.warn(message)

    def error(self, message, color=FOREGROUND_RED):
        set_color(color)
        self.logger.error(message)

    # def cri(self, message):
    #     self.logger.critical(message)

if __name__=="__main__":
    logger = My_Logger('log_class.log', logging.DEBUG, logging.DEBUG)
    logger.debug("debug messsage")
    logger.info("info message")
    logger.warn("warn message")
    logger.error("error message")
    # logger.cri("critical message")