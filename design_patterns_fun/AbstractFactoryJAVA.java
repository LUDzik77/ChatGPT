package org.example;

interface Accessory {
    String render();
}

class BlueLightSaber implements Accessory {
    @Override
    public String render() {
        return "blue light  sabre";
    }
}

class RedLightSaber implements Accessory {
    @Override
    public String render() {
        return "blue light  sabre";
    }
}

class TheForce implements Accessory {
    @Override
    public String render() {
        return "the FORCE of the purest JEDI in the universe";
    }
}

class DarkForce implements Accessory {
    @Override
    public String render() {
        return "DARK force of one of that filthy Siths!";
    }
}

interface AbstractAccessoryFactory {
    Accessory create_light_saber();
    Accessory create_force();
}


class SithAccessoryFactory implements AbstractAccessoryFactory {
    @Override
    public Accessory create_light_saber() {
        return new RedLightSaber();
    }
    @Override
    public Accessory create_force() {
        return new DarkForce();
    }
}

class JediAccessoryFactory implements AbstractAccessoryFactory {
    @Override
    public Accessory create_light_saber() {
        return new BlueLightSaber();
    }
    @Override
    public Accessory create_force() {
        return new TheForce();
    }
}

class Client {
    public static void main(String[] args) {
        String currentOS = System.getProperty("os.name");

        if (currentOS.startsWith("Windows")) {
            client(new JediAccessoryFactory());
        } else {
            client(new SithAccessoryFactory());
        }
    }

    public static void client(AbstractAccessoryFactory accessoryFactory) {
        Accessory lightsaber = accessoryFactory.create_light_saber();
        Accessory force = accessoryFactory.create_force();
        System.out.println(force.render());
        System.out.println(lightsaber.render());
    }
}