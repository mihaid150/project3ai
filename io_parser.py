import re


def parse_fast_downward_output(output):
    # Regular expressions for different parts of the output
    plan_length_pattern = re.compile(r'Plan length: (\d+)')
    plan_cost_pattern = re.compile(r'Plan cost: (\d+)')
    expanded_states_pattern = re.compile(r'Expanded (\d+) state\(s\)')
    search_time_pattern = re.compile(r'Search time: ([\d.]+)s')
    total_time_pattern = re.compile(r'Total time: ([\d.]+)s')
    planner_time_pattern = re.compile(r'Planner time: ([\d.]+)s')

    # Extracting data using regular expressions
    plan_length_match = plan_length_pattern.search(output)
    plan_cost_match = plan_cost_pattern.search(output)
    expanded_states_match = expanded_states_pattern.search(output)
    search_time_match = search_time_pattern.search(output)
    total_time_match = total_time_pattern.search(output)
    planner_time_match = planner_time_pattern.search(output)

    # Parsing extracted data
    plan_length = int(plan_length_match.group(1)) if plan_length_match else None
    plan_cost = int(plan_cost_match.group(1)) if plan_cost_match else None
    expanded_states = int(expanded_states_match.group(1)) if expanded_states_match else None
    search_time = float(search_time_match.group(1)) if search_time_match else None
    total_time = float(total_time_match.group(1)) if total_time_match else None
    planner_time = float(planner_time_match.group(1)) if planner_time_match else None

    # Extracting steps
    steps_start = output.find('Actual search time')
    steps_end = output.find('Plan length', steps_start)
    steps = output[steps_start:steps_end].strip().split('\n')[1:-1] if steps_start != -1 and steps_end != -1 else []

    return {
        "steps": steps,
        "plan_length": plan_length,
        "plan_cost": plan_cost,
        "expanded_states": expanded_states,
        "search_time": search_time,
        "total_time": total_time,
        "planner_time": planner_time
    }
