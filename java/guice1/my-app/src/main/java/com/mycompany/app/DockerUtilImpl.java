package com.mycompany.app;

import java.util.List;

import com.github.dockerjava.api.DockerClient;
import com.github.dockerjava.api.model.Container;

import com.google.inject.Inject;

public class DockerUtilImpl implements DockerUtil {
    private final DockerClient client;

    @Inject
    public DockerUtilImpl(DockerClient client) {
        this.client = client;
    }

    public void listContainers() {
        System.out.println("LIST CONTAINERS");
        final List<Container> containers = client.listContainersCmd().exec();
        for (final Container container : containers) {
            System.out.println("docker client id: " + container.getId());
            System.out.println("docker client command: " + container.getCommand());
            for (final String name : container.getNames()) {
                System.out.println("docker client name: " + name);
            }
        }

    }
}
