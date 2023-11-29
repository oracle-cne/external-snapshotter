FROM container-registry.oracle.com/os/oraclelinux:8-slim

COPY rpms /tmp/

RUN rpm -i /tmp/*.rpm &&\
    microdnf clean all &&\
    rm -rf /var/cache/yum/* /tmp/* &&\
    ln -s /usr/share/licenses /LICENSES

ENTRYPOINT ["/usr/bin/csi-snapshotter"]

