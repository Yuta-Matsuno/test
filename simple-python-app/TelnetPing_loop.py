import Telnet_test_M
import Ping_test_M
import time
import sys

args = sys.argv
counter = 0

while True:
    counter += 1
    test_class_1 = Telnet_test_M.Telnet()
    txt = test_class_1.test_method(args, args[2], args[3], args[4])
#    console = raw_input("Press 'show' if you want to watch the configuration:")
    test_class_2 = Ping_test_M.Telnet()
    test_class_2.test_method(args, args[1], args[2], args[3], args[4])
    if counter == 3:
            break
            
