from py2pddl import Domain, create_type
from py2pddl import predicate, action, goal, init


class TravellingSalesmanCostDomain(Domain):
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


class TravellingSalesmanCostProblem(TravellingSalesmanCostDomain):

    def __init__(self):
        super().__init__()
        self.cities = TravellingSalesmanCostDomain.City.create_objs(["AB", "AR", "AG", "BC", "BH", "BN", "BT", "BV",
                                                                     "BR", "B", "BZ", "CS", "CL", "CJ", "CT", "CV",
                                                                     "DB", "DJ", "GL", "GR", "GJ", "HR", "HD", "IL",
                                                                     "IS", "IF", "MM", "MH", "MS", "NT", "OT", "PH",
                                                                     "SM", "SJ", "SB", "SV", "TR", "TM", "TL", "VS",
                                                                     "VL", "VN"])

    @init
    def init(self) -> list:
        data = [
            self.current(self.cities["TM"]), self.visited(self.cities["TM"]),
            self.connected(self.cities["TM"], self.cities["AR"]),
            self.connected(self.cities["TM"], self.cities["HD"]),
            self.connected(self.cities["TM"], self.cities["CS"]),

            self.connected(self.cities["AR"], self.cities["TM"]),
            self.connected(self.cities["AR"], self.cities["HD"]),
            self.connected(self.cities["AR"], self.cities["AB"]),
            self.connected(self.cities["AR"], self.cities["BH"]),

            self.connected(self.cities["BH"], self.cities["AR"]),
            self.connected(self.cities["BH"], self.cities["AB"]),
            self.connected(self.cities["BH"], self.cities["CJ"]),
            self.connected(self.cities["BH"], self.cities["SJ"]),
            self.connected(self.cities["BH"], self.cities["SM"]),

            self.connected(self.cities["SM"], self.cities["BH"]),
            self.connected(self.cities["SM"], self.cities["SJ"]),
            self.connected(self.cities["SM"], self.cities["MM"]),

            self.connected(self.cities["MM"], self.cities["SM"]),
            self.connected(self.cities["MM"], self.cities["SJ"]),
            self.connected(self.cities["MM"], self.cities["CJ"]),
            self.connected(self.cities["MM"], self.cities["BN"]),
            self.connected(self.cities["MM"], self.cities["SV"]),

            self.connected(self.cities["SJ"], self.cities["SM"]),
            self.connected(self.cities["SJ"], self.cities["BH"]),
            self.connected(self.cities["SJ"], self.cities["CJ"]),
            self.connected(self.cities["SJ"], self.cities["MM"]),

            self.connected(self.cities["CJ"], self.cities["SJ"]),
            self.connected(self.cities["CJ"], self.cities["BH"]),
            self.connected(self.cities["CJ"], self.cities["AB"]),
            self.connected(self.cities["CJ"], self.cities["MS"]),
            self.connected(self.cities["CJ"], self.cities["BN"]),
            self.connected(self.cities["CJ"], self.cities["MM"]),

            self.connected(self.cities["AB"], self.cities["CJ"]),
            self.connected(self.cities["AB"], self.cities["BH"]),
            self.connected(self.cities["AB"], self.cities["AR"]),
            self.connected(self.cities["AB"], self.cities["HD"]),
            self.connected(self.cities["AB"], self.cities["VL"]),
            self.connected(self.cities["AB"], self.cities["SB"]),
            self.connected(self.cities["AB"], self.cities["MS"]),

            self.connected(self.cities["HD"], self.cities["AB"]),
            self.connected(self.cities["HD"], self.cities["AR"]),
            self.connected(self.cities["HD"], self.cities["TM"]),
            self.connected(self.cities["HD"], self.cities["CS"]),
            self.connected(self.cities["HD"], self.cities["GJ"]),
            self.connected(self.cities["HD"], self.cities["VL"]),

            self.connected(self.cities["CS"], self.cities["HD"]),
            self.connected(self.cities["CS"], self.cities["TM"]),
            self.connected(self.cities["CS"], self.cities["MH"]),
            self.connected(self.cities["CS"], self.cities["GJ"]),

            self.connected(self.cities["MH"], self.cities["CS"]),
            self.connected(self.cities["MH"], self.cities["GJ"]),
            self.connected(self.cities["MH"], self.cities["DJ"]),

            self.connected(self.cities["DJ"], self.cities["MH"]),
            self.connected(self.cities["DJ"], self.cities["GJ"]),
            self.connected(self.cities["DJ"], self.cities["VL"]),
            self.connected(self.cities["DJ"], self.cities["OT"]),

            self.connected(self.cities["GJ"], self.cities["DJ"]),
            self.connected(self.cities["GJ"], self.cities["MH"]),
            self.connected(self.cities["GJ"], self.cities["CS"]),
            self.connected(self.cities["GJ"], self.cities["HD"]),
            self.connected(self.cities["GJ"], self.cities["VL"]),

            self.connected(self.cities["VL"], self.cities["GJ"]),
            self.connected(self.cities["VL"], self.cities["HD"]),
            self.connected(self.cities["VL"], self.cities["AB"]),
            self.connected(self.cities["VL"], self.cities["SB"]),
            self.connected(self.cities["VL"], self.cities["AG"]),
            self.connected(self.cities["VL"], self.cities["OT"]),
            self.connected(self.cities["VL"], self.cities["DJ"]),

            self.connected(self.cities["SB"], self.cities["VL"]),
            self.connected(self.cities["SB"], self.cities["AB"]),
            self.connected(self.cities["SB"], self.cities["MS"]),
            self.connected(self.cities["SB"], self.cities["BV"]),
            self.connected(self.cities["SB"], self.cities["AG"]),

            self.connected(self.cities["MS"], self.cities["SB"]),
            self.connected(self.cities["MS"], self.cities["AB"]),
            self.connected(self.cities["MS"], self.cities["CJ"]),
            self.connected(self.cities["MS"], self.cities["BN"]),
            self.connected(self.cities["MS"], self.cities["SV"]),
            self.connected(self.cities["MS"], self.cities["HR"]),
            self.connected(self.cities["MS"], self.cities["BV"]),

            self.connected(self.cities["BN"], self.cities["MM"]),
            self.connected(self.cities["BN"], self.cities["CJ"]),
            self.connected(self.cities["BN"], self.cities["MS"]),
            self.connected(self.cities["BN"], self.cities["SV"]),

            self.connected(self.cities["SV"], self.cities["MM"]),
            self.connected(self.cities["SV"], self.cities["BN"]),
            self.connected(self.cities["SV"], self.cities["HR"]),
            self.connected(self.cities["SV"], self.cities["NT"]),
            self.connected(self.cities["SV"], self.cities["IS"]),
            self.connected(self.cities["SV"], self.cities["BT"]),

            self.connected(self.cities["HR"], self.cities["SV"]),
            self.connected(self.cities["HR"], self.cities["MS"]),
            self.connected(self.cities["HR"], self.cities["BV"]),
            self.connected(self.cities["HR"], self.cities["CV"]),
            self.connected(self.cities["HR"], self.cities["BC"]),
            self.connected(self.cities["HR"], self.cities["NT"]),

            self.connected(self.cities["BV"], self.cities["MS"]),
            self.connected(self.cities["BV"], self.cities["SB"]),
            self.connected(self.cities["BV"], self.cities["AG"]),
            self.connected(self.cities["BV"], self.cities["DB"]),
            self.connected(self.cities["BV"], self.cities["PH"]),
            self.connected(self.cities["BV"], self.cities["BZ"]),
            self.connected(self.cities["BV"], self.cities["CV"]),
            self.connected(self.cities["BV"], self.cities["HR"]),

            self.connected(self.cities["AG"], self.cities["BV"]),
            self.connected(self.cities["AG"], self.cities["SB"]),
            self.connected(self.cities["AG"], self.cities["VL"]),
            self.connected(self.cities["AG"], self.cities["OT"]),
            self.connected(self.cities["AG"], self.cities["TR"]),
            self.connected(self.cities["AG"], self.cities["DB"]),

            self.connected(self.cities["OT"], self.cities["DJ"]),
            self.connected(self.cities["OT"], self.cities["VL"]),
            self.connected(self.cities["OT"], self.cities["AG"]),
            self.connected(self.cities["OT"], self.cities["TR"]),

            self.connected(self.cities["TR"], self.cities["OT"]),
            self.connected(self.cities["TR"], self.cities["AG"]),
            self.connected(self.cities["TR"], self.cities["DB"]),
            self.connected(self.cities["TR"], self.cities["GR"]),

            self.connected(self.cities["DB"], self.cities["AG"]),
            self.connected(self.cities["DB"], self.cities["BV"]),
            self.connected(self.cities["DB"], self.cities["PH"]),
            self.connected(self.cities["DB"], self.cities["IF"]),
            self.connected(self.cities["DB"], self.cities["B"]),
            self.connected(self.cities["DB"], self.cities["GR"]),
            self.connected(self.cities["DB"], self.cities["TR"]),

            self.connected(self.cities["GR"], self.cities["TR"]),
            self.connected(self.cities["GR"], self.cities["DB"]),
            self.connected(self.cities["GR"], self.cities["B"]),
            self.connected(self.cities["GR"], self.cities["CL"]),

            self.connected(self.cities["B"], self.cities["GR"]),
            self.connected(self.cities["B"], self.cities["IF"]),
            self.connected(self.cities["B"], self.cities["DB"]),
            self.connected(self.cities["B"], self.cities["CL"]),

            self.connected(self.cities["IF"], self.cities["B"]),
            self.connected(self.cities["IF"], self.cities["DB"]),
            self.connected(self.cities["IF"], self.cities["PH"]),
            self.connected(self.cities["IF"], self.cities["IL"]),
            self.connected(self.cities["IF"], self.cities["CL"]),

            self.connected(self.cities["PH"], self.cities["DB"]),
            self.connected(self.cities["PH"], self.cities["IF"]),
            self.connected(self.cities["PH"], self.cities["IL"]),
            self.connected(self.cities["PH"], self.cities["BZ"]),
            self.connected(self.cities["PH"], self.cities["BV"]),

            self.connected(self.cities["CV"], self.cities["BV"]),
            self.connected(self.cities["CV"], self.cities["HR"]),
            self.connected(self.cities["CV"], self.cities["BC"]),
            self.connected(self.cities["CV"], self.cities["VN"]),
            self.connected(self.cities["CV"], self.cities["BZ"]),

            self.connected(self.cities["BT"], self.cities["SV"]),
            self.connected(self.cities["BT"], self.cities["IS"]),

            self.connected(self.cities["NT"], self.cities["SV"]),
            self.connected(self.cities["NT"], self.cities["HR"]),
            self.connected(self.cities["NT"], self.cities["BC"]),
            self.connected(self.cities["NT"], self.cities["VS"]),
            self.connected(self.cities["NT"], self.cities["IS"]),

            self.connected(self.cities["IS"], self.cities["BT"]),
            self.connected(self.cities["IS"], self.cities["SV"]),
            self.connected(self.cities["IS"], self.cities["NT"]),
            self.connected(self.cities["IS"], self.cities["VS"]),

            self.connected(self.cities["BC"], self.cities["NT"]),
            self.connected(self.cities["BC"], self.cities["VS"]),
            self.connected(self.cities["BC"], self.cities["VN"]),
            self.connected(self.cities["BC"], self.cities["CV"]),
            self.connected(self.cities["BC"], self.cities["HR"]),

            self.connected(self.cities["VS"], self.cities["IS"]),
            self.connected(self.cities["VS"], self.cities["NT"]),
            self.connected(self.cities["VS"], self.cities["BC"]),
            self.connected(self.cities["VS"], self.cities["VN"]),
            self.connected(self.cities["VS"], self.cities["GL"]),

            self.connected(self.cities["VN"], self.cities["BC"]),
            self.connected(self.cities["VN"], self.cities["CV"]),
            self.connected(self.cities["VN"], self.cities["BZ"]),
            self.connected(self.cities["VN"], self.cities["BR"]),
            self.connected(self.cities["VN"], self.cities["GL"]),
            self.connected(self.cities["VN"], self.cities["VS"]),

            self.connected(self.cities["GL"], self.cities["VS"]),
            self.connected(self.cities["GL"], self.cities["VN"]),
            self.connected(self.cities["GL"], self.cities["BR"]),
            self.connected(self.cities["GL"], self.cities["TL"]),

            self.connected(self.cities["BZ"], self.cities["VN"]),
            self.connected(self.cities["BZ"], self.cities["CV"]),
            self.connected(self.cities["BZ"], self.cities["BV"]),
            self.connected(self.cities["BZ"], self.cities["PH"]),
            self.connected(self.cities["BZ"], self.cities["IL"]),
            self.connected(self.cities["BZ"], self.cities["BR"]),

            self.connected(self.cities["BR"], self.cities["GL"]),
            self.connected(self.cities["BR"], self.cities["VN"]),
            self.connected(self.cities["BR"], self.cities["BZ"]),
            self.connected(self.cities["BR"], self.cities["IL"]),
            self.connected(self.cities["BR"], self.cities["CT"]),
            self.connected(self.cities["BR"], self.cities["TL"]),

            self.connected(self.cities["TL"], self.cities["GL"]),
            self.connected(self.cities["TL"], self.cities["BR"]),
            self.connected(self.cities["TL"], self.cities["CT"]),

            self.connected(self.cities["IL"], self.cities["BR"]),
            self.connected(self.cities["IL"], self.cities["BZ"]),
            self.connected(self.cities["IL"], self.cities["PH"]),
            self.connected(self.cities["IL"], self.cities["IF"]),
            self.connected(self.cities["IL"], self.cities["CL"]),
            self.connected(self.cities["IL"], self.cities["BR"]),
            self.connected(self.cities["IL"], self.cities["CT"]),

            self.connected(self.cities["CL"], self.cities["CT"]),
            self.connected(self.cities["CL"], self.cities["IL"]),
            self.connected(self.cities["CL"], self.cities["B"]),
            self.connected(self.cities["CL"], self.cities["IF"]),
            self.connected(self.cities["CL"], self.cities["GR"]),

            self.connected(self.cities["CT"], self.cities["TL"]),
            self.connected(self.cities["CT"], self.cities["BR"]),
            self.connected(self.cities["CT"], self.cities["IL"]),
            self.connected(self.cities["CT"], self.cities["CL"]),
        ]
        return data

    @goal
    def goal(self) -> list:
        return [self.visited(self.cities["AB"]),
                self.visited(self.cities["AR"]),
                self.visited(self.cities["AG"]),
                self.visited(self.cities["BC"]),
                self.visited(self.cities["BH"]),
                self.visited(self.cities["BN"]),
                self.visited(self.cities["BT"]),
                self.visited(self.cities["BV"]),
                self.visited(self.cities["BR"]),
                self.visited(self.cities["B"]),
                self.visited(self.cities["BZ"]),
                self.visited(self.cities["CS"]),
                self.visited(self.cities["CL"]),
                self.visited(self.cities["CJ"]),
                self.visited(self.cities["CT"]),
                self.visited(self.cities["CV"]),
                self.visited(self.cities["DB"]),
                self.visited(self.cities["DJ"]),
                self.visited(self.cities["GL"]),
                self.visited(self.cities["GR"]),
                self.visited(self.cities["GJ"]),
                self.visited(self.cities["HR"]),
                self.visited(self.cities["HD"]),
                self.visited(self.cities["IL"]),
                self.visited(self.cities["IS"]),
                self.visited(self.cities["IF"]),
                self.visited(self.cities["MM"]),
                self.visited(self.cities["MH"]),
                self.visited(self.cities["MS"]),
                self.visited(self.cities["NT"]),
                self.visited(self.cities["OT"]),
                self.visited(self.cities["PH"]),
                self.visited(self.cities["SM"]),
                self.visited(self.cities["SJ"]),
                self.visited(self.cities["SB"]),
                self.visited(self.cities["SV"]),
                self.visited(self.cities["TR"]),
                self.visited(self.cities["TM"]),
                self.visited(self.cities["TL"]),
                self.visited(self.cities["VS"]),
                self.visited(self.cities["VL"]),
                self.visited(self.cities["VN"])]
