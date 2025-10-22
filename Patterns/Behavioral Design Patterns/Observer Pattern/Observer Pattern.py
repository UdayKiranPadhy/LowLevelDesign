"""

The Observer design pattern is a behavioral pattern where an object, known as the subject, maintains a list of its
dependents, called observers, that are notified of any state changes, typically by calling one of their methods. This
pattern is often used to implement distributed event handling systems.


Scenario Without Observer Pattern:
Imagine you have a weather monitoring system. In a simplistic design without the
Observer pattern, you might have a WeatherData class that contains temperature, humidity, and pressure data. Now,
let's say you want to display this data on multiple devices: a mobile app, a web application, and a desktop widget.

Without the Observer pattern, each display device needs to constantly poll the WeatherData class for updates. This
creates tight coupling between the WeatherData class and the display devices, and it can be inefficient as devices
might be checking for updates even when there are none.

Applying Observer Pattern: Now, let's apply the Observer pattern to simplify this scenario. We introduce an Observer
interface with an update method. The display devices implement this interface. The WeatherData class maintains a list
of observers and notifies them when its state changes.


In interview you may be asked to implement Amazon Notify Me feature
This is what you are being expected to do:

"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, data):
        pass


class Observables(ABC):
    @abstractmethod
    def add(self, observer: Observer):
        pass

    @abstractmethod
    def remove(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self, data):
        pass


class IPhoneObservables(Observables):
    def __init__(self):
        self.observers = []
        self.data = None

    def add(self, observer: Observer):
        self.observers.append(observer)

    def remove(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.data)

    def get_data(self):
        return self.data

    def set_data(self, data):
        if self.data == 0:
            self.notify()
        self.data = data


class EMailObserver(Observer):
    def __init__(self, email: str, observable: Observables):
        self.email = email
        self.observable = observable

    def update(self, data):
        print("Email: " + self.email + "product in stock")


class MobileObserver(Observer):
    def __init__(self, username: str, observable: Observables):
        self.username = username
        self.observable = observable

    def update(self, data):
        print("Username: " + self.username + "product in stock")


if __name__ == '__main__':
    iphone = IPhoneObservables()

    observer1 = EMailObserver("xyz@gmail.com", iphone)
    observer2 = EMailObserver("abc@gmail.com", iphone)
    observer3 = MobileObserver("xyz", iphone)

    iphone.add(observer1)
    iphone.add(observer2)
    iphone.add(observer3)

    iphone.set_data(0)
    iphone.set_data(1)
