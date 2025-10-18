"""

The Prototype Design Pattern is a creational pattern that lets you create new objects by copying existing ones (the “prototype”) instead of constructing them from scratch.

It’s useful when:

Object creation is expensive or complex.
You need many similar objects with small differences.
You want to avoid coupling code to concrete class constructors.


Real-Life Use Cases

Game Development
Imagine spawning enemies with the same base stats, but different weapons or skins.
Cloning a “prototype enemy” avoids constructing them from scratch every frame.

UI Component Systems
Copying a prototype button or widget with a few style tweaks saves reinitialization overhead.

Machine Learning Pipelines
Cloning model configurations or data transformers before mutation experiments.

Document Editors
Duplicating a base document template and editing attributes (headers, metadata, etc.).

"""

import copy

class Document:
    def __init__(self, title, author, content, metadata):
        self.title = title
        self.author = author
        self.content = content
        self.metadata = metadata

    def clone(self, **attrs):
        obj = copy.deepcopy(self)
        obj.__dict__.update(attrs)
        return obj

# Create a base template
invoice_template = Document(
    title="Invoice Template",
    author="Finance Dept",
    content="Invoice for services rendered.",
    metadata={"company": "TechCorp", "currency": "USD"}
)

# Clone and modify
client_invoice = invoice_template.clone(
    title="Invoice #12345",
    metadata={"company": "TechCorp", "currency": "USD", "client": "Acme Inc."}
)

print(client_invoice.title)
print(client_invoice.metadata)
