"""

The Adapter Design Pattern is a structural pattern that allows two incompatible interfaces to work together.

It converts the interface of a class into another interface the client expects, without changing the existing code.
Think of it as:
“Make this old weird plug fit into my shiny new socket.”

🧠 The Core Idea
You have:
Client — the code that expects a certain interface.
Adaptee — an existing class with a different interface.
Adapter — the bridge that makes them compatible.

The Adapter wraps the Adaptee and exposes the Client’s expected interface.

"""

import xml.etree.ElementTree as ET

class XMLService:
    def get_data(self):
        return "<user><name>Uday</name><role>Engineer</role></user>"

class JSONAdapter:
    def __init__(self, xml_service):
        self.xml_service = xml_service

    def get_data(self):
        xml = self.xml_service.get_data()
        root = ET.fromstring(xml)
        return {child.tag: child.text for child in root}

# Client code expects JSON-like data
xml_service = XMLService()
adapter = JSONAdapter(xml_service)
data = adapter.get_data()

print(data)


"""

Cant we use a similar static method for a class like create_from_json instead of adapter design pattern.

Yes, you can use a static or class method like create_from_json() to adapt inputs.
But no, that’s not the same thing as an Adapter Pattern — it’s a shortcut that works in simple cases but breaks down when the world gets complicated (and it always does).

"""

import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(data['name'], data['age'])

    @classmethod
    def create_from_dict(cls, data_dict):
        return cls(data_dict['name'], data_dict['age'])



"""

| **Approach**         | **Who Adapts?**          | **Where Logic Lives**  | **When It Fails**                                                                                 |
| -------------------- | ------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------- |
| `create_from_json()` | The class itself         | Inside the class       | When you need to adapt *external systems*, *multiple incompatible APIs*, or *complex hierarchies* |
| **Adapter Pattern**  | A separate adapter class | Outside the main class | Scales easily when new external interfaces appear                                                 |



The Core Design Difference

create_from_json modifies the core class to understand foreign formats.
It’s fine for one or two cases, but soon your class becomes a Swiss Army knife — with a corkscrew, bottle opener, and emotional baggage.

The Adapter Pattern keeps your core class pure and delegates adaptation to a separate class, keeping things open for extension 
and closed for modification (the Open/Closed Principle from SOLID).


Example: Where It Starts to Fall Apart

Let’s say your class User originally just loads from JSON.
Then your team adds:

XML data from a legacy service

YAML from a configuration tool

Protobuf from an ML pipeline

Your class suddenly looks like this Frankenstein’s monster:

"""

class User:
    @classmethod
    def create_from_json(cls, data): ...
    @classmethod
    def create_from_xml(cls, data): ...
    @classmethod
    def create_from_yaml(cls, data): ...
    @classmethod
    def create_from_protobuf(cls, data): ...


"""
correct approach is to create separate adapters for each format:

"""

class XMLUserAdapter:
    def __init__(self, xml_data):
        self.xml_data = xml_data

    def get_user(self):
        # Convert XML -> dict -> User
        ...

class YAMLUserAdapter:
    def __init__(self, yaml_data):
        self.yaml_data = yaml_data

    def get_user(self):
        # Convert YAML -> dict -> User
        ...
