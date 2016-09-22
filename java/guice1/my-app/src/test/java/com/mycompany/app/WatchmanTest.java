// https://github.com/junit-team/junit4/wiki/rules

package com.mycompany.app;

import static org.junit.Assert.fail; 
import org.junit.AssumptionViolatedException; 
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TestRule;
import org.junit.rules.TestWatcher;
import org.junit.runner.Description;
import org.junit.runners.model.Statement;


import com.google.inject.Guice;
import com.google.inject.Inject;
import com.google.inject.Injector;
import com.google.inject.Module;

import com.mycompany.app.DockerUtil;

/*
import java.util.List;

import com.github.dockerjava.api.DockerClient;
import com.github.dockerjava.core.DockerClientBuilder;
import com.github.dockerjava.core.DefaultDockerClientConfig;
// import com.github.dockerjava.api.command.InspectContainerResponse;
import com.github.dockerjava.api.model.Container;
// import com.github.dockerjava.api.model.ExposedPort;
*/


public class WatchmanTest {
  private static String watchedLog = "";


    @Before
    public void doSetup() {
        System.out.println("BEFORE");
    }

    /*
    private DockerClient getDockerClient() {
        final DefaultDockerClientConfig config = DefaultDockerClientConfig.createDefaultConfigBuilder()
                .withRegistryUrl("unix:///var/run/docker.sock").withDockerHost("unix:///var/run/docker.sock")
                .withDockerTlsVerify(false).build();
        return DockerClientBuilder.getInstance(config).build();
    }
    */


  @Rule
  public TestRule watchman = new TestWatcher() {
    @Override
    public Statement apply(Statement base, Description description) {
      return super.apply(base, description);
    }

    @Override
    protected void succeeded(Description description) {
      watchedLog += "\nsucceeded\n" + description.getDisplayName() + " " + "success!\n";
    }

    @Override
    protected void failed(Throwable e, Description description) {
      watchedLog += "\nfailed\n" + description.getDisplayName() + " " + e.getClass().getSimpleName() + "\n";
    }

    @Override
    protected void skipped(AssumptionViolatedException e, Description description) {
      watchedLog += "\nskipped\n" + description.getDisplayName() + " " + e.getClass().getSimpleName() + "\n";
    }

    @Override
    protected void starting(Description description) {
      super.starting(description);
      System.out.println("START\n" + description.getDisplayName() + " starting\n'" + watchedLog + "'\nDONE\n");
    }

    @Override
    protected void finished(Description description) {
      super.finished(description);
      System.out.println("START\n" + description.getDisplayName() + " finished\n'" + watchedLog + "'\nDONE\n");
    }
  };

  @Test
  public void fails() {
    // fail();
  }

  /*
  @Test
  public void succeeds() {
    // abstract: DockerClient client = new DockerClient("unix:///var/run/docker.sock");
    DockerClient client = getDockerClient();
    System.out.println("got docker client");
    final List<Container> containers = client.listContainersCmd().exec();
    for (final Container container : containers) {
        System.out.println("docker client id: " + container.getId());
        System.out.println("docker client command: " + container.getCommand());
        for (final String name : container.getNames()) {
            System.out.println("docker client name: " + name);
        }
    }
  }
  */

    @Test
    public void testDockerUtil() {
        @Inject
        DockerUtil dockerUtil;

        dockerUtil.listContainers();
    }
}
