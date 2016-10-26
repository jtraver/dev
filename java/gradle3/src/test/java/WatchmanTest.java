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

import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import java.lang.reflect.Method;

import com.github.dockerjava.api.DockerClient;
import com.github.dockerjava.core.DockerClientBuilder;
import com.github.dockerjava.core.DefaultDockerClientConfig;
// import com.github.dockerjava.api.command.InspectContainerResponse;
import com.github.dockerjava.api.model.Container;
import com.github.dockerjava.api.model.ContainerHostConfig;
import com.github.dockerjava.api.model.ContainerPort;
import com.github.dockerjava.api.model.ContainerNetworkSettings;
import com.github.dockerjava.api.model.ContainerNetwork;
// import com.github.dockerjava.api.model.ExposedPort;


import com.aerospike.client.AerospikeClient;
import com.aerospike.client.cluster.Node;


public class WatchmanTest {
    private DockerClient dockerClient = null;

  private static String watchedLog = "";


    private DockerClient getDockerClient() {
        final DefaultDockerClientConfig config = DefaultDockerClientConfig.createDefaultConfigBuilder()
                .withRegistryUrl("unix:///var/run/docker.sock").withDockerHost("unix:///var/run/docker.sock")
                .withDockerTlsVerify(false).build();
        return DockerClientBuilder.getInstance(config).build();
    }


    private AerospikeClient getAerospikeClient(DockerClient dockerClient) {
        final List<Container> containers = dockerClient.listContainersCmd().exec();
        int port = 999999;
        int start = port;
        String ip = null;
        for (final Container container : containers) {
            port = start;
            ContainerPort containerPorts[] = container.getPorts();
            for (int i = 0; i < containerPorts.length; i++) {
                ContainerPort containerPort = containerPorts[i];
                int p = containerPorts[i].getPrivatePort();
                if (p < port) {
                    port = p;
                }
            }
            // test container does not publish any ports
            if (port == start)
            {
                continue;
            }
            // should verify that network map entry key is 'test-runner'?
            ip = container.getNetworkSettings().getNetworks().entrySet().iterator().next().getValue().getIpAddress();
            if (ip != null) {
                System.out.println("container ip = " + ip);
                System.out.println("port = " + port);
                AerospikeClient asclient1 = new AerospikeClient(ip, port);
                if (asclient1 != null) {
                    return asclient1;
                }
                ip = null;
            }
        }
        return null;
    }


    private Set<String> getUserContainerIds(DockerClient dockerClient) {
        Set<String> ids = new HashSet<>();
        final List<Container> containers = dockerClient.listContainersCmd().exec();
        for (final Container container : containers) {
            for (final String name : container.getNames()) {
                System.out.println("docker container name: " + name);
                if (!name.startsWith("/test_"))
                {
                    ids.add(container.getId());
                }
            }
        }
        return ids;
    }

    private Set<String> getAllContainerIds(DockerClient dockerClient) {
        Set<String> ids = new HashSet<>();
        Class setStringClass = ids.getClass();
        Method setStringClassMethods[] = setStringClass.getMethods();
        System.out.println("Set<String> setStringClassMethods: " + setStringClassMethods);
        for (int i = 0; i < setStringClassMethods.length; i++) {
            Method setStringClassMethod = setStringClassMethods[i];
            System.out.println(i + " Set<String> method " + setStringClassMethod.getName());
        }
        final List<Container> containers = dockerClient.listContainersCmd().exec();
        for (final Container container : containers) {
            System.out.println("container = " + container);
            System.out.println("docker container id: " + container.getId());
            System.out.println("docker container command: " + container.getCommand());
            for (final String name : container.getNames()) {
                System.out.println("docker container name: " + name);
            }
            ids.add(container.getId());
        }
        return ids;
    }


    private Set<String> getUserContainerNames(DockerClient dockerClient) {
        Set<String> names = new HashSet<>();
        final List<Container> containers = dockerClient.listContainersCmd().exec();
        for (final Container container : containers) {
            for (final String name : container.getNames()) {
                if (!name.startsWith("/test_"))
                {
                    names.add(name);
                }
            }
        }
        return names;
    }

    private Set<String> getAllContainerNames(DockerClient dockerClient) {
        Set<String> names = new HashSet<>();
        final List<Container> containers = dockerClient.listContainersCmd().exec();
        for (final Container container : containers) {
            for (final String name : container.getNames()) {
                names.add(name);
            }
        }
        return names;
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
    if (dockerClient == null) {
        dockerClient = getDockerClient();
    }

    System.out.println(" ");
    System.out.println("all container ids");
    Set<String> ids = getAllContainerIds(dockerClient);
    for (final String id : ids) {
        System.out.println("all container id " + id);
    }


    System.out.println(" ");
    System.out.println("aerospike container ids");
    ids = getUserContainerIds(dockerClient);
    for (final String id : ids) {
        System.out.println("aerospike container id " + id);
    }


    System.out.println(" ");
    System.out.println("all container names");
    Set<String> names = getAllContainerNames(dockerClient);
    for (final String name : names) {
        System.out.println("all container name " + name);
    }


    System.out.println(" ");
    System.out.println("aerospike container names");
    names = getUserContainerNames(dockerClient);
    for (final String name : names) {
        System.out.println("aerospike container name " + name);
    }

  }

  @Test
  public void succeeds() {
    // abstract: DockerClient dockerClient = new DockerClient("unix:///var/run/docker.sock");
    if (dockerClient == null) {
        dockerClient = getDockerClient();
    }
    // DockerClient dockerClient = getDockerClient();
    System.out.println("got docker dockerClient");
    Class dockerclass = dockerClient.getClass();
    Method dockermethods[] = dockerclass.getMethods();
    System.out.println("docker dockermethods: " + dockermethods);
    for (int i = 0; i < dockermethods.length; i++) {
        Method dockermethod = dockermethods[i];
        System.out.println(i + " dockerClient method " + dockermethod.getName());
    }
    /*
     * 0 dockerClient method listContainersCmd
     * 1 dockerClient method authCmd
     * 2 dockerClient method infoCmd
     * 3 dockerClient method unpauseContainerCmd
     * 4 dockerClient method eventsCmd
     * 5 dockerClient method statsCmd
     * 6 dockerClient method createVolumeCmd
     * 7 dockerClient method inspectVolumeCmd
     * 8 dockerClient method removeVolumeCmd
     * 9 dockerClient method listVolumesCmd
     * 10 dockerClient method listNetworksCmd
     * 11 dockerClient method inspectNetworkCmd
     * 12 dockerClient method createNetworkCmd
     * 13 dockerClient method removeNetworkCmd
     * 14 dockerClient method connectToNetworkCmd
     * 15 dockerClient method disconnectFromNetworkCmd
     * 16 dockerClient method createImageCmd
     * 17 dockerClient method loadImageCmd
     * 18 dockerClient method searchImagesCmd
     * 19 dockerClient method pullImageCmd
     * 20 dockerClient method pushImageCmd
     * 21 dockerClient method pushImageCmd
     * 22 dockerClient method pingCmd
     * 23 dockerClient method removeImageCmd
     * 24 dockerClient method listImagesCmd
     * 25 dockerClient method inspectImageCmd
     * 26 dockerClient method saveImageCmd
     * 27 dockerClient method createContainerCmd
     * 28 dockerClient method startContainerCmd
     * 29 dockerClient method execCreateCmd
     * 30 dockerClient method inspectContainerCmd
     * 31 dockerClient method removeContainerCmd
     * 32 dockerClient method containerDiffCmd
     * 33 dockerClient method stopContainerCmd
     * 34 dockerClient method killContainerCmd
     * 35 dockerClient method updateContainerCmd
     * 36 dockerClient method renameContainerCmd
     * 37 dockerClient method restartContainerCmd
     * 38 dockerClient method commitCmd
     * 39 dockerClient method buildImageCmd
     * 40 dockerClient method buildImageCmd
     * 41 dockerClient method buildImageCmd
     * 42 dockerClient method topContainerCmd
     * 43 dockerClient method tagImageCmd
     * 44 dockerClient method pauseContainerCmd
     * 45 dockerClient method authConfig
     * 46 dockerClient method waitContainerCmd
     * 47 dockerClient method attachContainerCmd
     * 48 dockerClient method execStartCmd
     * 49 dockerClient method inspectExecCmd
     * 50 dockerClient method logContainerCmd
     * 51 dockerClient method copyArchiveFromContainerCmd
     * 52 dockerClient method copyFileFromContainerCmd
     * 53 dockerClient method copyArchiveToContainerCmd
     * 54 dockerClient method versionCmd
     * 55 dockerClient method withDockerCmdExecFactory
     * 56 dockerClient method getInstance
     * 57 dockerClient method getInstance
     * 58 dockerClient method getInstance
     * 59 dockerClient method close
     * 60 dockerClient method wait
     * 61 dockerClient method wait
     * 62 dockerClient method wait
     * 63 dockerClient method equals
     * 64 dockerClient method toString
     * 65 dockerClient method hashCode
     * 66 dockerClient method getClass
     * 67 dockerClient method notify
     * 68 dockerClient method notifyAll
     * */
    final List<Container> containers = dockerClient.listContainersCmd().exec();
    for (final Container container : containers) {
        System.out.println("container = " + container);
        System.out.println("docker container id: " + container.getId());
        System.out.println("docker container command: " + container.getCommand());
        for (final String name : container.getNames()) {
            System.out.println("docker container name: " + name);
        }
        Class containerclass = container.getClass();
        Method containermethods[] = containerclass.getMethods();
        System.out.println("container containermethods: " + containermethods);
        for (int i = 0; i < containermethods.length; i++) {
            Method containermethod = containermethods[i];
            System.out.println(i + " container method " + containermethod.getName());
        }
        /*
         * 0 container method getCommand
         * 1 container method getNames
         * 2 container method getImageId
         * 3 container method getImage
         * 4 container method getHostConfig
         * 5 container method getCreated
         * 6 container method getPorts
         * 7 container method getSizeRw
         * 8 container method getSizeRootFs
         * 9 container method getNetworkSettings
         * 10 container method getLabels
         * 11 container method getStatus
         * 12 container method equals
         * 13 container method toString
         * 14 container method hashCode
         * 15 container method getId
         * 16 container method wait
         * 17 container method wait
         * 18 container method wait
         * 19 container method getClass
         * 20 container method notify
         * 21 container method notifyAll
         * */
        System.out.println("container names = " + container.getNames());
        System.out.println("container image id = " + container.getImageId());
        System.out.println("container host config = " + container.getHostConfig());
        System.out.println("container ports = " + container.getPorts());
        System.out.println("container network = " + container.getNetworkSettings());
        System.out.println("container labels = " + container.getLabels());
        System.out.println("container status = " + container.getStatus());

        ContainerHostConfig hostConfig = container.getHostConfig();
        Class hostConfigClass = hostConfig.getClass();
        Method hostConfigmethods[] = hostConfigClass.getMethods();
        System.out.println("hostConfig hostConfigmethods: " + hostConfigmethods);
        for (int i = 0; i < hostConfigmethods.length; i++) {
            Method hostConfigmethod = hostConfigmethods[i];
            System.out.println(i + " hostConfig method " + hostConfigmethod.getName());
        }


        ContainerPort containerPorts[] = container.getPorts();
        for (int j = 0; j < containerPorts.length; j++) {
            ContainerPort containerPort = containerPorts[j];
            System.out.println("containerPort = " + containerPort);
            Class portClass = containerPort.getClass();
            Method portmethods[] = portClass.getMethods();
            System.out.println("port portmethods: " + portmethods);
            for (int i = 0; i < portmethods.length; i++) {
                Method portmethod = portmethods[i];
                System.out.println(i + " port method " + portmethod.getName());
            }
            /*
             * port portmethods: [Ljava.lang.reflect.Method;@4158bffc
             * 0 port method withType
             * 1 port method getIp
             * 2 port method withIp
             * 3 port method getPrivatePort
             * 4 port method withPrivatePort
             * 5 port method getPublicPort
             * 6 port method withPublicPort
             * 7 port method equals
             * 8 port method toString
             * 9 port method hashCode
             * 10 port method getType
             * 11 port method wait
             * 12 port method wait
             * 13 port method wait
             * 14 port method getClass
             * 15 port method notify
             * 16 port method notifyAll
             * */
            // System.out.println("container port type = " + containerPort.withType());
            System.out.println("container port get ip = " + containerPort.getIp());
            // System.out.println("container port with ip = " + containerPort.withIP());
            System.out.println("container port getPrivatePort = " + containerPort.getPrivatePort());
            // System.out.println("container port withPrivatePort = " + containerPort.withPrivatePort());
            System.out.println("container port getPublicPort = " + containerPort.getPublicPort());
            // System.out.println("container port withPublicPort = " + containerPort.withPublicPort());
        }

        System.out.println("container network = " + container.getNetworkSettings());
        ContainerNetworkSettings containerNetworkSettings = container.getNetworkSettings();
        Class containerNetworkSettingsClass = containerNetworkSettings.getClass();
        Method containerNetworkSettingsmethods[] = containerNetworkSettingsClass.getMethods();
        System.out.println("containerNetworkSettings containerNetworkSettingsmethods: " + containerNetworkSettingsmethods);
        for (int i = 0; i < containerNetworkSettingsmethods.length; i++) {
            Method containerNetworkSettingsmethod = containerNetworkSettingsmethods[i];
            System.out.println(i + " containerNetworkSettings method " + containerNetworkSettingsmethod.getName());
        }
        /*
         * 0 containerNetworkSettings method getNetworks
         * 1 containerNetworkSettings method withNetworks
         * 2 containerNetworkSettings method equals
         * 3 containerNetworkSettings method toString
         * 4 containerNetworkSettings method hashCode
         * 5 containerNetworkSettings method wait
         * 6 containerNetworkSettings method wait
         * 7 containerNetworkSettings method wait
         * 8 containerNetworkSettings method getClass
         * 9 containerNetworkSettings method notify
         * 10 containerNetworkSettings method notifyAll
         * */
        System.out.println("container networks = " + containerNetworkSettings.getNetworks());
        Map<String, ContainerNetwork> containerNetworkMap = containerNetworkSettings.getNetworks();
        System.out.println("container network map = " + containerNetworkMap);
        for (Map.Entry<String, ContainerNetwork> entry :containerNetworkMap.entrySet())
        {
            System.out.println("container network map entry: " + entry.getKey() + "/" + entry.getValue());
            ContainerNetwork containerNetwork = entry.getValue();
            System.out.println("container network = " + containerNetwork);
            Class containerNetworkclass = containerNetwork.getClass();
            System.out.println("aerospike containerNetworkclass: " + containerNetworkclass);
            Method containerNetworkmethods[] = containerNetworkclass.getMethods();
            System.out.println("aerospike containerNetworkmethods: " + containerNetworkmethods);
            for (int i = 0; i < containerNetworkmethods.length; i++) {
                Method containerNetworkmethod = containerNetworkmethods[i];
                System.out.println(i + " containerNetwork method " + containerNetworkmethod.getName());
            }
            /*
             * 0 containerNetwork method getLinks
             * 1 containerNetwork method getMacAddress
             * 2 containerNetwork method withAliases
             * 3 containerNetwork method withAliases
             * 4 containerNetwork method withIpv4Address
             * 5 containerNetwork method withLinks
             * 6 containerNetwork method withLinks
             * 7 containerNetwork method withMacAddress
             * 8 containerNetwork method getEndpointId
             * 9 containerNetwork method withEndpointId
             * 10 containerNetwork method getGateway
             * 11 containerNetwork method withGateway
             * 12 containerNetwork method getGlobalIPv6Address
             * 13 containerNetwork method withGlobalIPv6Address
             * 14 containerNetwork method getGlobalIPv6PrefixLen
             * 15 containerNetwork method withGlobalIPv6PrefixLen
             * 16 containerNetwork method getIpAddress
             * 17 containerNetwork method getIpamConfig
             * 18 containerNetwork method withIpamConfig
             * 19 containerNetwork method getIpPrefixLen
             * 20 containerNetwork method withIpPrefixLen
             * 21 containerNetwork method getIpV6Gateway
             * 22 containerNetwork method withIpV6Gateway
             * 23 containerNetwork method getNetworkID
             * 24 containerNetwork method withNetworkID
             * 25 containerNetwork method getAliases
             * 26 containerNetwork method equals
             * 27 containerNetwork method toString
             * 28 containerNetwork method hashCode
             * 29 containerNetwork method wait
             * 30 containerNetwork method wait
             * 31 containerNetwork method wait
             * 32 containerNetwork method getClass
             * 33 containerNetwork method notify
             * 34 containerNetwork method notifyAll
             * */
            System.out.println("container network links = " + containerNetwork.getLinks());
            System.out.println("container network mac address = " + containerNetwork.getMacAddress());
            System.out.println("container network end point id = " + containerNetwork.getEndpointId());
            System.out.println("container network gateway = " + containerNetwork.getGateway());
            System.out.println("container network global ipv6 address = " + containerNetwork.getGlobalIPv6Address());
            System.out.println("container network global ipv6 prefix len = " + containerNetwork.getGlobalIPv6PrefixLen());
            System.out.println("container network ip address = " + containerNetwork.getIpAddress());
            System.out.println("container network ipam config = " + containerNetwork.getIpamConfig());
            System.out.println("container network ip prefix len = " + containerNetwork.getIpPrefixLen());
            System.out.println("container network ipv6 gateway = " + containerNetwork.getIpV6Gateway());
            System.out.println("container network network id = " + containerNetwork.getNetworkID());
            System.out.println("container network aliases = " + containerNetwork.getAliases());
        }
    }
    AerospikeClient asclient1 = new AerospikeClient("174.22.0.1", 3000);
    System.out.println("aerospike asclient1: " + asclient1);
    Class asclass = asclient1.getClass();
    System.out.println("aerospike asclass: " + asclass);
    Method asmethods[] = asclass.getMethods();
    System.out.println("aerospike asmethods: " + asmethods);
    for (int i = 0; i < asmethods.length; i++) {
        Method asmethod = asmethods[i];
        System.out.println(i + " asclient1 method " + asmethod.getName());
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

	Node[] nodes = asclient1.getNodes();
	/*
	 * 0 node method hasBatchIndex
	 * 1 node method putConnection
	 * 2 node method closeConnection
	 * 3 node method isActive
	 * 4 node method hasDouble
	 * 5 node method hasReplicasAll
	 * 6 node method hasPeers
	 * 7 node method useNewBatch
	 * 8 node method refresh
	 * 9 node method getConnection
	 * 10 node method equals
	 * 11 node method toString
	 * 12 node method hashCode
	 * 13 node method getAddress
	 * 14 node method getName
	 * 15 node method close
	 * 16 node method getHost
	 * 17 node method wait
	 * 18 node method wait
	 * 19 node method wait
	 * 20 node method getClass
	 * 21 node method notify
	 * 22 node method notifyAll
	 * */
	for (Node node : nodes) {
        Class nodeClass = node.getClass();
        Method nodeMethods[] = nodeClass.getMethods();
        System.out.println("node nodeMethods: " + nodeMethods);
        for (int i = 0; i < nodeMethods.length; i++) {
            Method nodeMethod = nodeMethods[i];
            System.out.println(i + " node method " + nodeMethod.getName());
        }
	}

	for (Node node : nodes) {
        // System.out.println("node: connection = " + node.getConnection(100));
        System.out.println("node: address = " + node.getAddress());
        System.out.println("node: name = " + node.getName());
        System.out.println("node: host = " + node.getHost());
	}
    final List<String> nodenames1 = asclient1.getNodeNames();
    for (final String nodename : nodenames1) {
        System.out.println("asclient1: nodename = " + nodename);
    }
    AerospikeClient asclient2 = getAerospikeClient(dockerClient);
    if (asclient2 == null) {
        System.out.println("asclient2 = " + asclient2);
    }
    else {
        final List<String> nodenames2 = asclient2.getNodeNames();
        for (final String nodename : nodenames2) {
            System.out.println("asclient2: nodename = " + nodename);
        }
    }
  }
}
