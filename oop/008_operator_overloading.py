class Rational:

    def __init__(self, p=1, q=1) -> None:
        self.p = p
        self.q = q

    def __add__(self, other):
        s = Rational()
        s.p = self.p * other.q + self.q * other.p
        s.q = self.q * other.q
        return s
    
    def __str__(self):
        return f"{self.p} / {self.q}"


r1 = Rational(2, 3)
r2 = Rational(3, 4)
# res = r1.__add__(r2)
res = r1 + r2
print(f"{r1.p} / {r1.q} + {r2.p} / {r2.q} = {res.p} / {res.q}")
print(f"{r1} + {r2} = {res}")
