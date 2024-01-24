# Why we use Logging?>>>>> to find error and critical issues with time
#Where to use ? >>> On Server
#logging have 5 Levels
# critical 50
# error    40
# warning  30
# info     20
# debug    10
#___________________________________________________________________

import logging

logging.basicConfig()

logging.critical("Critical Msg")
logging.error("  ERROR Msg ")
logging.warning("warning Msg")
logging.info("info Msg")
logging.debug("debug Msg")

#Here Note if we run logging.basicConfig() it will take only 1st 3 levels i.e 50 40 30

# if we want all levels we need to use level number or level name 
