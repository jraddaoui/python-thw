from nose.tools import *
import NAME

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    text = "Hello word!"
    NAME.print_stuff(text)
