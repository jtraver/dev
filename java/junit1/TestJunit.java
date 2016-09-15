// http://www.tutorialspoint.com/junit/junit_basic_usage.htm
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestJunit {
    
   String message = "Hello World";  
   MessageUtil messageUtil = new MessageUtil(message);

   @Test
   public void testPrintMessage() {
      // message = "New World";  
      assertEquals(message,messageUtil.printMessage());
   }
}
