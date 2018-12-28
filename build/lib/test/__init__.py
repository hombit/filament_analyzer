def test():
    from . import unittests
    import unittest

    suite = unittest.TestSuite()
    suite.addTest(unittests.test_suite())

    return suite
