from math import pi

if __name__ == '__main__':
    def userInput():
        try:
            circle_radius = float(input("Enter radius: "))
            return circle_radius
        except ValueError:
            print("Please enter a numeric value")
            userInput()

    radius = userInput()
    circle_area = pi * radius ** 2
    print(f"The area of a circle with a radius of {radius} is " + str(circle_area))