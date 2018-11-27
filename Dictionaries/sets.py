example = set()

example.add(43)
example.add(False)
example.add(3.123)
example.add("Thorium")
example.add(43)
print(example)
len(example)
example.remove(43)
print(example)
# example.remove(50) This raises an error if it does not exist in the set
help(example.discard())
example.discard(50)
example2 = set([1, 2, 3, "one"])

example2.clear()

odd = set([1,3,5,7,9])
even = set([2,4,6,8,10])
prime = set([2,3,5,7])
composite = set([4,6,8,9,10])

odd.union(even)
even.union(odd)
odd.intersection(prime)
prime.intersection(even)
even.intersection(odd)
prime.union(composite)
2 in prime
6 in odd
9 not in even
dir(prime)