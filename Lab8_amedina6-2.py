"""Menu-driven geometry calculator."""

import circle as circle_module
import rectangle as rectangle_module


# Aliases are necessary because both circle.py and rectangle.py have a function
# named calc_area(). Using aliases helps Python know which calc_area() function
# to use: circle_module.calc_area() or rectangle_module.calc_area().


def get_positive_number(prompt):
    """Ask the user for a positive number and validate the input."""
    while True:
        try:
            number = float(input(prompt))

            if number <= 0:
                print("Error: Please enter a positive number greater than zero.")
            else:
                return number

        except ValueError:
            print("Error: Please enter a valid number.")


def display_menu():
    """Display the geometry calculator menu."""
    print()
    print("Geometry Calculator")
    print("-------------------")
    print("1. Calculate Circle Area")
    print("2. Calculate Circle Circumference")
    print("3. Calculate Rectangle Area")
    print("4. Calculate Rectangle Perimeter")
    print("5. Exit")


def main():
    """Run the main geometry calculator program."""
    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            radius = get_positive_number("Enter the radius of the circle: ")
            area = circle_module.calc_area(radius)
            print(f"The area of the circle is {area:.3f}.")
            input("Press Enter to continue...")

        elif choice == "2":
            radius = get_positive_number("Enter the radius of the circle: ")
            circumference = circle_module.calc_circumference(radius)
            print(f"The circumference of the circle is {circumference:.3f}.")
            input("Press Enter to continue...")

        elif choice == "3":
            width = get_positive_number("Enter the width of the rectangle: ")
            height = get_positive_number("Enter the height of the rectangle: ")
            area = rectangle_module.calc_area(width, height)
            print(f"The area of the rectangle is {area:.1f}.")
            input("Press Enter to continue...")

        elif choice == "4":
            width = get_positive_number("Enter the width of the rectangle: ")
            height = get_positive_number("Enter the height of the rectangle: ")
            perimeter = rectangle_module.calc_perimeter(width, height)
            print(f"The perimeter of the rectangle is {perimeter:.1f}.")
            input("Press Enter to continue...")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()