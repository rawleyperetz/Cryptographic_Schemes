# The Baby-Step-Giant-Step is an algorithm for solving the Discrete Logarithm Problem. Computational Complexity O(sqrt(n)) Hope you like it.
# This code computes the solution to the Discrete Log Problem (DLP)

def babyStep_giantStep(base, num, mod):
    powers, inverse_powers = [], []
    for i in range(1,mod-1):
        powers.append(pow(base,i)%mod)
        inverse_val = (num*pow(base,-i*2,mod))%mod 
        inverse_powers.append(inverse_val)
        if inverse_val in powers:
            break 
    index = powers.index(inverse_powers[-1])
    print(f"Collision: Power is {index + 1} and Inverse Part is {i*2}")
    print(f"Inverse is given as {pow(base,-1,mod)}")
    solution = index + 1 + i*2
    return f"Value of x is {solution}"

print(babyStep_giantStep(7,26,41))
print("===========================")
print(babyStep_giantStep(7,4,11))
