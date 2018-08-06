import timeit
import random
testlist = [random.randrange(1, 200) for _ in range(100)]
t = timeit.Timer("testlist.index(n)", "from __main__ import testlist,n")
for n in testlist:
	print("{}: ".format(n), t.timeit(number=1000), "miliseconds")
