// https://github.com/junit-team/junit4/wiki/rules

package com.mycompany.app;

import static org.junit.Assert.fail; 
import org.junit.AssumptionViolatedException; 
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TestRule;
import org.junit.rules.TestWatcher;
import org.junit.runner.Description;
import org.junit.runners.model.Statement;

import com.github.dockerjava.api.DockerClient;

public class WatchmanTest {
  private static String watchedLog = "";

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
    fail();
  }

  @Test
  public void skips() {
    skip();
  }

  @Test
  public void succeeds() {
    DockerClient client = new DockerClient("unix:///var/run/docker.sock");
  }
}
