#credits: https://github.com/gumieri/copr-sway/blob/master/waybar/waybar.spec
#credits: https://git.lab.cowley.tech/chriscowley/copr-sway/src/branch/master/waybar/waybar.spec

%global ver 0.8.0
%global gittag v%{ver}
#global commit 5a30abdf0b3b39ea21298bea91f28924373e4f0b

%global shortcommit %(c=%{commit}; echo ${c:0:7})
%define build_timestamp %(date +"%Y%m%d")
%define snap	%{?commit:.%{build_timestamp}git%{shortcommit}}
%define archive_name	%{?commit}%{!?commit:%{?ver}}

Name:			waybar
Version:	%{ver}
Release:	1%{snap}%{?dist}
Summary:	Wayland bar for Sway

License:	MIT
URL:		https://github.com/Alexays/Waybar
Source0:	%{url}/archive/%{archive_name}.tar.gz#/%{name}-%{version}%{?snap}.tar.gz

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	meson >= 0.47.0

BuildRequires:  fmt-devel >= 5.3.0
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libinput) 
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(spdlog) >= 1.3.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)

Recommends:     fontawesome-fonts

%description
%{summary}.

%prep
%autosetup -p 1 -n Waybar-%{ver}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/xdg/%{name}
%config(noreplace) %{_sysconfdir}/xdg/%{name}/config
%config(noreplace) %{_sysconfdir}/xdg/%{name}/style.css
%{_bindir}/%{name}
