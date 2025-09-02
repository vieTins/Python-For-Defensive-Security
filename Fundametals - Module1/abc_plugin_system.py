# Design an abstract class Command with name and run(args); dynamically load subclasses from a plugins/ directory and execute them.  
from abc import ABC, abstractmethod
import os
import importlib.util
import inspect
class Command(ABC): 
    @abstractmethod
    def name(self)->str:
        pass
    def run(self, args: list[str]) -> None:
        pass

class PluginManager:
    def __init__(self, plugin_dir: str = "plugins")-> None:
        self.plugin_dir  = plugin_dir
        self.commands = {}
    def load_plugins(self)->None:
        # Tải tất cả plugin từ folder plugins
        if not os.path.exists(self.plugin_dir):
            print(f"Plugin directory '{self.plugin_dir}' does not exist.")
            return 
        init_file = os.path.join(self.plugin_dir, "__init__.py")
        if not os.path.exists(init_file):
            with open (init_file, "w") as f:
                f.write("# Init file for plugins package\n")
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py") and filename != "__init__.py": 
                self._load_plugins(filename)
    # Tải 1 plugin cụ thể
    def _load_plugins(self, filename:str)->None:
        try:
            plugin_path = os.path.join(self.plugin_dir, filename)
            module_name = filename[:-3]  # Remove .py extension
            # load module
            spec = importlib.util.spec_from_file_location(module_name, plugin_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module) 
            # Tìm các class kết thừa từ class Command 
            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and issubclass(obj, Command) and obj != Command):
                    # tạo instance và đăng ký 
                    command_instance = obj()
                    command_name = command_instance.name() 
                    self.commands[command_name] = command_instance 
                    print(f"Loaded plugin: {command_name} from {filename}")
        except Exception as e:
            print(f"Failed to load plugin {filename}: {e}")
    def execute_command(self, command_name:str, args: list[str]):
        if command_name in self.commands:
            try:
                self.commands[command_name].run(args)
            except Exception as e:
                print(f"Failed to execute command '{command_name}': {e}") 
        else: 
            print(f"Command '{command_name}' not found.") 
            self.list_commands()
    def list_commands(self)->None:
        if self.commands:
            print("Available commands:")
            for command_name in self.commands:
                print(f" - {command_name}")
        else:
            print("No commands available.")
def main():
    manager = PluginManager()
    manager.load_plugins()
    print("\nPlugin System Ready. Type 'help' to list commands or 'exit' to quit.")
    while True:
        try: 
            user_input = input("> ").strip()
            if not user_input:
                continue
            if user_input.lower() == "exit":
                break
            if user_input.lower() == "help":
                manager.list_commands()
            else:
                parts = user_input.split()
                command_name = parts[0]
                args = parts[1:]
                manager.execute_command(command_name, args)
        except (KeyboardInterrupt, EOFError):
            print("Exiting...")
            break
if __name__ == "__main__":
    main()