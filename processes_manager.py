import subprocess
from io_parser import parse_fast_downward_output


def run_py2pddl_init(file_name, domain_problem_name, types, predicates, actions):
    # Define the command and inputs
    command = ["python3", "-m", "py2pddl.init", file_name]
    inputs = [
        domain_problem_name + "\n",  # Name input followed by newline
        types + "\n",  # Types input followed by newline
        predicates + "\n",  # Predicates input followed by newline
        actions + "\n"  # Actions input followed by newline
    ]

    # Start the subprocess and get the stdin, stdout, stderr
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True)

    # Send the inputs to the process and get the output
    output, error = process.communicate(input="".join(inputs))

    # Check for errors
    if process.returncode != 0:
        print(f"Error: {error}")
    else:
        print(f"Output: {output}")


def run_py2pddl_parse(file_name):
    # Define the command
    command = ["python3", "-m", "py2pddl.parse", file_name]

    # Start the subprocess and get the stdin, stdout, stderr
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Wait for the process to finish and get the output and error
    output, error = process.communicate()

    # Check for errors
    if process.returncode != 0:
        print("Error in command execution.")
        print("Error Output:\n", error)
    else:
        print("Command executed successfully!")
        print("Output:\n", output)


def run_fast_downward():
    # Define the command to be executed
    command = ["/home/mihai/tools/downward/fast-downward.py", "./domain.pddl",
               "./problem.pddl", "--heuristic", "h=ff()", "--search", "astar(h)"]

    # Run the command
    process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Check if the process was successful
    if process.returncode == 0:
        print("Command executed successfully!")
        print(parse_fast_downward_output(process.stdout))
    else:
        print("Error in command execution.")
