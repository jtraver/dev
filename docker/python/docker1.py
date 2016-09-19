#!/usr/bin/python

import apihelper
import docker
import env as env1
import os


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
        name = None
        for k1,v1 in container.items():
            print "%s %s" % (str(k1), str(v1))
            # State running
            if k1 == 'State' and v1 == 'running':
                running = True
            # Names [u'/clever_wright']
            elif k1 == 'Names':
                # both of these work
                name = v1[0][1:]
                # name = v1[0]
        if running:
            print "container %s is up and running" % str(name)
            e = dockerClient.exec_create(container=container, cmd="pwd")
            start1 = dockerClient.exec_start(exec_id=e['Id'])
            print "start1 = %s" % str(start1)
            e = dockerClient.exec_create(container=container, cmd="ls")
            start1 = dockerClient.exec_start(exec_id=e['Id'])
            print "start1 = %s" % str(start1)
    env = os.environ
    print
    print "env = %s" % str(env)
    pinfo(env)
    # print "env = %s" % str(env.map())
    PROJECT = env.get("PROJECT_ID")
    # PROJECT = env.map("PROJECT_ID")
    # PROJECT = env.map()
    print "PROJECT = %s" % str(PROJECT)

main()
