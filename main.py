from processes_manager import run_py2pddl_parse, run_py2pddl_init, run_fast_downward
from tsp_cost.adapter import modify_domain_pddl, modify_problem_pddl

# run only once at the creation of the class
# run_py2pddl_init("tsp_cost/tsp_cost.py", "TravellingSalesmanCost", "city", "visited connected current distance", "move")

run_py2pddl_parse("tsp_cost/tsp_cost.py")
modify_domain_pddl("domain.pddl")
modify_problem_pddl("problem.pddl", "tsp_cost/distances.txt")
run_fast_downward()
