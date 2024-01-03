from processes_manager import run_py2pddl_parse, run_py2pddl_init, run_fast_downward

# run only once at the creation of the class
# run_py2pddl_init("tsp_basic.py", "TravellingSalesmanBasic", "city", "visited connected current", "move")

#run_py2pddl_parse("tsp_basic.py")
run_fast_downward()

