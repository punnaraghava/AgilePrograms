from hello import greet,add
def test_greet(): assert greet("Amar") == "Hello, Amar!"
def test_add():
    print("Adding Vaues...")
    assert add(2, 3) == 5