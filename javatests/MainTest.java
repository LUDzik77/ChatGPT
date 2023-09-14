import org.example.Main;
import org.junit.BeforeClass;
import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;


public class MainTest {

    @BeforeClass
    public static void promptMe(){
        System.out.println("Begin > > tests");
        //return("Andrzej");
    }

    @Before
    public void prompttest(){
        System.out.println("running test ...");
        //return("Andrzej");
    }

    @Test
    public void When_functionIsExecuted_ExpectFirstCapitalLetter(){
        String str = Main.ludwik();
        assertEquals(Character.isUpperCase(str.charAt(0)), true);
    }

    @Test
    public void When_functionIsExecuted_ExpectSpecyficResultReturned(){
        String str = Main.ludwik();
        assertEquals("Ludwik", str);
    }

}
