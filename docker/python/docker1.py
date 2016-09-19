#!/usr/bin/python

import apihelper
import docker


def pinfo(object):
    print
    print "--------------------------------------------------------------------------------"
    print "| %s" % str(object)
    print "--------------------------------------------------------------------------------"
    apihelper.info(object)


def main():
    pinfo(docker)
    dockerClient = docker.Client(base_url='unix://var/run/docker.sock')
    pinfo(dockerClient)
    # composeClient = client.ClientFromEnv()
    containers = dockerClient.containers(all=True)
    pinfo(containers)
    count = 0
    for container in containers:
        pinfo(container)
        count += 1
        print
        print "container %s" % str(count)
        running = False
        for k1,v1 in container.items():
            print "%s %s" % (str(k1), str(v1))
            # State running
            if k1 == 'State' and v1 == 'running':
                running = True
        if running:
            print "container is up and running"
            

main()
