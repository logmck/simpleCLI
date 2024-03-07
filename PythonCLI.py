class Node:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []

class FileSystem:
    def __init__(self):
        self.root = Node('/')
        self.current_directory = self.root

    def mkdir(self, directory_name):
        new_directory = Node(directory_name)
        self.current_directory.children.append(new_directory)

    def touch(self, file_name):
        new_file = Node(file_name, is_file=True)
        self.current_directory.children.append(new_file)

    def ls(self):
        for child in self.current_directory.children:
            print(child.name)

    def cd(self, directory_name):
        if directory_name == '..':
            if self.current_directory != self.root:
                self.current_directory = self.find_parent_directory(self.current_directory)
        else:
            found = False
            for child in self.current_directory.children:
                if not child.is_file and child.name == directory_name:
                    self.current_directory = child
                    found = True
                    break
            if not found:
                print(f"Directory '{directory_name}' not found.")

    def find_parent_directory(self, node):
        parent = self.root
        for child in self.root.children:
            if child == node:
                return parent
            parent = self.find_parent_directory_recursive(child, node)
            if parent:
                return parent
        return None

    def find_parent_directory_recursive(self, parent, node):
        for child in parent.children:
            if child == node:
                return parent
            grandparent = self.find_parent_directory_recursive(child, node)
            if grandparent:
                return grandparent
        return None

class SimpleCLI:
    def __init__(self):
        self.file_system = FileSystem()

    def run(self):
        print("Welcome to Simple CLI! Type 'help' for available commands.")
        while True:
            command = input(f"{self.file_system.current_directory.name} $ ").strip().split()
            if not command:
                continue
            if command[0] == 'exit':
                print("Exiting...")
                break
            elif command[0] == 'help':
                self.display_help()
            elif command[0] == 'mkdir':
                if len(command) < 2:
                    print("Usage: mkdir <directory_name>")
                else:
                    self.file_system.mkdir(command[1])
            elif command[0] == 'touch':
                if len(command) < 2:
                    print("Usage: touch <file_name>")
                else:
                    self.file_system.touch(command[1])
            elif command[0] == 'ls':
                self.file_system.ls()
            elif command[0] == 'cd':
                if len(command) < 2:
                    print("Usage: cd <directory>")
                else:
                    self.file_system.cd(command[1])
            else:
                print("Command not found. Type 'help' for available commands.")

    def display_help(self):
        print("Available commands:")
        print("  exit - Exit the program")
        print("  help - Display this help message")
        print("  mkdir <directory_name> - Create a new directory")
        print("  touch <file_name> - Create a new file")
        print("  ls - List files and directories in the current directory")
        print("  cd <directory> - Change current directory")

if __name__ == "__main__":
    cli = SimpleCLI()
    cli.run()
