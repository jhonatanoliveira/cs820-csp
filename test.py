from csp_generator import generate_csp

# Test generate_csp
n = 5
p = 0.7
alpha = 0.9
r = 0.2
variables, domains, constrains = generate_csp(n, p, alpha, r)
print(variables)
print(domains)
print(constrains)