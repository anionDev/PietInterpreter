import argparse
from .interpreter.executeFunctions import interpret, takeStep
from .interpreter.imageFunctions import getImage
from .GUI.GUI import GUI

def main():

    parser = argparse.ArgumentParser(description='Interprets a piet image')
    parser.add_argument("-f", "--file", required=True, type=str, help="complete filepath to a .png or .gif image")
    parser.add_argument("-v", "--verbose", action="store_true", help="Outputs number of steps to StdOut")
    parser.add_argument("-g", "--graphical", action="store_true", help="Opens GUI with the file loaded")

    args = parser.parse_args()

    if not args.graphical:
        interpret(getImage(args.file))

        if args.verbose:
            print(f"\nTotal steps: {takeStep.counter}")
    else:
        app = GUI()
        app.setFileText(args.file)
        app.loadFile()
        app.run()

if __name__ == "__main__":
    main()
