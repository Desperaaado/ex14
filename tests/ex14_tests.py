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
    # assert colors.pop() == None
    colors.push('apple')
    assert colors.pop() == 'apple'
    colors.push('banana')
    colors.push('canada')
    assert colors.pop() == 'canada'
    colors.push('duck')
    assert colors.pop() == 'duck'

def test_remove():
    colors = DLList()
    colors.push('apple')
    assert colors.remove('apple') == 0
    colors.push('banana')
    colors.push('canada')
    colors.push('duck')
    assert colors.remove('duck') == 2

def test_first():
    colors = DLList()
    colors.push('apple')
    assert colors.first() == 'apple'
    colors.push('banana')
    colors.push('canada')
    colors.push('duck')
    assert colors.first() == 'apple'

def test_last():
    colors = DLList()
    colors.push('apple')
    assert colors.last() == 'apple'
    colors.push('banana')
    colors.push('canada')
    colors.push('duck')
    assert colors.last() == 'duck'

def test_get():
    colors = DLList()
    colors.push('apple')
    assert colors.get(1) == None
    colors.push('banana')
    colors.push('canada')
    colors.push('duck')
    assert colors.get(2) == 'canada'

def test_count():
    colors = DLList()
    colors.push('apple')
    assert colors.count() == 1
    colors.push('banana')
    colors.push('canada')
    colors.push('duck')
    assert colors.count() == 4

def test_shift():
    colors = DLList()
    colors.push('apple')
    colors.shift('banana')
    colors.push('canada')
    colors.shift('duck')
    result = colors.dump('silence')
    answer = ['duck', 'banana', 'apple', 'canada']
    assert result == answer

def test_unshift():
    colors = DLList()
    colors.push('apple')
    colors.push('banana')
    colors.push('canada')
    assert colors.unshift() == 'apple'
    result = colors.dump('silence')
    answer = ['banana', 'canada']
    assert result == answer