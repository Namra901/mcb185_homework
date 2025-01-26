def tm(A, T, G, C):
    """Calculate the melting temperature (Tm) of an oligo."""
    total_bases = A + T + G + C
    if total_bases <= 13:
        return (A + T) * 2 + (G + C) * 4
    else:
        return 64.9 + (41 * (G + C - 16.4) / total_bases)

# Demonstration of the function
if __name__ == "__main__":
    print("Melting temperatures (Tm):")
    print(tm(5, 7, 3, 4))  # Short oligo (<= 13 bases)
    print(tm(10, 15, 25, 20))  # Longer oligo (> 13 bases)
    print(tm(4, 3, 2, 4))  # Another example

