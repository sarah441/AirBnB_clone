#!/usr/bin/python3
"""the console to begin"""
import cmd


"""task 6 : Your class definition must be: class HBNBCommand(cmd.Cmd):
quit and EOF to exit the program
a custom prompt: (hbnb)
an empty line + ENTER shouldn’t execute anything"""

class HBNBCommand(cmd.Cmd):
    """change to custom which is hbnb"""
    prompt = "(hbnb)"

    def do_EOF(self, args):
        """EOF end of file to exit the programm"""
        return True

    def do_quit(self, args):
        """Quits to quit the shell"""
        return True

    def emptyline(self):
        """empty line when where the user presses Enter without typing any command."""
        pass
if __name__ == "__main__":
    HBNBCommand().cmdloop()
