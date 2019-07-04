def find_costructor(decomposition_sum):
    for constructor in range(decomposition_sum):
        constructor_sum=constructor
        for digit in str(constructor):
            constructor_sum+=int(digit)
        if decomposition_sum==constructor_sum:
            return constructor
    return 0
decomposition_sum=int(input())
print(find_costructor(decomposition_sum))