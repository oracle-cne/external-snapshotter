{{{$version := printf "%s.%s.%s" .major .minor .patch }}}
%if 0%{?with_debug}
# https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global _buildhost build-ol%{?oraclelinux}-%{?_arch}.oracle.com

Name:           external-snapshotter
Version:        {{{ $version }}}
Release:        1%{?dist}
BuildArch:      x86_64
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
make csi-snapshotter

%install
install -m 755 -d %{buildroot}%{_bindir}
install -p -m 755 -t %{buildroot}/%{_bindir} bin/csi-snapshotter

%files
%license LICENSE THIRD_PARTY_LICENSES.txt
%{_bindir}/csi-snapshotter

%changelog
* {{{.changelog_timestamp}}} - {{{$version}}}-1
- Added Oracle specific build files for external-snapshotter.

