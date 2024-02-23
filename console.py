import cmd

"""Console module
"""


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """ EOF command to exit the program
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def create(self, inst):
        base = BaseModel


"""create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
Ex: $ create BaseModel
If the class name is missing, print ** class name missing ** (ex: $ create)
If the class name doesn’t exist, print ** class doesn't exist ** (ex: $ create MyModel)"""
if __name__ == '__main__':
    HBNBCommand().cmdloop()
