// https://github.com/zorzella/guiceberry/blob/master/doc/tutorial/test/junit4/tutorial_1_server/Example1PageObjectsTest.java

package com.mycompany.app;


import com.google.guiceberry.junit4.GuiceBerryRule;
import com.google.inject.Inject;

import org.junit.Rule;
import org.junit.Test;

// import tutorial_1_server.testing.PetStoreEnv0Simple;
// import tutorial_1_server.testing.WelcomeTestPage;
import com.mycompany.app.PetStoreEnv0Simple;
import com.mycompany.app.WelcomeTestPage;

public class Example1PageObjectsTest {

  @Rule
  public GuiceBerryRule guiceBerry = new GuiceBerryRule(PetStoreEnv0Simple.class);

  @Inject
  WelcomeTestPage welcomeTestPage;

  @Test
  public void testPetStoreWelcomeMessage() {
    welcomeTestPage
      .goTo()
      .assertWelcomeMessageIs("Welcome!");
  }

  @Test
  public void testPetStoreTitle() {
    welcomeTestPage
      .goTo()
      .assertTitleIs("Welcome to the pet store");
  }
}
