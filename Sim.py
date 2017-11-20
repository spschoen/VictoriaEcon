import Econ

province = Econ.Province("Test", [], [], [])
Econ.add_province("Test", [], [], [province])

pop = Econ.Pop("German", 10)

province.add_pop(pop)

print("|-------------------------------------------------|")
print("| Province Name | Prov ID | Pop Count | Neighbors |")
print("|-------------------------------------------------|")
print(Econ.provinces[0])
print("|-------------------------------------------------|")
print(Econ.provinces[1])
print("|-------------------------------------------------|")
