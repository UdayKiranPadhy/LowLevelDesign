"""

The Builder Pattern is a creational pattern that separates the construction of a complex object from its representation.
Translation: it lets you build objects piece by piece, controlling the process, without stuffing 20 parameters 
into your constructor like a sadist.

You basically have:

A Director: Orchestrates how to build the product.
A Builder Interface: Defines steps to build the parts.
One or more Concrete Builders: Implement those steps.
The Product: The final object assembled at the end.

"""


class House:
    def __init__(self):
        self.floors = None
        self.windows = None
        self.doors = None
        self.has_garage = False
        self.has_garden = False
        self.has_swimming_pool = False

    def __str__(self):
        return (f"House with {self.floors} floors, {self.windows} windows, "
                f"{self.doors} doors, "
                f"garage: {self.has_garage}, garden: {self.has_garden}, pool: {self.has_swimming_pool}")

# Builder interface
class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_floors(self, floors):
        self.house.floors = floors
        return self

    def build_windows(self, windows):
        self.house.windows = windows
        return self

    def build_doors(self, doors):
        self.house.doors = doors
        return self

    def add_garage(self):
        self.house.has_garage = True
        return self

    def add_garden(self):
        self.house.has_garden = True
        return self

    def add_swimming_pool(self):
        self.house.has_swimming_pool = True
        return self

    def build(self):
        return self.house

# Director (optional)
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_luxury_house(self):
        return (self.builder
                .build_floors(2)
                .build_windows(10)
                .build_doors(5)
                .add_garage()
                .add_garden()
                .add_swimming_pool()
                .build())

# Usage
builder = HouseBuilder()
director = Director(builder)
luxury_house = director.construct_luxury_house()
print(luxury_house)




# Real World Example
# It can be used in building SQL queries, complex UI components, or even constructing different types of documents.

"""

Why (and When) to Use It

✅ Use Builder when:

You have a class with many optional parameters.
Object creation involves complex assembly steps.
You need different representations of the same object (e.g., plain vs. luxury house).

❌ Avoid it when:

The object is simple and easily constructed with a few parameters.
You just want to look “enterprisey” while building a 10-line script.

"""

# Real World Example: Building a SQL Query
class SQLQueryBuilder:
    def __init__(self):
        self._select = []
        self._table = None
        self._where = []
        self._order_by = None

    def select(self, *columns):
        self._select.extend(columns)
        return self

    def from_table(self, table):
        self._table = table
        return self

    def where(self, condition):
        self._where.append(condition)
        return self

    def order_by(self, column):
        self._order_by = column
        return self

    def build(self):
        query = f"SELECT {', '.join(self._select)} FROM {self._table}"
        if self._where:
            query += " WHERE " + " AND ".join(self._where)
        if self._order_by:
            query += f" ORDER BY {self._order_by}"
        return query + ";"

# Usage
query = (
    SQLQueryBuilder()
    .select("id", "name", "email")
    .from_table("users")
    .where("age > 18")
    .where("country = 'India'")
    .order_by("name")
    .build()
)

print(query)




# Real World Example: Building HTTP Requests

class HttpRequest:
    def __init__(self, method, url, headers, params, data):
        self.method = method
        self.url = url
        self.headers = headers
        self.params = params
        self.data = data

    def __str__(self):
        return f"{self.method} {self.url}\nHeaders: {self.headers}\nParams: {self.params}\nData: {self.data}"

class HttpRequestBuilder:
    def __init__(self):
        self.method = "GET"
        self.url = None
        self.headers = {}
        self.params = {}
        self.data = None

    def set_method(self, method):
        self.method = method
        return self

    def set_url(self, url):
        self.url = url
        return self

    def add_header(self, key, value):
        self.headers[key] = value
        return self

    def add_param(self, key, value):
        self.params[key] = value
        return self

    def set_data(self, data):
        self.data = data
        return self

    def build(self):
        return HttpRequest(self.method, self.url, self.headers, self.params, self.data)

# Usage
request = (
    HttpRequestBuilder()
    .set_method("POST")
    .set_url("https://api.example.com/users")
    .add_header("Authorization", "Bearer token123")
    .add_param("verbose", "true")
    .set_data({"name": "Uday", "role": "Engineer"})
    .build()
)

print(request)
