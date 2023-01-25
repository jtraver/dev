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
    # docker-py          1.10.6
    # docker-pycreds     0.4.0
    version = dockerClient.version()
    print("docker client version = %s" % str(version))
    pinfo(dockerClient)
    # composeClient = client.ClientFromEnv()
    print("\ndc.containers")
    pinfo(dockerClient.containers)
    print("\ndc.containers()")
    pinfo(dockerClient.containers())
    print("\ncontainers")
    for container1 in dockerClient.containers():
        print("  containter1 = %s" % str(container1))
        for k1, v1 in container1.items():
            print("    k1 = %s" % str(k1))
            print("      v1 = %s" % str(v1))
    print("docker client version = %s" % str(version))

main()
