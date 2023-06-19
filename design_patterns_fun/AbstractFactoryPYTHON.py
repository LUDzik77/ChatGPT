from abc import ABC, abstractmethod
import platform
# platform is a common example:)

#As no interface in python,  I might be added in the class name
#f.e:  IAccessory   
class Accessory(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class BlueLightSaber(Accessory):
    def render(self) -> str:
        return "render: BLUE lightsaber"

class RedLightSaber(Accessory):
    def render(self) -> str:
        return "render: RED lightsaber"


class DarkForce(Accessory):
    def render(self) -> str:
        return "render: DARK force of one of that filthy Siths!"

class TheForce(Accessory):
    def render(self) -> str:
        return "render: the FORCE of the purest JEDI in the universe"


class AbstractAccessoryFactory():
    @abstractmethod
    def create_light_saber(self) -> Accessory:
        pass

    @abstractmethod
    def create_force(self) -> Accessory:
        pass


class SithAccessoryFactory(AbstractAccessoryFactory):
    def create_light_saber(self) -> Accessory:
        return RedLightSaber()

    def create_force(self) -> Accessory:
        return DarkForce()


class JediAccessoryFactory(AbstractAccessoryFactory):
    def create_light_saber(self) -> Accessory:
        return BlueLightSaber()

    def create_force(self) -> Accessory:
        return TheForce()


#it would be obviously not in the same script; It would import the framwork
def client(accessory_factory: AbstractAccessoryFactory) -> None:
    lightsaber = accessory_factory.create_light_saber()
    force = accessory_factory.create_force()

    print(force.render())
    print(lightsaber.render())


if __name__ == "__main__":
    current_os = platform.system()

    if current_os == "Windows":
        client(JediAccessoryFactory())
    else:
        client(SithAccessoryFactory())
