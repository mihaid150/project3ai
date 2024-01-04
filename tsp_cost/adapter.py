import re
def modify_domain_pddl(file_name):
    """
    modify_domain_pddl will append the rest of the PDDL code to domain.pddl in order to have cost implementation.
    This function also checks if the required modifications are already present.
    """

    functions_section = "\n\t(:functions\n\t\t(distance ?from- - city ?to - city) - number\n\t\t(total-cost) - number)\n"

    with open(file_name, 'r') as file:
        domain_pddl_content = file.read()

    # Check if modifications are already present
    if ":action-costs" in domain_pddl_content:
        print("':action-costs' is already present in the requirements.")
    else:
        # Adding ":action-costs" to ":requirements"
        domain_pddl_content = domain_pddl_content.replace(
            "(:requirements :strips :typing)",
            "(:requirements :strips :typing :action-costs)")

    if "(distance ?from- - city ?to - city) - number" in domain_pddl_content:
        print("Functions section is already present.")
    else:
        # Adding ":functions" section after the closing of ":predicates"
        insert_position = domain_pddl_content.find(")\n\t(:action")
        domain_pddl_content = domain_pddl_content[:(insert_position + 1)] + functions_section + domain_pddl_content[(insert_position + 1):]

    if "(increase (total-cost) (distance ?from- ?to))" in domain_pddl_content:
        print(":effect modification in :action move is already present.")
    else:
        # Modifying ":effect" in ":action move"
        domain_pddl_content = domain_pddl_content.replace(
            ":effect (and (not (current ?from-)) (current ?to) (visited ?to))",
            ":effect (and (not (current ?from-)) (current ?to) (visited ?to) (increase (total-cost) (distance ?from- ?to)))")

    with open(file_name, 'w') as file:
        file.write(domain_pddl_content)

    print("Modifications applied successfully.")


def modify_problem_pddl(problem1_file_name, distances_file_name):
    # Read the original problem1.pddl content
    with open(problem1_file_name, 'r') as file:
        problem1_content = file.read()

    # Find the last connected statement using regex
    last_connected_match = re.search(r'\(connected [^\)]+\)\s*\)', problem1_content)
    if last_connected_match:
        last_connected_index = last_connected_match.end() - 1

        # Read the distances from distances.txt and format them for PDDL
        distances_str = "\n\t\t(= (total-cost) 0)"
        with open(distances_file_name, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 3:
                    # Format each line as a distance assertion in PDDL
                    distances_str += f"\n\t\t(= (DISTANCE {parts[0]} {parts[1]}) {parts[2]})"

        # Insert the distances and total-cost initialization after the last connected statement
        problem1_content = (problem1_content[:last_connected_index] + distances_str +
                            "\n\t" + problem1_content[last_connected_index:])

        last_visited_match = re.search(r'\(visited \w+\)\)\)', problem1_content)
        if last_visited_match:
            last_visited_index = last_visited_match.end()

            # Insert the metric minimize statement before the last visited statement
            metric_str = "\n\t(:metric minimize (total-cost))"
            problem1_content = (problem1_content[:last_visited_index] + metric_str +
                                problem1_content[last_visited_index:])


    else:
        print("No connected statements found.")

    # Write the modified content back to problem1.pddl
    with open(problem1_file_name, 'w') as file:
        file.write(problem1_content)

    print("problem1.pddl has been updated with distance data and cost metric.")


# Call the function with appropriate file names



