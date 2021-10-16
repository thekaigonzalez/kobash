import argparse
import sys

class ArgumentParser(argparse.ArgumentParser):

    def error(self, message):
        self.print_help(sys.stderr)
        print(2, '%s: error: %s\n' % (self.prog, message))