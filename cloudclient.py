import random
from dwave.cloud import Client

with Client.from_config() as client:
    print("client.token\t\t", client.token)
    print("client.get_solvers()\t\t", client.get_solvers())
    print("client.get_solver()\t\t", client.get_solver())
    print()


# Connect using the default or environment connection information
with Client.from_config() as client:

    # Load the default solver
    print("Load the default solver")
    solver = client.get_solver()
    print(solver)

    # Build a random Ising model to exactly fit the graph the solver supports
    linear = {index: random.choice([-1, 1]) for index in solver.nodes}
    quad = {key: random.choice([-1, 1]) for key in solver.undirected_edges}

    # Send the problem for sampling, include solver-specific parameter 'num_reads'
    computation = solver.sample_ising(linear, quad, num_reads=100)

    # Print the first sample out of a hundred
    print(computation.samples[0])

