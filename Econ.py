provinces = []


def add_province(name, pops, goods, neighbors):
    prov = Province(name, pops, goods, neighbors)
    provinces.append(prov)
    return prov


class Pop:
    def __init__(self, name):
        self.name = name


class Province:
    def __init__(self, name, pops, goods, neighbors):
        self.name = str(name)
        self.prov_id = len(provinces)

        if isinstance(pops, list):
            self.pops = pops
        else:
            raise TypeError("Province init pop not list")

        if isinstance(goods, list):
            self.goods = goods
        else:
            raise TypeError("Province init goods not list")

        if isinstance(neighbors, list):
            self.neighbors = neighbors
        else:
            raise TypeError("Province init neighbors not list")

        provinces.append(self)

    def __str__(self):
        return "Province " + self.name + ", prov_id " + str(self.prov_id) + "\nPops: " + str(self.pops) + \
               "\nGoods: " + str(self.goods) + "\nNeighbors: " + str(self.neighbors)


class Good:
    def __init__(self, name, supply):
        self.name = name
        self.supply = supply