# This is the modified source file for feature-y branch
def feature_y():
    print("This is feature-y branch")
    print("This is a new feature added in feature-y branch")
    print("Feature Y: This is a program to check if a number is prime or not")
    num = int(input("Enter a number: "))

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

if __name__ == "__main__":
    feature_y()
