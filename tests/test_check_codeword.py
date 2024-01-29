from lib.check_codeword import *

def test_correct_check_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

    # close_res = check_codeword("")

"""
If the codeword is wrong
Returns "WRONG!"
"""
def test_wrong_codeword():
    result = check_codeword("poopoo")
    assert result == "WRONG!"
        
"""
If the codeword get the first and last letter
correct
Returns "Close, but nope."
"""

def test_close_codeword():
    result = check_codeword("hoe")
    assert result == "Close, but nope."