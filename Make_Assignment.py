# Function to convert steps to miles
def steps_to_miles(steps):
    # Check if steps is negative
    if steps < 0:
        raise ValueError("Exception: Negative step count entered.")
    # 2000 steps = 1 mile, so divide steps by 2000
    miles = steps / 2000
    return miles

# Main program
def main():
    try:
        # Get number of steps from user
        print("Please enter the number steps taken:")
        steps = int(input())
        # Convert steps to miles
        miles = steps_to_miles(steps)
        # Print miles with 2 decimal places
        print(f'{miles:.2f}')
    except ValueError as e:
        # Print error message if ValueError occurs
        print(e)

# Run the main program
if __name__ == "__main__":
    main()