%global ver	1.0.0
%global commit	v%{ver}
%global gitdate	%{nil}
%global gitrel	%{nil}
%global gitver	%{nil}


Name:		kanshi
Version:	%{ver}
Release:	1%{?dist}
Summary:	A lightweight dynamic display configuration for Wayland.

License:	MIT
URL:		https://github.com/emersion/kanshi
Source0:	%{url}/archive/%{commit}.tar.gz#/%{name}-%{version}%{?gitver}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
BuildRequires:	scdoc

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
%{_bindir}/kanshi
%{_mandir}/man1/kanshi.1.gz
%{_mandir}/man5/kanshi.5.gz
