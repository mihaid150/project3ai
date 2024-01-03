from py2pddl import Domain, create_type
from py2pddl import predicate, action, goal, init


class TravellingSalesmanBasicDomain(Domain):
    City = create_type("City")

    @predicate(City)
    def visited(self, city):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(City, City)
    def connected(self, city1, city2):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(City)
    def current(self, city):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @action(City, City)
    def move(self, from_, to):
        precond = [self.current(from_), self.connected(from_, to), ~self.visited(to)]
        effect = [~self.current(from_), self.current(to), self.visited(to)]
        return precond, effect


class TravellingSalesmanBasicProblem(TravellingSalesmanBasicDomain):

    def __init__(self):
        super().__init__()
        self.cities = TravellingSalesmanBasicDomain.City.create_objs(["TM", "HD", "AB", "SB", "CJ", "BH", "MM"])

    @init
    def init(self) -> list:
        init_cond = [self.current(self.cities["TM"]), self.visited(self.cities["TM"]),
                     self.connected(self.cities["TM"], self.cities["HD"]),
                     self.connected(self.cities["HD"], self.cities["TM"]),
                     self.connected(self.cities["TM"], self.cities["BH"]),
                     self.connected(self.cities["BH"], self.cities["TM"]),
                     self.connected(self.cities["HD"], self.cities["AB"]),
                     self.connected(self.cities["AB"], self.cities["HD"]),
                     self.connected(self.cities["AB"], self.cities["SB"]),
                     self.connected(self.cities["SB"], self.cities["AB"]),
                     self.connected(self.cities["AB"], self.cities["CJ"]),
                     self.connected(self.cities["CJ"], self.cities["AB"]),
                     self.connected(self.cities["CJ"], self.cities["BH"]),
                     self.connected(self.cities["BH"], self.cities["CJ"]),
                     self.connected(self.cities["CJ"], self.cities["MM"]),
                     self.connected(self.cities["MM"], self.cities["CJ"]),
                     self.connected(self.cities["BH"], self.cities["MM"]),
                     self.connected(self.cities["MM"], self.cities["BH"]),
                     self.connected(self.cities["SB"], self.cities["CJ"]),
                     self.connected(self.cities["CJ"], self.cities["SB"]),
                     ]
        return init_cond

    @goal
    def goal(self) -> list:
        return [self.visited(self.cities["TM"]),
                self.visited(self.cities["HD"]),
                self.visited(self.cities["AB"]),
                self.visited(self.cities["SB"]),
                self.visited(self.cities["CJ"]),
                self.visited(self.cities["BH"]),
                self.visited(self.cities["MM"])]
