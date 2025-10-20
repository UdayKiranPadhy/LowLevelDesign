"""

The Core Idea

The Proxy Pattern provides a substitute or placeholder for another object to control access to it.
Basically, you wrap a real object with another object that:
Performs some extra behavior (like logging, caching, or access control)
Then delegates the actual work to the real object behind the scenes

It’s like a friend who answers your phone calls, filters the spam, and only passes through the interesting ones.


Let’s simulate a video streaming app where loading a full video from a remote server is expensive.
"""

from time import sleep

class Video:
    """RealSubject - Represents a heavy resource (actual video file)."""
    def __init__(self, filename):
        self.filename = filename
        self._load_video_from_disk()

    def _load_video_from_disk(self):
        print(f"Loading video '{self.filename}' from disk... (takes time)")
        sleep(2)  # simulate expensive operation
        print(f"Video '{self.filename}' loaded successfully.")

    def play(self):
        print(f"Playing video '{self.filename}'...")


class VideoProxy:
    """Proxy - Controls access to the heavy Video object."""
    def __init__(self, filename):
        self.filename = filename
        self._real_video = None

    def play(self):
        if self._real_video is None:
            print(f"Proxy: Initializing the real video object...")
            self._real_video = Video(self.filename)
        print(f"Proxy: Delegating play() call to the real video object.")
        self._real_video.play()


video = VideoProxy("the_matrix.mp4")

print("Accessing video first time:")
video.play()

print("\nAccessing video second time:")
video.play()


"""

Output:
Accessing video first time:
Proxy: Initializing the real video object...
Loading video 'the_matrix.mp4' from disk... (takes time)
Video 'the_matrix.mp4' loaded successfully.
Proxy: Delegating play() call to the real video object.
Playing video 'the_matrix.mp4'...

Accessing video second time:
Proxy: Delegating play() call to the real video object.
Playing video 'the_matrix.mp4'...

"""
