import Econ

Map = Econ.Map()

province = Map.add_province("Berlin", [], [], [])
Map.add_province("Potsdam", [], [], [province])

pop = Econ.Pop("German", 10)

province.add_pop(pop)

print("|-------------------------------------------------|")
print("| Province Name | Prov ID | Pop Count | Neighbors |")
print("|-------------------------------------------------|")
print(Map.get_province(0))
print("|-------------------------------------------------|")
print(Map.get_province(1))
print("|-------------------------------------------------|")
