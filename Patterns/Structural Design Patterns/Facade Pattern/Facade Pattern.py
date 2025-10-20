"""

The Facade Pattern provides a simplified interface to a complex subsystem of classes, libraries, or APIs.

When you call a shop to place a phone order, an operator is your facade to all services and departments of the shop. 
The operator provides you with a simple voice interface to the ordering system, payment gateways, and various delivery services.




Example in Python: Home Theater System

You’re designing a home theater automation program.
Without a facade, your “watch movie” operation might look like this:

projector.on()
projector.set_input("HDMI1")
amplifier.on()
amplifier.set_volume(20)
lights.dim()
player.on()
player.play("Inception.mp4")


That’s... a lot of ceremony.

Now let’s fix it using the Facade Pattern.

"""

class Amplifier:
    def on(self): print("Amplifier: Power on")
    def set_volume(self, level): print(f"Amplifier: Setting volume to {level}")

class Projector:
    def on(self): print("Projector: Power on")
    def set_input(self, source): print(f"Projector: Input set to {source}")

class Lights:
    def dim(self): print("Lights: Dimming to 30%")
    def on(self): print("Lights: Turning on to full brightness")

class MediaPlayer:
    def on(self): print("MediaPlayer: Power on")
    def play(self, movie): print(f"MediaPlayer: Playing {movie}")
    def stop(self): print("MediaPlayer: Stopping movie")


class HomeTheaterFacade:
    def __init__(self, amp, projector, lights, player):
        self.amp = amp
        self.projector = projector
        self.lights = lights
        self.player = player

    def watch_movie(self, movie):
        print("\n--- Starting movie mode ---")
        self.lights.dim()
        self.projector.on()
        self.projector.set_input("HDMI1")
        self.amp.on()
        self.amp.set_volume(20)
        self.player.on()
        self.player.play(movie)

    def end_movie(self):
        print("\n--- Shutting down theater ---")
        self.player.stop()
        self.lights.on()



amp = Amplifier()
projector = Projector()
lights = Lights()
player = MediaPlayer()

theater = HomeTheaterFacade(amp, projector, lights, player)

theater.watch_movie("Inception.mp4")
theater.end_movie()
