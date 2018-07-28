class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        # clientが使っても良い
        pass

    def _unsafe_method(self):
        # clientは使うべきでは無い
        pass

print("Hello. World!")
print(200)
print(200.1)

print(type("Hello, World"))
print(type(200))
print(type(200.1))
