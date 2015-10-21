%define keepstatic 1
Name:           gmp-static
Version:        6.0.0
Release:        0
License:        GPL-2.0 and LGPL-3.0+
Summary:        The GNU MP Library
Url:            http://gmplib.org/
Group:          Base/Libraries
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
Source1001: 	gmp.manifest
BuildRequires:  gcc-c++
BuildRequires:  pkg-config

%description
A static binaries for a library for calculating huge numbers (integer and floating point).

%prep
%setup -q
cp %{SOURCE1001} .

%build
export CFLAGS="%{optflags} -fexceptions";
%reconfigure \
         --enable-static \
         --disable-shared \
         --enable-cxx
make %{?_smp_mflags}

%check
# do not disable "make check", FIX THE BUGS!
make check

%install
%make_install


%files
%manifest gmp.manifest
%license COPYINGv2
%doc AUTHORS README NEWS
%doc %{_infodir}/gmp.info*.gz
%{_libdir}/libgmp.a
%{_libdir}/libgmpxx.a
%{_libdir}/pkgconfig/gmp.pc
/usr/include/gmp.h
/usr/include/gmpxx.h
