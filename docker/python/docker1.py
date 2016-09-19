#!/usr/bin/python

import apihelper
import docker
# import env as env1
import os
import io
import tarfile

def put_file(container, filepath, content):
    """Upload a file to a container."""
    return put_files(container, [(filepath, content)])

def put_files(container, files):
    """Upload files to a container.
    The files parameter is a list of tuples of either:
      - (path, content, mode)
      - (path, content)
    """
    ts = io.BytesIO()
    t = tarfile.TarFile(mode='w', fileobj=ts)
    for ft in files:
        fp = None
        fc = None
        fm = None
        if len(ft) == 3:
            fp, fc, fm = ft
        else:
            fp, fc = ft
        fs = io.BytesIO()
        fs.write(fc)
        fs.seek(0)
        fi = tarfile.TarInfo(name=fp)
        fi.size = len(fs.getvalue())
        if fm:
            fi.mode = fm
        t.addfile(tarinfo=fi, fileobj=fs)
        t.close()
    ts.seek(0)
    return dockerClient.put_archive(container=container, path="/", data=ts)


def pinfo(object):
    print
    print "--------------------------------------------------------------------------------"
    print "| %s" % str(object)
    print "--------------------------------------------------------------------------------"
    apihelper.info(object)


def main():
    global dockerClient
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
            # dockerClient.put_archive(container=container, path="/tmp", data="./archive1.tar")
            put_file(container, 'tmp.tmp', "test tmp.tmp")
    if False:
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
