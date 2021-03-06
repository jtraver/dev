// https://github.com/zorzella/guiceberry/blob/master/doc/tutorial/test/junit4/tutorial_1_server/Example0HelloServerTest.java

package com.mycompany.app;

import static org.junit.Assert.assertEquals;

import com.google.guiceberry.junit4.GuiceBerryRule;
import com.google.inject.Inject;

import org.junit.Rule;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

// import tutorial_1_server.testing.PetStoreEnv0Simple;
// import tutorial_1_server.testing.PortNumber;
import com.mycompany.app.PetStoreEnv0Simple;
import com.mycompany.app.PortNumber;

public class Example0HelloServerTest {

  @Rule
  public GuiceBerryRule guiceBerry = new GuiceBerryRule(PetStoreEnv0Simple.class);

  @Inject
  WebDriver driver;
  
  @Inject
  @PortNumber int portNumber;

  @Test
  public void testPetStoreWelcome() {
    driver.get("http://localhost:" + portNumber);
    WebElement element = driver.findElement(By.xpath("//div[@id='welcome']"));
    assertEquals("Welcome!", element.getText());
  }

  @Test
  public void testPetStoreTitle() {
    driver.get("http://localhost:" + portNumber);
    assertEquals("Welcome to the pet store", driver.getTitle());
  }
}
