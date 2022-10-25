s = set()
s.add(1)
s.add(2)
print(type(s))
print(s)

intersectionSet = s.intersection({1, 2, 3, 4, 5})  # it checks up the other set and execute along that data
unionSet = s.union({1, 2, 3, 4, 5, 6, 7, 8})  # creates a new set.

isDisJoint = {2, 4}
print(s.isdisjoint(isDisJoint))

print(intersectionSet)
print(unionSet)

