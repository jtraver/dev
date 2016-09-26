// https://github.com/zorzella/guiceberry/blob/master/doc/tutorial/test/junit4/tutorial_0_basic/Example0HelloWorldTest.java

package com.mycompany.app;

import static org.junit.Assert.assertTrue;

import com.google.guiceberry.GuiceBerryModule;
import com.google.guiceberry.junit4.GuiceBerryRule;
import com.google.inject.AbstractModule;

import org.junit.Rule;
import org.junit.Test;

public class Example0HelloWorldTest {

  @Rule
  public final GuiceBerryRule guiceBerry = new GuiceBerryRule(Env.class);

  @Test
  public void testNothing() throws Exception {
    System.out.println("Example0HelloWorldTest.testNothing");
    assertTrue(true);
  }

  public static final class Env extends AbstractModule {
    @Override
    protected void configure() {
      install(new GuiceBerryModule());
    }
  }
}
