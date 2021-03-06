// package tutorial_1_server.testing;
package com.mycompany.app;

import com.google.guiceberry.GuiceBerryEnvMain;
import com.google.guiceberry.GuiceBerryModule;
import com.google.guiceberry.TestScoped;
import com.google.inject.AbstractModule;
import com.google.inject.Inject;
import com.google.inject.Module;
import com.google.inject.Provides;
import com.google.inject.Singleton;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.htmlunit.HtmlUnitDriver;

// import tutorial_1_server.prod.PetStoreServer;
// import tutorial_1_server.prod.Pet;
import com.mycompany.app.PetStoreServer;
import com.mycompany.app.Pet;

public final class PetStoreEnv2StaticOverride extends AbstractModule {
  
  @Provides @Singleton
  @PortNumber int getPortNumber() {
    return FreePortFinder.findFreePort();
  }
  
  @Provides @TestScoped
  WebDriver getWebDriver() {
    WebDriver driver = new HtmlUnitDriver();
    return driver;
  }

  @Provides
  @Singleton
  PetStoreServer buildPetStoreServer(@PortNumber int portNumber) {
    PetStoreServer result = new PetStoreServer(portNumber) {
      @Override
      protected Module getPetStoreModule() {
        return new PetStoreModuleWithGlobalStaticOverride();
      }
    };
    return result;
  }
  
  @Override
  protected void configure() {
    install(new GuiceBerryModule());
    bind(GuiceBerryEnvMain.class).to(PetStoreServerStarter.class);
  }
  
  private static final class PetStoreServerStarter implements GuiceBerryEnvMain {

    @Inject
    private PetStoreServer petStoreServer;
    
    public void run() {
      // Starting a server should never be done in a @Provides method 
      // (or inside Provider's get).
      petStoreServer.start();
    }
  }

  public static final class PetStoreModuleWithGlobalStaticOverride 
      extends PetStoreServer.PetStoreModule {

    // !!!HERE!!!!
    public static Pet override;
    
    @Override
    protected Pet calculateFeaturedPet() {
      // !!!HERE!!!!
      if (override != null) {
        return override;
      }
      return super.calculateFeaturedPet();
    }
  }
}
