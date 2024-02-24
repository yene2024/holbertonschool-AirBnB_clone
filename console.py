import cmd
import shlex
from models.base_model import BaseModel
"""Console module
"""


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb)"
    classes = ["BaseModel"]

    def do_EOF(self, line):
        """ EOF command to exit the program
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        commands = shlex.split(args)
        if commands == "":
            print("** class name missing **")
        elif commands not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
