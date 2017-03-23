# main.py
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
# This script is a utility for running all implemented search algorithms.
# After calling the script in a prompt command, the user can input constants and pick a search algorithm.
# For more details, please, see documentation in the README file.


from csp_generator import generate_csp
from csp_inference import backtrack, arc_consistency


def main():
  """
  Description
  -----------
  Shows a menu to the user.
  User can input constants used by the model RB.
  User can pick a search algorithm for solving the CSP.
  See README file for more details.
  
  Example
  -------
  >>> main()
  >>> Initial state (comma separated):
  --> 1,2,3,8,5,6,7,4,0
  >>> Choose the Search algorithm
  >>> 1) Depth First
  >>> 2) Breath First
  >>> 3) Best First - tiles out of place
  >>> 4) Best First - min moves
  >>> 5) Best First - heuristic H
  --> 3
  >>> Result:
  [[1, 2, 3, 8, 5, 6, 7, 4, 0], [1, 2, 3, 8, 5, 0, 7, 4, 6], [1, 2, 3, 8, 0, 5, 7, 4, 6], [1, 2, 3, 8, 5, 6, 7, 0, 4], [1, 2, 0, 8, 5, 3, 7, 4, 6], [1, 2, 3, 8, 0, 6, 7, 5, 4], [1, 2, 3, 8, 4, 5, 7, 0, 6], [1, 0, 3, 8, 2, 5, 7, 4, 6], [1, 2, 3, 0, 8, 5, 7, 4, 6], [1, 2, 3, 8, 5, 6, 0, 7, 4], [1, 2, 3, 8, 4, 5, 7, 6, 0], [1, 2, 3, 8, 6, 0, 7, 5, 4], [1, 0, 2, 8, 5, 3, 7, 4, 6], [1, 0, 3, 8, 2, 6, 7, 5, 4], [1, 2, 3, 0, 8, 6, 7, 5, 4], [1, 2, 3, 8, 4, 5, 0, 7, 6], [1, 2, 3, 8, 4, 0, 7, 6, 5], [1, 2, 3, 8, 0, 4, 7, 6, 5]]
  >>> Want to try again? (Y/N)
  -->
  """

  keep_running = True

  while keep_running:

    # Input constants
    print()
    print()
    print(">>> !!! Starting Assignment 2 Solution !!! <<<")
    print()
    print(">>> Constants:")
    n = int(input("--> Number of variables (n): "))
    p = float(input("--> Constraint Tightness (p): "))
    alpha = float(input("--> Constant alpha: "))
    r = float(input("--> Constant r: "))
    print()

    # Using AC or not
    print()
    print(">>> Do you wish to run Arc-Consistency before backtrack?")
    use_ac_str = input("--> (y/n): ")
    print()
    use_ac = False
    if (use_ac_str == "y") or (use_ac_str == "Y") or (use_ac_str == "yes") or (use_ac_str == "Yes") or (use_ac_str == "YES"):
      use_ac = True

    # Shows options
    print()
    print(">>> Choose the Search algorithm")
    print(">>> 1) Backtrack Search")
    print(">>> 2) Backtrack Search with Forward Checking")
    print(">>> 3) Backtrack Search with Maintaining Arc Consistency (MAC)")

    # Input search algorithm option
    option = input("--> ")
    print()

    # Generate CSP and run AC if needed
    variables, domains, constrains = generate_csp(n, p, alpha, r)
    ac_result = True
    if use_ac:
      ac_result = arc_consistency(variables, domains, constrains)

    # Print generated CSP
    print()
    print(">>> Generated CSP:")
    print(">>> Variables: " + ",".join(["X"+str(v) for v in variables]))
    print(">>> Domain: " + ",".join([str(v) for v in domains[0]]))
    print(">>> Constrains:")
    for (var1, var2) in constrains:
      print("("+str(var1)+","+str(var2)+"): " + " ".join([str(val1)+","+str(val2) for val1, val2 in constrains[(var1,var2)]]))
    print()

    # If AC can not reduce domain to zero or AC is not run.
    if ac_result:
      # Run search algorithm
      result = None
      if option == "1":
        result = backtrack({}, variables, domains, constrains)
      elif option == "2":
        result = backtrack({}, variables, domains, constrains, inf_type="FC")
      elif option == "3":
        result = backtrack({}, variables, domains, constrains, inf_type="MAC")
      
      # Shows result from search algorithm
      if result:
        print(">>> Solution <<<")
        print(", ".join(["X"+str(v)+":"+str(result[v]) for v in result]))
        print()
        print()
      else:
        print(">>> Not a valid choice.")
    # In case AC returns fail.
    else:
      print(">>> You are lucky! Just by running AC we can tell that the CSP has no solution.")

    # Loop again if users wants to 
    print(">>> Want to try again? (Y/N)")
    again = input("--> ")

    if again != "y" and again != "Y":
      keep_running = False



# Run main
if __name__ == "__main__":
  main()
