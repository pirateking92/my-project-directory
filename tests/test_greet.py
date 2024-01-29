from lib.greet import *

def test_greet_says_hello_name():
    result = greet("Matt")
    assert result == "hello, Matt!"