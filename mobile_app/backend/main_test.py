from main import *
import unittest
import json
from flask import Flask, jsonify, Response

class TestMain(unittest.TestCase):
    def test_get_hello(self):
        self.assertEqual(get_hello(), 'Hello World!')

    def test_get_total(self):
        self.assertEqual(get_total(2,3,20,10), '6.6')

    
if __name__=='__main__':
    unittest.main()