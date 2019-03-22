import inspect, os
print inspect.getfile(inspect.currentframe()) # script filename (usually with path)
thisFile = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory
print thisFile

import sys
sys.path.append(thisFile)
from Analyze_V1 import learn