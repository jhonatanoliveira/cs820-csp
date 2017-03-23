# csp_generator.py
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
# A model for generating CSPs is implemented here.
# We focus on generating CSPs that are binary, for simplicity.
# Binary CSP instances should be randomly generated using the model RB proposed in [1].
# The choice of this model is motivated by the fact that it has exact phase transition and the ability to generate asymptotically hard instances.
#
#
# REFERENCES
# ----------
# [1] K. Xu and W. Li. Exact Phase Transitions in Random Constraint Satisfaction Problems. Journal of Artificial Intelligence Research, 12:93–103, 2000.
#
#
# IMPLEMENTATION STRUCTURES
# -------------------------
# A CSP is described by variables, its domain, and constrains in the variable's domain.
# Each variable is represented by a number.
# For example, a CSP with 3 variables has the following structure:
#   [0, 1, 2]
# The domain of variable is also represented by numbers.
# For instance, the domain of variable 0 is formed by the following 2 values:
#   [0, 1]
# Binary constrains are a list of tuples with values from variables that are not acceptable.
# All constrains are saved in a dictionary where the keys indicate the couple of variables involved.
# For example, constrains between variables 0 and 1 and between variables 2 and 3 can be described as follows:
#   {
#        (0,1): [(0,1), (1,2)],
#        (1,2): [(1,0), (2,2)]
#   }


from math import log, pow
from random import choice

def generate_csp(n, p, alpha, r):
  """
  Description
  -----------
  A binary random CSP instance generator following the Model RB from [1].
  The inputs are n, p, alpha and r where n is the number of variables, p (0 < p < 1) is the constraint tightness, and r and alpha (0 < r, alpha < 1) are two positive constants used by the model RB.

  Example
  -------
  >>> n = 5
  >>> p = 0.7
  >>> alpha = 0.9
  >>> r = 0.2
  >>> variables, domains, constrains = generate_csp(n, p, alpha, r)
  [0, 1, 2, 3, 4]
  {0: [0, 1, 2, 3], 1: [0, 1, 2, 3], 2: [0, 1, 2, 3], 3: [0, 1, 2, 3], 4: [0, 1, 2, 3]}
  {(2, 1): [(2, 3), (0, 1), (0, 3), (3, 2), (1, 1), (1, 2), (2, 2), (0, 3), (0, 0), (2, 1), (1, 3), (3, 0)], (0, 3): [(1, 2), (1, 3), (0, 1), (3, 2), (3, 3), (0, 1), (0, 1), (3, 1), (2, 1), (1, 1), (2, 0), (0, 1)], (3, 4): [(1, 1), (0, 2), (2, 2), (1, 2), (2, 3), (1, 3), (3, 0), (1, 0), (1, 3), (0, 3), (2, 0), (2, 1)]}

  References
  ----------
  [1] K. Xu and W. Li. Exact Phase Transitions in Random Constraint Satisfaction Problems. Journal of Artificial Intelligence Research, 12:93–103, 2000.
  """

  # STEP 0
  # Compute variables of the CSP
  variables = range(0,n)
  # Compute domain of each variable
  d = round( pow(n,alpha) ) # domain size of each variable
  domains = {}
  for var in variables:
    domains[var] = list(range(0,d))

  # STEP 1
  # Compute quantity of constrains
  constrains_qnt = round( r * n * log(n) )
  # Select 2 variables for each constrain, without repetition
  var_constrains = []
  while len(var_constrains) <= constrains_qnt:
    var1, var2 = (choice(variables), choice(variables))
    # make sure we select a new unique pair of variables
    if (var1 != var2) and (not (var1,var2) in var_constrains) and (not (var2,var1) in var_constrains):
      var_constrains.append((var1,var2))

  # STEP 2
  # Compute quantity of incompatible pairs of values
  incomp_qnt = round( p * (pow(d,2)) )
  # Select pair of incompatible values
  constrains = {}
  # For each constrain
  for var1, var2 in var_constrains:
    incomp_values = []
    while len(incomp_values) <= incomp_qnt:
      val1, val2 = (choice(domains[var1]), choice(domains[var2]))
      # make sure we select a new unique pair of variables
      if (not (val1,val2) in incomp_values) or (not (val2,val1) in incomp_values):
        incomp_values.append((val1,val2))
    constrains[(var1, var2)] = incomp_values

  # Return full CSP
  return list(variables), domains, constrains
