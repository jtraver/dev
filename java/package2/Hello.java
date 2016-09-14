import world.*;
import world.moon.*;

public class Hello {
    public static void main(String[] args) {
        HelloWorld helloWorld = new HelloWorld();
        HelloMoon helloMoon = new HelloMoon();
        helloWorld.hello();
        helloMoon.hello();
    }
}
