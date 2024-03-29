import math

def count_possible_keys():
 
    total_permutations = math.factorial(25)

    effectively_unique_keys = 2 ** 25

    return total_permutations, effectively_unique_keys

def main():
    total_permutations, effectively_unique_keys = count_possible_keys()
    print("Total number of unique permutations of 25 items:", total_permutations)
    print("Approximate number of effectively unique keys:", effectively_unique_keys)

if __name__ == "__main__":
    main()
