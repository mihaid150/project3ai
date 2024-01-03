
import subprocess
from io_parser import parse_fast_downward_output

# retrieve the domain and the problem
domain = None
problem = None

# Save the domain to a file named 'domain.pddl'
with open('domain.pddl', 'w') as domain_file:
    domain_file.write(domain)

# Save the problem to a file named 'problem.pddl'
with open('problem.pddl', 'w') as problem_file:
    problem_file.write(problem)

# Define the command to be executed
command = ["/home/mihai/tools/downward/fast-downward.py", "./domain.pddl", "./problem.pddl",
           "--heuristic", "h=ff()", "--search", "astar(h)"]

# Run the command
process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Check if the process was successful
if process.returncode == 0:
    print("Command executed successfully!")
    print(process.stdout)
else:
    print("Error in command execution.")
    print("Error Output:\n", process.stderr)