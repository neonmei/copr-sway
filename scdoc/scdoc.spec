Name:		scdoc
Version:	1.10.0
Release:	1%{?dist}
Summary:	scdoc is a simple man page generator for POSIX systems written in C99.

License:	IDontKnow
URL:		https://git.sr.ht/~sircmpwn/scdoc
Source0:	%{url}/archive/%{version}.tar.gz

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	sed
BuildRequires:	glibc-static

%description
%{summary}

%prep
%autosetup


%build
export PREFIX=/
make PREFIX=%{_prefix} %{?_smp_mflags}


%install
%make_install PREFIX=%{_prefix}


%check
make check


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man5/%{name}.5.gz
/usr/lib/pkgconfig/%{name}.pc
%license COPYING
%doc README.md
