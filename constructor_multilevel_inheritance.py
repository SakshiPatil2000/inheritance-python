class A:
    def __init__(self):
        print("A init")
        
class B(A):
    def __init__(self):
        super().__init__()
        print("B init")
        
class C(B):
    def __init__(self):
        super().__init__()
        print("C init")
        
obj = C()