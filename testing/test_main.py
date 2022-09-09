try:
    import AutoFeedback.varchecks as vc
except: 
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

import unittest
from main import *

class UnitTests( unittest.TestCase ): 
   def test_service_func(self):
      st_func = qn.edge2queue[0].service_f
      myvar = randomvar( 2, variance=4, nsamples=100 )
      assert( check_func( st_func, [(,)], [myvar] ) )
