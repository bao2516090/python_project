# -*- coding:utf-8 -*-
# -----------------------1.简单使用-------------------------
#导入logging模块
# import logging
#
# #设置显示级别，高于INFO的信息才会输出
# logging.basicConfig(level=logging.INFO)
#
# #创建logger实例
# logger = logging.getLogger("root")

#设置logger的信息
# logger.info("Start xiaobao's Logging...")
# messages = {"name":"xiaobao","age":25}
# logger.debug("I am debug...")
# logger.info("xiaobao's messgae：%s", messages)
#
# import Llogging.bao_log_mod
#
# logger.info("Finish Logging...")

# -----------------------2.日志保存到文件中------------------
#
import logging
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
#
# # 创建Filter handler
# handler = logging.FileHandler("hello.log")
# handler.setLevel(logging.INFO)
#
# # 创建日志格式format
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
#
# logger.addHandler(handler)
# logger.info("log has output to file")

# ------------------------3.采用配置文件的方式------------------
# import logging
# import logging.config
#
# logging.config.fileConfig("logging.conf")
#
# logger = logging.getLogger("test")
#
# # 设置输出的信息
# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warning message")
# logger.error("error message")
# logger.critical("critical message")

# ------------------------4.多模块使用logging---------------------
# import logging
# import logging.config
#
# logging.config.fileConfig("logging.conf")
# test_logger = logging.getLogger("test")
#
# test_logger.debug("GraphServer Is Started......")
#
# import Logging.bao_log_mod

# ----------------------5.大型项目中构建logging类---------------------
import logging
from Logging.bao_log_class import My_Logger

logobj = My_Logger('class_log.log',logging.DEBUG,logging.DEBUG)
logobj.debug("debug message")
logobj.info("info message")
logobj.warn("warn message")
logobj.error("error message")