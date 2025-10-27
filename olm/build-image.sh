#!/usr/bin/env bash

set -x

CONTAINER_CLI="${CONTAINER_CLI:-podman}"

name="csi-snapshotter"
version="8.3.0"
registry="container-registry.oracle.com/olcne"
docker_tag=${registry}/${name}:v${version}

"${CONTAINER_CLI}" build --pull \
    --build-arg https_proxy=${https_proxy} \
    --build-arg version=${version} \
    --volume /etc/yum.repos.d:/etc/yum.repos.d \
    --tag ${docker_tag} -f ./olm/builds/Dockerfile_csiSnapshotter .

name="snapshot-controller"
docker_tag=${registry}/${name}:v${version}

"${CONTAINER_CLI}" build --pull \
    --build-arg https_proxy=${https_proxy} \
    --build-arg version=${version} \
    --volume /etc/yum.repos.d:/etc/yum.repos.d \
    --tag ${docker_tag} -f ./olm/builds/Dockerfile_snapshotController .
