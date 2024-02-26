#!/usr/bin/python3
"""Console module
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb)"
    classes = ["BaseModel", "User", "Amenity", "City",
               "Place", "Review", "State"]

    def do_EOF(self, line):
        """ EOF command to exit the program
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
        """
        commands = shlex.split(args)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")

            storage.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id.
        """
        commands = shlex.split(args)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{commands[0]}.{commands[1]}"
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file).
        """
        commands = shlex.split(args)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{commands[0]}.{commands[1]}"
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name.
        """
        commands = shlex.split(args)
        objects = storage.all()

        if len(commands) == 0:
            for key, value in objects.items():
                print(str(value))
        elif commands[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split(".")[0] == commands[0]:
                    print(str(value))

    def default(self, args):
        """Called on an input line when the command prefix is not recognized.
        """
        commands = args.split(".")
        if len(commands) == 2:
            if commands[0] in self.classes:
                if commands[1] == "all()":
                    self.do_all(commands[0])
                else:
                    print("** Unknown syntax:", args)
            else:
                print("** class doesn't exist **")
        else:
            print("** Unknown syntax:", args)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
        """
        commands = shlex.split(args)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{commands[0]}.{commands[1]}"
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attr = commands[2]
                value = commands[3]
                try:
                    value = eval(value)
                except Exception:
                    pass
                setattr(obj, attr, value)
                obj.save()

    def count(self, args):
        """Retrieve the number of instances of a class.
        """
        commands = shlex.split(args)
        objects = storage.all()
        count = 0
        for key, value in objects.items():
            if key.split(".")[0] == commands[0]:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
