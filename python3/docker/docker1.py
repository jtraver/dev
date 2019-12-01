#!/usr/bin/env python3
#!/usr/bin/python

import apihelper
import docker


def pinfo(object):
    print()
    print("--------------------------------------------------------------------------------")
    print(("| %s" % str(object)))
    print("--------------------------------------------------------------------------------")
    apihelper.info(object)


def main():
    pinfo(docker)
    dockerClient = docker.Client(base_url='unix://var/run/docker.sock')
    pinfo(dockerClient)
    # composeClient = client.ClientFromEnv()

main()
