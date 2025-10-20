"""

Composite is a structural design pattern that lets you compose objects into tree structures 
and then work with these structures as if they were individual objects.

You’ve got objects that form part–whole hierarchies.
For example, a File and a Folder.

A File is a single item.

A Folder contains files and other folders.

But both should be treated the same way — you should be able to call something like open() or show_details() on both a file and a folder without writing a special case for each.

That’s the Composite pattern’s mission:

“Allow clients to treat individual objects and compositions of objects uniformly.”

It’s literally the OOP version of "don’t make me think."
"""

from abc import ABC, abstractmethod

# The Component
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self, indent=0):
        pass


# The Leaf
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def show_details(self, indent=0):
        print(" " * indent + f"File: {self.name} ({self.size}KB)")


# The Composite
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show_details(self, indent=0):
        print(" " * indent + f"Folder: {self.name}")
        for child in self.children:
            child.show_details(indent + 2)


# Create files
file1 = File("resume.pdf", 120)
file2 = File("photo.png", 340)
file3 = File("data.csv", 560)

# Create folders
root = Folder("root")
documents = Folder("documents")
pictures = Folder("pictures")

# Compose hierarchy
documents.add(file1)
pictures.add(file2)
root.add(documents)
root.add(pictures)
root.add(file3)

# Display everything
root.show_details()

"""

Folder: root
  Folder: documents
    File: resume.pdf (120KB)
  Folder: pictures
    File: photo.png (340KB)
  File: data.csv (560KB)


"""