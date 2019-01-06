from nose.tools import *
from ex14.ex14 import *

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_push():
    colors = DLList()
    colors.push('apple')
    colors.push('banana')
    colors.push('canada')
    colors.push('duck')

def test_pop():
    colors = DLList()
    assert colors.pop() == None
    colors.push('apple')
    assert colors.pop() == 'apple'
    colors.push('banana')
    colors.push('canada')
    assert colors.pop() == 'canada'
    colors.push('duck')
    assert colors.pop() == 'duck'
    colors.dump()

