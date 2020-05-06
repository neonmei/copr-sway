%global ver 1.1.0
%global gittag v%{ver}
%global commit 846b725637840fd41aaa252d457392758197e1d8

%global shortcommit          %(c=%{commit}; echo ${c:0:7})
%define build_timestamp      %(date +"%Y%m%d")
%define snap                 %{?commit:.%{build_timestamp}git%{shortcommit}}
%define archive_name         %{?commit}%{!?commit:%{?gittag}}

Name:		kanshi
Version:	%{ver}
Release:	1%{snap}%{?dist}
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
%setup -q -n %{name}-%{!?commit:%{ver}}%{?commit}


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
