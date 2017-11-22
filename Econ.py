provinces = []


class Map:
    def __init__(self):
        self.provinces = []

    def add_province(self, name, pops, goods, neighbors):
        prov = Province(name, pops, goods, neighbors)
        self.provinces.append(prov)

        for neighbor in neighbors:
            neighbor.add_neighbor(self)

        return prov

    def get_province(self, index):
        if index > len(self.provinces) or index < 0:
            raise IndexError("Requested index out of bounds.")
        else:
            return self.provinces[index]

    def tick(self):
        pass


class Pop:
    def __init__(self, name, count):
        self.name = name
        self.count = int(count)


class Province:
    def __init__(self, name, pops, goods, neighbors):
        self.name = str(name)
        self.prov_id = len(provinces)
        self.pop_count = 0

        if isinstance(pops, list):
            self.pops = pops
            for pop in pops:
                self.pop_count += pop.count
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

    def add_pop(self, pop):
        self.pops.append(pop)
        self.pop_count += pop.count

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __str__(self):
        """

        | Province Name | Province ID | Province Pop Count | Province Neighbor Count |

        :return: above
        """

        s = "| " + self.name.ljust(13) + " | " + str(self.prov_id).zfill(7) + " | " + str(self.pop_count).zfill(9)
        s = s + " | " + str(len(self.neighbors)).zfill(2).rjust(9) + " |"

        return s

        # return "Province " + self.name + ", prov_id " + str(self.prov_id) + "\nPops: " + str(self.pops) + \
        #        "\nGoods: " + str(self.goods) + "\nNeighbors: " + str(self.neighbors)

    def __repr__(self):
        return "Province " + self.name + ", prov_id " + str(self.prov_id) + "\nPops: " + str(self.pops) + \
               "\nGoods: " + str(self.goods) + "\nNeighbors: " + str(self.neighbors)


class Good:
    def __init__(self, name, supply):
        self.name = name
        self.supply = supply
