# This is the modified source file for feature-z branch
def feature_z():
    print("This is feature-z branch")
    print("This is a new feature added in feature-z branch")
    print("Feature Z: This is a program to generate Fibonacci sequence")
    n = int(input("Enter the number of terms: "))

    n1, n2 = 0, 1
    count = 0

    if n <= 0:
       print("Please enter a positive integer")
    elif n == 1:
       print("Fibonacci sequence up to", n, ":")
       print(n1)
    else:
       print("Fibonacci sequence:")
       while count < n:
           print(n1)
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1

if __name__ == "__main__":
    feature_z()
