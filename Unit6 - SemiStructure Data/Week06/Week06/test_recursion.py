def test_recursion(idx):
    print(idx)
    return 0 if idx == 0 else idx + test_recursion(idx - 1)

def infiniteloop():
    while 1 == 1:
        pass

infiniteloop()
#test_recursion(-10)
