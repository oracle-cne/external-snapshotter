{{{$version := printf "%s.%s.%s" .major .minor .patch }}}
%if 0%{?with_debug}
# https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%{!?registry: %global registry container-registry.oracle.com/olcne}
%global _buildhost	build-ol%{?oraclelinux}-%{?_arch}.oracle.com
%global image_name	csi-snapshotter
%global _name		external-snapshotter

Name:           %{_name}-container-images
Version:        {{{ $version }}}
Release:        1%{?dist}
Summary:        External-snapshotter sidecar application
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/kubernetes-csi/external-snapshotter.git
Source:         %{name}-%{version}.tar.bz2

%description
External-snapshotter watches Kubernetes Snapshot objects and triggers snapshot
creation and deletion against an CSI endpoint.

%prep
%setup -q -n %{name}-%{version}

%build
%global rpm_name %{_name}-%{version}-%{release}.%{_build_arch}
yum clean all && \
  yumdownloader --destdir=${PWD}/rpms %{rpm_name}

%global docker_tag %{registry}/%{image_name}:v%{version}
docker build --pull \
    --build-arg https_proxy=${https_proxy} \
    -t %{docker_tag} -f ./olm/builds/Dockerfile .
docker save -o %{_name}.tar %{docker_tag}

%install
%__install -D -m 644 %{_name}.tar %{buildroot}/usr/local/share/olcne/%{_name}.tar

%files
%license LICENSE THIRD_PARTY_LICENSES.txt
/usr/local/share/olcne/%{_name}.tar

%changelog
* {{{.changelog_timestamp}}} - {{{$version}}}-1
- Added Oracle specific build files for external-snapshotter.

