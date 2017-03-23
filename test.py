# test.py
#
# AUTHOR
# ---------
# Jhonatan S. Oliveira
# oliveira@uregina.ca
# Department of Computer Science
# University of Regina
# Canada
#
#
# DESCRIPTION
# -----------
# This runs all the main functions for the search algorithm implementations.
# The tests are not formal and are not checked.
# This is only a simple way of visualizing outputs and trying different settings for running the implementations.

from csp_generator import generate_csp
from csp_inference import arc_consistency, backtrack

# Test generate_csp
n = 5
p = 0.2
alpha = 0.9
r = 0.2
print()
print("*** Testing: generate_csp ***")
variables, domains, constrains = generate_csp(n, p, alpha, r)
print(variables)
print(domains)
print(constrains)
print("*** --- End Testing: generate_csp ***")
print()

# Test arc consistency
print()
print("*** Testing: arc_consistency ***")
variables = [0, 1, 2, 3, 4]
domains = {0: [0, 1, 2, 3], 1: [0, 1, 2, 3], 2: [0, 1, 2, 3], 3: [0, 1, 2, 3], 4: [0, 1, 2, 3]}
constrains = {(4, 3): [(3, 2), (2, 1), (3, 1), (1, 1), (2, 1), (2, 2), (2, 1), (2, 1), (0, 1), (1, 3), (0, 3), (1, 2)], (1, 3): [(3, 3), (0, 2), (3, 0), (0, 0), (2, 3), (1, 3), (2, 1), (1, 3), (0, 2), (0, 1), (1, 2), (0, 3)], (2, 0): [(1, 2), (2, 1), (2, 0), (3, 0), (3, 0), (0, 0), (3, 2), (3, 2), (0, 2), (1, 1), (1, 3), (1, 3)]}
print("---> Before AC")
print(variables)
print(domains)
print(constrains)
print("---> After AC")
result = arc_consistency(variables, domains, constrains)
print(result)
print(variables)
print(domains)
print(constrains)
print("*** --- End Testing: arc_consistency ***")
print()



# Test backtrack
print()
print("*** Testing: backtrack ***")
variables = [0, 1, 2, 3, 4]
domains = {0: [0, 1, 2, 3], 1: [0, 1, 2, 3], 2: [0, 1, 2, 3], 3: [0, 1, 2, 3], 4: [0, 1, 2, 3]}
constrains = {(4, 3): [(3, 2), (2, 1), (3, 1), (1, 1), (2, 1), (2, 2), (2, 1), (2, 1), (0, 1), (1, 3), (0, 3), (1, 2)], (1, 3): [(3, 3), (0, 2), (3, 0), (0, 0), (2, 3), (1, 3), (2, 1), (1, 3), (0, 2), (0, 1), (1, 2), (0, 3)], (2, 0): [(1, 2), (2, 1), (2, 0), (3, 0), (3, 0), (0, 0), (3, 2), (3, 2), (0, 2), (1, 1), (1, 3), (1, 3)]}
result = backtrack({}, variables, domains, constrains)
print(result)
print("*** --- End Testing: backtrack ***")
print()


# Test backtrack
print()
print("*** Testing: backtrack with Forward Checking ***")
variables, domains, constrains = generate_csp(n, p, alpha, r)
result = backtrack({}, variables, domains, constrains, inf_type="FC")
print(result)
print("*** --- End Testing: backtrack ***")
print()

# Test backtrack
print()
print("*** Testing: backtrack with MAC ***")
variables, domains, constrains = generate_csp(n, p, alpha, r)
result = backtrack({}, variables, domains, constrains, inf_type="MAC")
print(result)
print("*** --- End Testing: backtrack ***")
print()
