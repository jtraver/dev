// https://github.com/junit-team/junit4/wiki/rules

// package com.mycompany.app;

import static org.junit.Assert.fail; 
import org.junit.AssumptionViolatedException; 
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.TestRule;
import org.junit.rules.TestWatcher;
import org.junit.runner.Description;
import org.junit.runners.model.Statement;

import java.util.List;
import java.lang.reflect.Method;

import com.github.dockerjava.api.DockerClient;
import com.github.dockerjava.core.DockerClientBuilder;
import com.github.dockerjava.core.DefaultDockerClientConfig;
// import com.github.dockerjava.api.command.InspectContainerResponse;
import com.github.dockerjava.api.model.Container;
// import com.github.dockerjava.api.model.ExposedPort;


import com.aerospike.client.AerospikeClient;


public class WatchmanTest {
  private static String watchedLog = "";


    private DockerClient getDockerClient() {
        final DefaultDockerClientConfig config = DefaultDockerClientConfig.createDefaultConfigBuilder()
                .withRegistryUrl("unix:///var/run/docker.sock").withDockerHost("unix:///var/run/docker.sock")
                .withDockerTlsVerify(false).build();
        return DockerClientBuilder.getInstance(config).build();
    }

/*
    private DockerClient getDockerClient() {
        final DockerClientConfig config = DockerClientConfig.createDefaultConfigBuilder()
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

  @Test
  public void succeeds() {
    // abstract: DockerClient dockerclient = new DockerClient("unix:///var/run/docker.sock");
    DockerClient dockerclient = getDockerClient();
    System.out.println("got docker dockerclient");
    final List<Container> containers = dockerclient.listContainersCmd().exec();
    for (final Container container : containers) {
        System.out.println("docker dockerclient id: " + container.getId());
        System.out.println("docker dockerclient command: " + container.getCommand());
        for (final String name : container.getNames()) {
            System.out.println("docker dockerclient name: " + name);
        }
    }
    AerospikeClient asclient = new AerospikeClient("174.22.0.1", 3000);
    System.out.println("aerospike asclient: " + asclient);
    Class asclass = asclient.getClass();
    System.out.println("aerospike asclass: " + asclass);
    Method asmethods[] = asclass.getMethods();
    System.out.println("aerospike asmethods: " + asmethods);
    for (int i = 0; i < asmethods.length; i++) {
        Method asmethod = asmethods[i];
        System.out.println(i + " " + asmethod.getName());
    }
    /*
     * 
     * 0 getReadPolicyDefault
     * 1 getWritePolicyDefault
     * 2 getScanPolicyDefault
     * 3 getQueryPolicyDefault
     * 4 getBatchPolicyDefault
     * 5 getInfoPolicyDefault
     * 6 getNodes
     * 7 getNodeNames
     * 8 touch
     * 9 getHeader
     * 10 getHeader
     * 11 operate
     * 12 scanAll
     * 13 scanNode
     * 14 scanNode
     * 15 getLargeList
     * 16 getLargeList
     * 17 getLargeList
     * 18 getLargeMap
     * 19 getLargeMap
     * 20 getLargeSet
     * 21 getLargeSet
     * 22 getLargeStack
     * 23 getLargeStack
     * 24 registerUdfString
     * 25 removeUdf
     * 26 queryNode
     * 27 queryAggregate
     * 28 queryAggregate
     * 29 queryAggregateNode
     * 30 createIndex
     * 31 createIndex
     * 32 dropIndex
     * 33 createUser
     * 34 dropUser
     * 35 changePassword
     * 36 grantRoles
     * 37 revokeRoles
     * 38 createRole
     * 39 dropRole
     * 40 grantPrivileges
     * 41 revokePrivileges
     * 42 queryUser
     * 43 queryUsers
     * 44 queryRole
     * 45 queryRoles
     * 46 isConnected
     * 47 prepend
     * 48 add
     * 49 get
     * 50 get
     * 51 get
     * 52 get
     * 53 get
     * 54 put
     * 55 append
     * 56 register
     * 57 register
     * 58 exists
     * 59 exists
     * 60 execute
     * 61 execute
     * 62 delete
     * 63 close
     * 64 query
     * 65 getNode
     * 66 wait
     * 67 wait
     * 68 wait
     * 69 equals
     * 70 toString
     * 71 hashCode
     * 72 getClass
     * 73 notify
     * 74 notifyAll
     * */

    final List<String> nodenames = asclient.getNodeNames();
    for (final String nodename : nodenames) {
        System.out.println(nodename);
    }
  }
}
