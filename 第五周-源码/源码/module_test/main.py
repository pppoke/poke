__author__ = "Alex Li"
# import module_alex
#module_alex=all_code   module_alex.name module_alex.logger()
import sys,os
print(sys.path)

x=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(x)
print(sys.path)
import module_alex
import package_test
package_test.test1.test()
module_alex.say_hello()
