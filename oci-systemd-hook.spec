%global provider github
%global provider_tld com
%global project mrunalp
%global repo hooks
%global git0 https://%{provider}.%{provider_tld}/%{project}/%{repo}
%global commit0 ebdb622b137884c71c89d8a61688408ce68fd93e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: oci-systemd-hook
Version: 0.1.3
Release: 3.git%{shortcommit0}%{?dist}
Summary: OCI systemd hook for Docker
License: GPLv3+
URL: %{git0}
Source: %{git0}/archive/%{commit0}/%{repo}-%{shortcommit0}.tar.gz
ExclusiveArch: %{go_arches}
BuildRequires: go-srpm-macros
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: yajl-devel
BuildRequires: libselinux-devel
Requires: docker

%description
OCI systemd %{repo} enable running systemd in a OCI runc/docker container.

%prep
%setup -q -n %{repo}-%{commit0}

%build
autoreconf -i
%configure --libexecdir=/usr/libexec/docker/%{repo}.d/
make %{?_smp_mflags}

%install
%make_install

%files
%if 0%{?fedora} >= 23
%license LICENSE
%else
%doc LICENSE
%doc README.md
%endif
%{_libexecdir}/docker/%{repo}.d/oci_systemd_hook
%{_mandir}/man1/oci_systemd_hook.1*

%changelog
* Thu Dec 10 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1.3-3.gitebdb622
- use separate macro for license when fedora 23 or higher
- update release tag when using git commits

* Thu Dec 10 2015 Lokesh Mandvekar <lsm5@fedoraproject.org> - 0.1.3-2
- spec file cleanup, resolve rpmlint errors
- archful as per docker

* Mon Nov 23 2015 Mrunal Patel <mrunalp@gmail.com> - 0.1.3-1
- Fix bug in man page installation

* Mon Nov 23 2015 Mrunal Patel <mrunalp@gmail.com> - 0.1.2-1
- Add man pages

* Mon Nov 23 2015 Mrunal Patel <mrunalp@gmail.com> - 0.1.1-1
- Initial RPM release
