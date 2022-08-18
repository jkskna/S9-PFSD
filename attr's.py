class cse:
    def__init__(self, id, name, cgpa):
    self.id = id
    self.name = name
    self.cgpa = cgpa


s = cse(10, "ABC", 9.5)
print(getattr(s, "name"))

setattr(s, "cgpa", 9.4)
print(getattr(s, "cgpa"))

delattr(s, "cgpa")
print(getattr(s, "cgpa"))

print(hasattr(s, "id"))
