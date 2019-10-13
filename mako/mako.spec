%global commit  v1.4
%global gitdate %{nil}
%global gitrel  %{nil}
%global gitver  %{nil}


Name:		mako
Version:	1.4
Release:	1%{?dist}
Summary:	A lightweight notification daemon for Wayland.

License:	MIT
URL:		https://github.com/emersion/mako
Source0:	%{url}/archive/%{commit}.tar.gz#/%{name}-%{version}%{?gitver}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:  systemd-devel
BuildRequires:  wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
BuildRequires:	cairo-devel
BuildRequires:	pango-devel
BuildRequires:	scdoc
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)

%description
%{summary}

%prep
%setup -q


%build
%meson
%meson_build


%install
%meson_install


%files
#doc
%license LICENSE
%{_bindir}/mako
%{_bindir}/makoctl
%{_mandir}/man1/mako.1.gz
%{_mandir}/man1/makoctl.1.gz
%{_datarootdir}/dbus-1/services/fr.emersion.mako.service


%changelog
* Thu Nov 22 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1-1.1
- Added missing build requisite

* Thu Nov 22 2018 Jerzy Drozdz <rpmbuilder@jdsieci.pl> - 1.1-1
- Initial build

