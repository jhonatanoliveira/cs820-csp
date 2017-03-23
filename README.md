Description
-----------

This is the solution for Assignment 3 in CS820 - Artificial Intelligence.
The solution proposes an implementation of 3 solving techniques for Constraint Satisfaction Problems (CSPs).
The implementation follows algorithms proposed in [1].
Follows an overview for each implemented algorithm:

* Backtrack Search: search for a solution in the CSP by using a depth first approach and backtracking whenever an inconsistency is found.

* Backtrack Search with Forward Checking: whenever a new variable is assigned, the forward-checking process establishes arc consistency for it.

* Backtrack Search with Maintaining Arc Consistency: similar to forward checking but recursively propagate constraints when changes are made to the domains of variables.

In order to test the techniques, a CSP generator was implemented.
Binary CSP instances can be randomly generated using the model RB proposed in [2].
The choice of this model is motivated by the fact that it has exact phase transition and the ability to generate asymptotically hard instances.
More precisely, CSPs are randomly generated using the following parameters: *n*, *p*, *alpha* and *r* where *n* is the number of variables, *p* (0 < p < 1) is the constraint tightness, and *r* and alpha (0 < r, alpha < 1) are two positive constants used by the model RB [2].


There are 6 files in this solution:
  - main.py: utility script with a simple user menu for running an initial state with a chosen search algorithm.
  - csp_inference.py: solving techniques implementations.
  - csp_generator.py: an instance CSP generator.
  - README: overview and instructions
  - tests.py: helper script for demonstrating functions.

You can also find this solution in the following [GitHub repository](https://github.com/jhonatanoliveira/cs820-csp).


References
----------

[1] Russell, S. J., & Norvig, P. (2002). Artificial intelligence: a modern approach.

[2] K. Xu and W. Li. Exact Phase Transitions in Random Constraint Satisfaction Problems. Journal of Artificial Intelligence Research, 12:93–103, 2000.


Requirements
-------------

This solution requires the following softwares:
- Python 3.6 or higher


How it Works
-------------

Use the ```main.py``` script helper to run the user interface.
A menu guides the user through all choices of solving techniques and input constants.
After assigning all options, the user will see a solution for the given CSP.

A CSP is described by variables, its domain, and constrains in the variable's domain.
Each variable is represented by a number.
For example, a CSP with 3 variables has the following structure:
```
  [0, 1, 2]
```
The domain of variable is also represented by numbers.
For instance, the domain of variable 0 is formed by the following 2 values:
```
  [0, 1]
```
Binary constrains are a list of tuples with values from variables that are not acceptable.
All constrains are saved in a dictionary where the keys indicate the couple of variables involved.
For example, constrains between variables 0 and 1 and between variables 2 and 3 can be described as follows:
```
  {
       (0,1): [(0,1), (1,2)],
       (1,2): [(1,0), (2,2)]
  }
```



Getting Started
---------------

In order to run the solution using the user's menu, the script ```main.py``` can be called from the terminal command as follows:

```
$ python main.py
```

This is an example of a complete user interaction run:

```
$ python main.py
>>> Starting Assignment 3 Solution <<<

>>> Constants:
--> Number of variables (n): 5
--> Constraint Tightness (p): 0.2
--> Constant alpha: 0.9
--> Constant r: 0.2


>>> Do you wish to run Arc-Consistency before backtrack?
--> (y/n): y


>>> Choose the Search algorithm
>>> 1) Backtrack Search
>>> 2) Backtrack Search with Forward Checking
>>> 3) Backtrack Search with Maintaining Arc Consistency (MAC)
--> 3


>>> Generated CSP:
>>> Variables: X0,X1,X2,X3,X4
>>> Domain: 0,1,2,3
>>> Constrains:
(4,0): 0,1 0,3 0,3 0,1
(1,2): 3,0 0,0 1,1 1,2
(4,1): 2,0 3,1 1,0 3,0

>>> Solution:
X0:0, X1:0, X2:1, X3:0, X4:0
>>> Want to try again? (Y/N)
-->
```

Users can keep running the menu as long as they want by typing "Y" or "y" at the end of the search algorithm run.


AUTHOR
---------
Jhonatan S. Oliveira
oliveira@uregina.ca
Department of Computer Science
University of Regina
Canada
