#!/usr/bin/python3
"""
HBNBCommand - Command Interpreter for HBNB Application
"""


import cmd
class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - Command Interpreter for HBNB Application
    """

    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'Amenity',
               'Place', 'City', 'State', 'Review']

    def do_quit(self, line):
        """Quits the session"""
        return True

    def do_EOF(self, line):
        """Exits the session"""
        return True

    def do_create(self, line):
        """creates a new instance of BaseModel"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            Models = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
                      'Place': Place, 'City': City,
                      'State': State, 'Review': Review}
            the_model = Models[args[0]]()
            print(the_model.id)
            the_model.save()

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key in storage.all():
                object = storage.all()[key]
                print(object)
            else:
                print("** no instance found **")

    def do_destory(self, line):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCammand.classes:
            print("** class doesn't exist **")
            return
        elif args < 2:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all()
                del storage.all()[key]
            storage.save()
            return
            else:
                print("** instance id missing **")

    


if __name__ == '__main__':
    HBNBCommand().cmdloop()