<<<<<<< Updated upstream
from pddl_domain_problem import PDDL
import subprocess
from io_parser import parse_fast_downward_output

pddl = PDDL()

# retrieve the domain and the problem
domain = pddl.get_domain()
problem = pddl.get_problem()

# Save the domain to a file named 'domain.pddl'
with open('tsp_basic_resources/domain.pddl', 'w') as domain_file:
    domain_file.write(domain)

# Save the problem to a file named 'problem.pddl'
with open('tsp_basic_resources/problem.pddl', 'w') as problem_file:
    problem_file.write(problem)
=======
from processes_manager import run_py2pddl_parse, run_py2pddl_init, run_fast_downward

# run only once at the creation of the class
# run_py2pddl_init("tsp_basic.py", "TravellingSalesmanBasic", "city", "visited connected current", "move")

#run_py2pddl_parse("tsp_basic.py")
run_fast_downward()

>>>>>>> Stashed changes

# Define the command to be executed
command = ["/home/mihai/tools/downward/fast-downward.py", "./domain.pddl", "./problem.pddl",
           "--heuristic", "h=ff()", "--search", "astar(h)"]

# Run the command
process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if the process was successful
if process.returncode == 0:
    print("Command executed successfully!")
    print(parse_fast_downward_output(process.stdout))
else:
    print("Error in command execution.")
    print("Error Output:\n", process.stderr)