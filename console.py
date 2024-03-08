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

    def do_create(self, arg):
        """creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            Models = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
                      'Place': Place, 'City': City,
                      'State': State, 'Review': Review}
            the_model = Models[arg]()
            print(the_model.id)
            the_model.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()