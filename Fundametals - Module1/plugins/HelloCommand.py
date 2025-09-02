from abc import ABC
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from abc_plugin_system import Command
class HelloCommand(Command): 
    def name(self)-> str:
        return "HelloCommand"
    def run(self, args: list[str])-> None:
        if args: 
            print(f"Hello, {args[0]}!")
            print("Hello, World!")