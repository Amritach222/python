import logging
logging.basicConfig(filename = "test.log", level = logging.DEBUG)#需要指定filename和level，不然无法输出


logging.exception("11111111")


import os
print (os.name)
print(os.path.abspath('.'))