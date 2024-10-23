import time
from importlib import reload

# load 1st time
import test_module
time.sleep(20)
# reload 
reload(test_module)
time.sleep(20) 

 # reload again  
reload(test_module)
print("This is test file..")