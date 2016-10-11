################################################################################
# test/java:openjdk-8
################################################################################

# Base Image
FROM maven:3-jdk-8

WORKDIR /qe/test

ADD https://services.gradle.org/distributions/gradle-2.8-bin.zip /downloads/

RUN gunzip -dq /downloads/gradle-2.8-bin.zip
RUN apt-get autoremove -y && apt-get clean

