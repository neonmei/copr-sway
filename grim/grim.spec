%global ver 1.2.0
%global gittag v%{ver}
#%%global commit 5a30abdf0b3b39ea21298bea91f28924373e4f0b

%global shortcommit %(c=%{commit}; echo ${c:0:7})
%define build_timestamp %(date +"%Y%m%d")
%define snap	%{?commit:.%{build_timestamp}git%{shortcommit}}
%define archive_name	%{?commit}%{!?commit:%{?gittag}}

Name:		grim
Version:	%{ver}
Release:	1%{snap}%{?dist}
Summary:	Grab images from Wayland.

License:	MIT
URL:		https://github.com/emersion/grim
Source0:	%{url}/archive/%{archive_name}.tar.gz#/%{name}-%{version}%{?snap}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols-devel >= 1.14
BuildRequires:	cairo-devel
BuildRequires:	pango-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	scdoc

%description
%{summary}

%prep
%setup -q -n %{name}-%{ver}


%build
%meson
%meson_build


%install
%meson_install


%files
#doc
%license LICENSE
%{_bindir}/grim
%{_mandir}/man1/grim.1.gz
