import Econ

province = Econ.Province("Test", [], [], [])
Econ.add_province("Test", [], [], [province])
print(Econ.provinces[0])
print(Econ.provinces[1])
