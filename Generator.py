import random
from Persona import Persona
class Generator:
    def __init__(self, number_contacts, number_relations):
        self.__number_contacts = number_contacts
        self.__number_relations = number_relations
        self.__streets = []
        self.__names = []
        self.__append_nombres()
        self.__append_calles()
        self.__contacts = []
        self.gen_list_of_contacts()
        self._combinations = []
        self.gen_combinations()
    def __append_nombres(self):
        with open("nombres.txt", "r") as f:
            for name in f:
                self.__names.append(str(name).title().replace("\n", ""))

    def __append_calles(self):
        with open("calles.txt", "r") as f2:
            for calle in f2:
                self.__streets.append(str(calle).title().replace("\n", ""))

    def get_random_name(self):
        return random.choice(self.__names)

    def get_random_street(self):
        return random.choice(self.__streets)

    def get_random_number(self):
        return random.randint(10000,99999)

    def gen_list_of_contacts(self):
        for n in range(self.__number_contacts):
            self.__contacts.append(Persona(self.get_random_name(), self.get_random_number(), self.get_random_street()))

    def get_list_of_contacts(self):
        return self.__contacts
    def gen_combinations(self):
        for i in range(self.__number_contacts):
            for j in range(self.__number_contacts):
                if i != j and (j,i) not in self._combinations:
                    self._combinations.append((i,j))
        return self._combinations

    def get_combination(self):
        actual = random.choice(self._combinations)
        self._combinations.remove(actual)
        return actual

    def insert_relations(self,net):
        max_rel = self.__number_contacts * (self.__number_contacts - 1)
        if self.__number_relations <= max_rel:
            for i in range(self.__number_relations):
                net.insertaRelacion(*self.get_combination())
        else:
            raise Exception("Inserte menos relaciones")



if __name__ == '__main__':
    gdor = Generator(5,20)
    print(gdor.__names)
    print(gdor.get_combination())
    print(gdor._combinations)
