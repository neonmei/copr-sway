# credits: https://git.lab.cowley.tech/chriscowley/copr-sway/src/branch/master/fmt/fmt.spec
# credits: https://github.com/gumieri/copr-sway/blob/master/fmt/fmt.spec

Name:      fmt
Version:   6.0.0
Release:   1%{?dist}
Summary:   Small, safe and fast formatting library for C++

License:	BSD
URL:      https://github.com/fmtlib/fmt
Source0:	%{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  doxygen
BuildRequires:  nodejs-less
BuildRequires:  python3-sphinx
BuildRequires:  python3-breathe

BuildRoot:      %{_tmppath}/%{name}-%{version}-build


%description
%{summary}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header file for using %{name}.


%prep
%autosetup -p1


%build
%cmake
%make_build


%install
%make_install


%files
%defattr(-,root,root)
%doc LICENSE.rst README.rst ChangeLog.rst CONTRIBUTING.md
%{_libdir}/libfmt.so.6*

%files devel
%defattr(-,root,root)
%{_includedir}/fmt
%{_libdir}/cmake/fmt
%{_libdir}/libfmt.so
%{_libdir}/pkgconfig/%{name}.pc
