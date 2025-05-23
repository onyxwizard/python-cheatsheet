#try block executes only if it fails then except block executes
def exception_handling_demo():
    try:
        age = input("Enter your age: ")
        result = 100 / int(age)
        print(f"Result of 100 / {age} is {result}")
        return "Success"
    except ValueError as e:
        print("Caught an error: Invalid input. Please enter a valid number.")
        print(f"Exception: {e}")
        
exception_handling_demo()    
    