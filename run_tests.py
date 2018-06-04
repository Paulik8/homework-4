# -*- coding: utf-8 -*-

import unittest

#from test_mikegus import TestsMikeGus
#from tests import Tests
from tests_privacy import TestsPrivacy
#from test_johnkeats97 import TestsBaseSettings


if __name__ == '__main__':
    #suite = unittest.TestSuite((unittest.makeSuite(Tests)),)
    #suite2 = unittest.TestSuite((unittest.makeSuite(TestsMikeGus)))
    #suite3 = unittest.TestSuite((unittest.makeSuite(TestsPrivacy)))
    suite = unittest.TestSuite((
        #unittest.makeSuite(TestsMikeGus),
        #unittest.makeSuite(Tests),
        unittest.makeSuite(TestsPrivacy),
        #unittest.makeSuite(TestsBaseSettings),
    ))
    result = unittest.TextTestRunner().run(suite)
