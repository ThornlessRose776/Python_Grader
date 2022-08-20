# Python_Grader
This class will take a folder of python functions and run those functions with inputs given from the user in a text file.
Can only grade one function at a time so won't run other functions in the file if there are other (since it uses the name of the function to run it)
Inputs for the class are handled in the UI.py file.
Four parameters need to be entered for the progrsm to work properly.

Path requires the file path of the folder containing the python files. Format should look like this: "C:\\Users\\name\\directory\\folder\\etc..."
Num_of_inputs requires the number of inputs that the function to be graded requires. This number is how it properly iterates through the next input.
ins_and_outs requires the file path to the text file that contains the test inputs and outputs for the function. This is how each file is graded. The file must be formated with each line either being an input or an output. Input comes first the output, then input again, and so on. For functions with multiple inputs, it would go as follows.

input1
input2
inputn
output
input1
input2
inputn
output
etc...

func_name requires the name of the function, without the "()" at the end. For example the function in the UI.py file would be input as "grade_assigments"
