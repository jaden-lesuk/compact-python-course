if __name__ == '__main__':
    def get_user_input():
        try:
            user_input = int(input("Enter a number to calculate the factorial: "))
            return user_input
        except ValueError:
            print("Please enter a numeric value")
            get_user_input()

    def calculate_factorial(n):
        if n < 2:
            return 1
        else:
            return n * calculate_factorial(n-1)

    user_number = get_user_input()
    user_factorial = calculate_factorial(user_number)

    print(f"The factorial of {user_number} is {user_factorial}")