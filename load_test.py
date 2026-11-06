#######################################
# Programmer: Adrian Sanchez
# Class: ENSC-201-01, Fall 2026
# PA5
# 11/5/26
# Description: 
# References used: PA5 document
#######################################

def get_positive_number(prompt):
    """
    This function prompts the user to enter a positive number and will
    repeatedly display the promp until the user enters a number that is > 0

    parameters: 
        prompt(string) : a message displayed to user

    returns:
        float: positive # entered by user
    """

    while True:
        positive_number = int(input(prompt))

        if positive_number >= 0:
            return(positive_number)
        else:
            print("Error: NOT a positive number. Please enter a positive number")


def calculate_stress(force, area):
    """
    Calculate the stress on a mechanical component using: Stress = Force / Area
    
    Parameters: 
        force (N), area (mm²)

    Return: 
            Stress (N/mm²) as a float
    
    pre-conditions: 
        force >= 0, area > 0
    """
    stress = force / area
    return stress


def classify_stress(stress, limit):
    """
    Classifies the stress into a category according the the percentage of 
    achieved stress based on the allowable stress limit

    parameters:
        stress(float) : calculated stress
        limit(float) : allowable stress limit

    returns:
        string: "SAFE" if the stress is below 80% of allowable limit
        "WARNING" if stress is between 80% and 100% of allowable limit
        "FAILURE" if stress is exceeding the allowable limit
    
    pre-conditions: stress >= 0, limit > 0
    """
    
    allowable_stress_limit = limit
    user_stress = stress
    if user_stress < allowable_stress_limit * 0.8:
        return ("SAFE")
    elif user_stress >= allowable_stress_limit * 0.8 and user_stress <= allowable_stress_limit:
        return ("WARNING")
    else:
        return ("FAILURE")


def run_load_test(initial_force, increment, cycles, area, limit):
    """
    Simulates loading tests on components beginning with an initial force
    and increasing the force with each cycle

    parameters:
        initial_force(float) : starting force
        increment(float) : amount of force added after each cycle
        cycles(int) : max number of cycles that will be simulated
        area(float) : area of component
        limit(float) : allowable stress limit

    Return: 
        The cycle number where failure occurred, or 0 if all cycles completed 
        without failure

    pre-conditions: initial_force > 0, increment > 0, cycles > 0, area > 0, limit > 0
    """

    force = initial_force
    for cycle in range(1, cycles + 1):
        stress = calculate_stress(force, area)
        classification = classify_stress(stress, limit)
        print("cycle: ", cycle)
        print("stress: ", stress)
        print("classification: ", classification)

        if classification == "FAILURE":
            print("result: Failed")
            print("simulation stopped early")
            return cycle
        force += increment
    print("Result: PASSED")
    print("All", cycles, "cycles completed")
    return 0


def main():
    """
    Runs all the programs which collects the input from the user, runs the load
    test, and prints the results

    returns: 
        nothing
    """

    again = input("Would you like to begin simulation? (y/n): ")
    again == "y"
    while again.lower() == "y":
        number = get_positive_number("Enter a positive number: ")
        print("Number entered: ", number)
        force = float(input("Enter a force in N: "))
        increment = float(input("Enter a force increment in N: "))
        cycles = int(input("Enter number of cycles: "))
        area = float(input("Enter an area (mm^2): "))
        limit = float(input("Enter an allowable stress limit in (N/mm^2): "))
        load_test = run_load_test(force, increment, cycles, area, limit)
        again = input("Would you like to run another test? (y/n): ")
    print("Simulation Ended")


if __name__ == "__main__":
    main()
