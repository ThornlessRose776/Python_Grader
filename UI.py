from Python_Grader import PythonGrader

def grade_assignments():
    """Function that gets the parameters needed from the user for the PythonGrader class and runs the methods from the class using those inputs
    """
    x = True
    while x == True:
        command = input("Enter g to grade a folder of assignments or e to exit: ")
        if command == "g":
            path = input("Enter the file path for the folder containing the assignments to be graded: ")
            num_of_inputs = int(input("Enter the amount of inputs the function to be graded contains: "))
            ins_and_outs = input("Enter the file path for the .txt file containing the test inputs and outputs: ")
            func_name = input("Enter the name of the function to be graded: ")

            grading = PythonGrader(path, num_of_inputs, ins_and_outs, func_name)
            grading.file_list()
            grading.inputs_and_outputs()
            grading.check_files()
            grading.check_answers()
            grading.quick_test()
            grading.grades_file()

        elif command == "e":
            x = False
        else:
            print("Invalid command, try again")

grade_assignments()

