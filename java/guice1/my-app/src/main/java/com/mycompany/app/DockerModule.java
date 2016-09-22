package com.mycompany.app;

import com.github.dockerjava.api.DockerClient;
import com.github.dockerjava.core.DockerClientBuilder;
import com.github.dockerjava.core.DefaultDockerClientConfig;
import com.google.inject.AbstractModule;

/**
 * Docker guice bindings.
 *
 */
public class DockerModule extends AbstractModule {

	/*
	 * (non-Javadoc)
	 *
	 * @see com.google.inject.AbstractModule#configure()
	 */
	@Override
	protected void configure() {
		bind(DockerClient.class).toInstance(getDockerClient());
        bind(DockerUtil.class).to(DockerUtilImpl.class);
	}

	/**
	 * @return docker client to use.
	 */
	private DockerClient getDockerClient() {
		final DefaultDockerClientConfig config = DefaultDockerClientConfig.createDefaultConfigBuilder()
				.withRegistryUrl("unix:///var/run/docker.sock").withDockerHost("unix:///var/run/docker.sock")
				.withDockerTlsVerify(false).build();
		return DockerClientBuilder.getInstance(config).build();
	}

}
