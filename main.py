from processes_manager import run_py2pddl_init, run_py2pddl_parse, run_fast_downward

# retrieve the domain and the problem
domain = None
problem = None

# Save the domain to a file named 'domain.pddl'
with open('pddl_resources/domain.pddl', 'w') as domain_file:
    domain_file.write(domain)

# Save the problem to a file named 'problem.pddl'
with open('pddl_resources/problem.pddl', 'w') as problem_file:
    problem_file.write(problem)

