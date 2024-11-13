from collections import deque
def is_valid_state(state, X, Y):
    """Check if the state is within the jug capacities."""
    return 0 <= state[0] <= X and 0 <= state[1] <= Y
def bfs(X, Y, Z):
    """Perform BFS to find the steps to get exactly Z liters in one of the jugs."""
    visited = set()
    queue = deque([(0, 0)])  
    parent = {}  
    operations = {}
    while queue:
        a, b = queue.popleft()
        if a == Z or b == Z:
            path = []
            while (a, b) != (0, 0):
                path.append((a, b, operations[(a, b)]))
                a, b = parent[(a, b)]
            path.append((0, 0, "Start"))
            path.reverse()
            return path
        if (a, b) in visited:
            continue
        visited.add((a, b))
        next_states = [
            (X, b, "Fill Jug 1"),  # Fill jug 1
            (a, Y, "Fill Jug 2"),  # Fill jug 2
            (0, b, "Empty Jug 1"),  # Empty jug 1
            (a, 0, "Empty Jug 2"),  # Empty jug 2
            (0,a+b, "Pour water from Jug 1 to Jug 2"),  # Pour jug 1 -> jug 2
            (a+b,0, "Pour water from Jug 2 to Jug 1"),  # Pour jug 2 -> jug 1
            (X,b-(X-a),"Pour water from Jug 2 to Jug 1 unitl Jug 1 is full"),
            (a-(Y-b),Y,"Pour water from Jug 1 to Jug 2 unitl Jug 2 is full")
        ]
        for state in next_states:
            new_state = state[:2]
            operation = state[2]
            if is_valid_state(new_state, X, Y) and new_state not in visited:
                queue.append(new_state)
                parent[new_state] = (a, b)
                operations[new_state] = operation
    return None  
def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == "exit":
            print("Exiting the program.")
            exit()
        try:
            value = int(user_input)
            if value > 0:
                return value
            elif value == 0:
                print("Jug Capacity can't be ZERO.")
            else:
                print("Jug Capacity can't be Negative.")
        except ValueError:
            print("Invalid input. Please enter a number.")
def water_jug_problem():
    X = get_integer_input("Enter the capacity of Jug 1: ")
    Y = get_integer_input("Enter the capacity of Jug 2: ")
    Z = get_integer_input("Enter the target amount of water: ")
    if Z > max(X, Y):
        print("No solution possible since target is greater than both jug capacities.")
        return
    solution = bfs(X, Y, Z)
    if solution:
        c=0
        print(f"\nSteps to get exactly {Z} liters:")
        for step in solution:
            c+=1
            print(f"Step{c}: {step[2]} \n      ({step[0]},{step[1]}) ")
        print("Solution found to fill the jugs.")
    else: 
        print("No solution exists for the given inputs.")
water_jug_problem()