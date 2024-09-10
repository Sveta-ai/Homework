my_dict={"Egor":2012,"Liza":1997,"Kolya":2005}
print(my_dict)
print(my_dict["Liza"])
my_dict["Inna"]= 1960
print(my_dict)
my_dict.update({"Vova":1961,
                "Yna":1969})
print(my_dict)
a=my_dict.pop("Kolya")
print(a)


my_set={3,4,5,6,7,4,6,1,(1,3,5),"Anna","Olya","Anna","Sveta"}
print(my_set)
my_set.add(8)
print(my_set)
my_set.update([2,9])
print(my_set)
my_set.remove(5)
print(my_set)
my_set.remove("Olya")
print(my_set)


