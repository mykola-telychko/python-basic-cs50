from script46 import hello 

def test_hello1():
    hello("David") == "hi, Dava"

def test_hello2():
    assert hello("David") == "hello, David"
    assert hello() == "hi, "

def test_argument(): 
    assert hello("David") == "hi, David"
    