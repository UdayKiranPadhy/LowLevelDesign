"""

🧠 The Core Idea

The Iterator Pattern provides a standard way to sequentially access elements in a collection without exposing the collection’s underlying representation.

Instead of forcing the client to know how your data is stored (array, tree, graph, hash map, dark magic), you create an iterator object that knows how to step through it.

It’s the difference between:

You rummaging through someone’s bag to find a pen,
vs.

Them handing you one item at a time, graciously.


Real-World Analogy

Think of a remote control flipping through TV channels.
You don’t care if the channels come from cable, satellite, or streaming — you just press next() or previous() and enjoy the show.
That remote is the iterator, hiding the underlying complexity of how channels are stored or fetched.

Client
   ↓
Iterator Interface → Concrete Iterator
   ↑
Aggregate Interface → Concrete Collection


Iterator: Defines methods like next(), has_next().

Concrete Iterator: Implements iteration logic for a specific collection.

Aggregate (Collection): Provides a factory method create_iterator().

Client: Uses the iterator to traverse the collection.

Example in Python: Custom Playlist Iterator

Let’s imagine you’re building a music player app and want to iterate through songs.

Step 1: The Collection (Aggregate)
"""
class Playlist:
    def __init__(self):
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)

    def create_iterator(self):
        return PlaylistIterator(self._songs)

# Step 2: The Iterator Interface and Concrete Iterator
class PlaylistIterator:
    def __init__(self, songs):
        self._songs = songs
        self._index = 0

    def has_next(self):
        return self._index < len(self._songs)

    def next(self):
        if not self.has_next():
            raise StopIteration("End of playlist")
        song = self._songs[self._index]
        self._index += 1
        return song

# Step 3 : The Client
playlist = Playlist()
playlist.add_song("Hotel California")
playlist.add_song("Bohemian Rhapsody")
playlist.add_song("Stairway to Heaven")

iterator = playlist.create_iterator()

while iterator.has_next():
    print("Now playing:", iterator.next())

"""

Now playing: Hotel California
Now playing: Bohemian Rhapsody
Now playing: Stairway to Heaven

"""



"""


🧩 Real-World Uses

Database Cursors
Iterating over query results one record at a time.

File I/O
Reading lines from a file using for line in file.

Streaming APIs
Consuming paginated or streaming data iteratively.

Tree Traversal
Iterators make recursive structures (DOM trees, ASTs) easier to traverse.

Collections in Frameworks
Frameworks like Django, Flask, Pandas — they all rely on iterator protocols under the hood.

"""