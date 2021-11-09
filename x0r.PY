from z3 import *
a2, a3, a4 = BitVecs('a2 a3 a4', 64)
s = Solver() # tao ra mang rong 
s.add(a2 - a3 == 2225223423)
s.add(a3 + a4 == 4201428739)
s.add(a2 - a4 == 1121399208)
if s.check() == sat:
    m = s.model()
    # dua cac gia tri vao mang thong qua s.model()
    for index in m:
        print("%s = %ld" % (index, m[index].as_long()))
