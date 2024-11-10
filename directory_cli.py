class Node:
    def __init__(self, name):
        self.name = name
        self.children = {}
        
class FileSystem:
    def __init__(self):
        self.root = {}
        
    def _get_node(self, path):
        """Helper method to get a node from a path"""
        if not path:
            return self.root
            
        parts = path.split('/')
        current = self.root
        
        for part in parts:
            if part not in current:
                return None
            current = current[part].children
            
        return current
        
    def _get_parent_and_name(self, path):
        """Helper method to get parent node and name from a path"""
        parts = path.split('/')
        name = parts[-1]
        parent_path = '/'.join(parts[:-1])
        parent = self._get_node(parent_path)
        return parent, name
        
    def create(self, path):
        """Create a new directory"""
        if not path:
            return
            
        parts = path.split('/')
        current = self.root
        
        for part in parts:
            if part not in current:
                current[part] = Node(part)
            current = current[part].children
            
    def delete(self, path):
        """Delete a directory"""
        parent, name = self._get_parent_and_name(path)
        if parent is None:
            print(f"Cannot delete {path} - {path.split('/')[0]} does not exist")
            return
            
        if name in parent:
            del parent[name]
            
    def move(self, source, target):
        """Move a directory from source to target"""
        # Get source node and its parent
        source_parent, source_name = self._get_parent_and_name(source)
        if source_parent is None or source_name not in source_parent:
            return
            
        # Get target node
        target_node = self._get_node(target)
        if target_node is None:
            return
            
        # Move the node
        node = source_parent[source_name]
        target_node[source_name] = node
        del source_parent[source_name]
        
    def list_directories(self, node=None, prefix="", first_call=True):
        """List all directories"""
        if first_call:
            node = self.root
            
        for name, dir_node in sorted(node.items()):
            print(f"{prefix}{name}")
            if dir_node.children:
                self.list_directories(dir_node.children, prefix + "  ", False)

def process_commands(commands):
    fs = FileSystem()
    
    for command in commands:
        print(command)
        parts = command.strip().split()
        
        if parts[0] == "CREATE":
            fs.create(parts[1])
        elif parts[0] == "DELETE":
            fs.delete(parts[1])
        elif parts[0] == "MOVE":
            fs.move(parts[1], parts[2])
        elif parts[0] == "LIST":
            fs.list_directories()

def main():
    # Read commands from standard input
    commands = []
    try:
        while True:
            line = input()
            if line.strip():
                commands.append(line)
    except EOFError:
        pass
    
    process_commands(commands)

if __name__ == "__main__":
    main()