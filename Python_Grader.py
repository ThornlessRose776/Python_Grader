import os # Used to iterate through the folder and get a list of the names of te files in the folder
import importlib.util # Used to be able to import each file's function using a directory that was written in string


class PythonGrader:

    def __init__(self, path, num_of_inputs, ins_and_outs, func_name) -> None:
        """Initializes the key variables that will be used throughout the class

        Args:
            path (str): A string of the file path where the folder with the assignments to be graded is located
            num_of_inputs (int): The num of inputs that the function to be graded required. 
            ins_and_outs (.txt file): A text file that contains test inputs and their proper outputs to be used to grade each assignment 
            func_name (str): A string that is exact name of the function (including dashes, etc. but NOT the "()" at the end of the function)
        """
        self.path = path # Format of path should be "C:\\Users\\name\\directory\\folder\\etc..."  "\\" is important for functions that use this variable!!!
        self.num_of_inputs = num_of_inputs # should just be an integer
        self.ins_and_outs = ins_and_outs # Text file format should have each line be an input or output. If multiple inputs 1 line per input
        #                                  Input(s) should come first IN ORDER if multiple(unless using keys), then output, then next input(s), then output, etc...
        self.func_name = func_name # string of function name with "()" ex. "func_tion" NOT "func_tion()""
        self.Assignment_files = [] # stores the name of the files in the folder
        self.input_list = [] # stores the inputs from the given text file
        self.output_list = [] # stores the outputs from the given text file
        self.student_outs = [] # stores the outputs for the student functions
        self.grades = [] # stores the grades of the students.
    
    def file_list(self):
        """Creates a list of the names of the files in the given folder
        """
        for filename in os.listdir(self.path):
            if filename == '__pycache__':  # Makes it so that pycache is skipping when looking at files in a folder
                pass
            else:
                self.Assignment_files.append(filename) # appends the name of the file to the list
        print("file list: ", self.Assignment_files) # check
    
    def inputs_and_outputs(self):
        """Creates a list for the inputs and another list for the outputs from the given text file
        """
        count = 1 # keeps track of if the the current line is an input or output
        with open(self.ins_and_outs) as f:
            for line in f:
                if count % (self.num_of_inputs + 1) == 0: # if true, then item is an output
                    self.output_list.append(line)
                    count += 1
                else: 
                    self.input_list.append(line) # item is in input
                    count += 1
        print("output list: ", self.output_list) # check
        print("input list: ", self.input_list) # check

    
    def file_checker(self,file):
        """Takes a file an runs a function inside of the file

        Args:
            file (str): A string that contains the name of the file
        """
        #path = "C:\\Users\\patar\\Downloads\\College Stuff\\Comp Fundamentals\\Final Project\\Assignments\\PS3_2.py"
        path = self.path + "\\" + file # appends the file name to the path in order to create the path to the file.
        spec = importlib.util.spec_from_file_location(file, path) # creates a module spec
        test = importlib.util.module_from_spec(spec) # creates a module from the spec
        spec.loader.exec_module(test) # Imports the module 
            
        for i in range(0,len(self.input_list),self.num_of_inputs): # goes through the list of every input, but skips every x where x is the num of inputs
            call = f"test.{self.func_name}(" # base call without inputs or last ")"
            for j in range(0,self.num_of_inputs): # loop that will append each input to call using the provided number of inputs
                if j == 0: # First input
                    call += f"{self.input_list[i+j]}" # No comma at the beginning
                else: # Other inputs
                    call += f",{self.input_list[i+j]}" # Comma at the beginning
            call += ")" # adds after final input
            print("call: ", call) # check
            out = eval(call) # eval takes a string and treats it as a function call, which will run the function with the specicfied inputs
            print("out: ", out) #check
            self.student_outs.append(str(out)) # Appends the output to the student output list.
            print("student outs: ", self.student_outs) # check
    
    def check_files(self):
        """Loop that takes each file name in the Assignment_files list and uses the name as the input for the file_checker method
        """
        for file in self.Assignment_files: # Iterates through self.Assignment_files
            self.file_checker(file) # runs the file using the method

    def check_answers(self):
        """Checks each student output with the outputs provided using the output list
        """
        answers = len(self.output_list) # number of outputs provided
        for i in range(0, len(self.student_outs), answers): # loop that skips every "answers" times
            score = 0 # base score
            for j in range(0,answers): # goes through each answer
                if "\n" in self.output_list[j]: # \n makes string unequal (who decided that was a good idea? I just want to know.)
                    self.student_outs[i+j] += "\n" # adds \n so that the two strings are equal(as the text file automatically has each answer except the last contain \n)
                if self.student_outs[i+j] == self.output_list[j]: # checks if the outputs are the same
                    score += 1 # adds 1 to the score
            grade = (score / answers) * 100 # calculates the grade based on the number of correct outputs
            self.grades.append(grade) # adds that grade to th egrade list
        print("Grades: ", self.grades) # check
    
    def grades_file(self): 
        """Creates a file with every assignment name and the grade that the assignment got.
        """
        with open("Grades.txt","w") as f:
            for i in range(0,len(self.Assignment_files)): 
                    f.write(f"{self.Assignment_files[i]}: {self.grades[i]}%\n") # writes the file name and the grade that file got. Both lists are in the order of the files in the list
        





            

            



