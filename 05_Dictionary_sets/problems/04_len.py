
a = set();
a.add(20);
a.add(20.0); # it is not included in the set
a.add('20');
print(a)
print(len(a))