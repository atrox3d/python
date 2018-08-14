#!/usr/bin/env python3

import unittest

from plusone import plusone

class PlusoneTest(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(plusone(-1 ), 0  )
        self.assertEqual(plusone(0 ),  1 )
        self.assertEqual(plusone(1 ),  2 )
        self.assertEqual(plusone(5 ),  6 )
        self.assertEqual(plusone(10),  11)
        self.assertEqual(plusone(20),  21)

if __name__ == "__main__": 
    unittest.main()


