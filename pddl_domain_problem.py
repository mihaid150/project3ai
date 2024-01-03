# demo for a basic case with domain and problem

from pddl.logic import Predicate, constants, variables
from pddl.core import Domain, Problem
from pddl.action import Action
from pddl.formatter import domain_to_string, problem_to_string
from pddl.requirements import Requirements


class PDDL:

    def __init__(self):
        # Variables and constants
        self.x, self.y, self.z = variables("x y z", types=["type_1"])
        self.a, self.b, self.c = constants("a b c", type_="type_1")

        # Predicates
        self.p1 = Predicate("p1", self.x, self.y, self.z)
        self.p2 = Predicate("p2", self.x, self.y)

        # Domain and problem
        self.domain = self.create_domain()
        self.problem = self.create_problem()

    def create_actions(self):
        a1 = Action(
            "action-1",
            parameters=[self.x, self.y, self.z],
            precondition=self.p1(self.x, self.y, self.z) & ~self.p2(self.y, self.z),
            effect=self.p2(self.y, self.z)
        )
        return [a1]

    def create_domain(self):
        requirements = [Requirements.STRIPS, Requirements.TYPING]
        return Domain("my_domain",
                      requirements=requirements,
                      types={"type_1": None},
                      constants=[self.a, self.b, self.c],
                      predicates=[self.p1, self.p2],
                      actions=self.create_actions())

    def create_problem(self):
        requirements = [Requirements.STRIPS, Requirements.TYPING]
        return Problem(
            "problem-1",
            domain=self.domain,
            requirements=requirements,
            objects=[],
            init=[self.p1(self.a, self.b, self.c), ~self.p2(self.b, self.c)],
            goal=self.p2(self.b, self.c)
        )

    def get_domain(self):
        return domain_to_string(self.domain)

    def get_problem(self):
        return problem_to_string(self.problem)
