%global ver 1.0.0
#%global gittag v%{ver}
%global commit 5a30abdf0b3b39ea21298bea91f28924373e4f0b

%global shortcommit %(c=%{commit}; echo ${c:0:7})
%define build_timestamp %(date +"%Y%m%d")
%define snap	%{?commit:.%{build_timestamp}git%{shortcommit}}
%define archive_name	%{?commit}%{!?commit:%{?gittag}}

Name:		kanshi
Version:	%{ver}
Release:	2%{snap}%{?dist}
Summary:	A lightweight dynamic display configuration for Wayland.

License:	MIT
URL:		https://github.com/emersion/kanshi
Source0:	%{url}/archive/%{archive_name}.tar.gz#/%{name}-%{version}%{?snap}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
BuildRequires:	scdoc

%description
%{summary}

%prep
%setup -q -n %{name}-%{archive_name}


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
