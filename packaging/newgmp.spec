%define keepstatic 1
Name:           newgmp
Version:        6.0.0
Release:        0
License:        GPL-2.0 and LGPL-3.0+
Summary:        The GNU MP Library
Url:            http://gmplib.org/
Group:          Base/Libraries
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
Source1001: 	newgmp.manifest
BuildRequires:  gcc-c++
BuildRequires:  pkg-config

%description
A library for calculating huge numbers (integer and floating point).

%package -n libnewgmp
Summary:        Shared library for the GNU MP Library
Group:          Base/Libraries

%description -n libnewgmp
Shared library for the GNU MP Library.

%package -n libnewgmpxx
Summary:        C++ bindings for the GNU MP Library
Group:          Base/Libraries
Requires:       libnewgmp = %{version}

%description -n libnewgmpxx
C++ bindings for the GNU MP Library.

%package devel
Summary:        Include Files and Libraries for Development with the GNU MP Library
Group:          Base/Development
Requires:       libnewgmp = %{version}
Requires:       libnewgmpxx = %{version}

%description devel
These libraries are needed to develop programs which calculate with
huge numbers (integer and floating point).

%prep
%setup -q
cp %{SOURCE1001} .

%build
export CFLAGS="%{optflags} -fexceptions";
%reconfigure \
         --enable-cxx
make %{?_smp_mflags}

%check
# do not disable "make check", FIX THE BUGS!
make check

%install
%make_install

%post -n libnewgmp -p /sbin/ldconfig

%post -n libnewgmpxx -p /sbin/ldconfig

%postun -n libnewgmp -p /sbin/ldconfig

%postun -n libnewgmpxx -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%license COPYINGv2
%doc AUTHORS README NEWS

%files -n libnewgmp
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libgmp.so.10*

%files -n libnewgmpxx
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libgmpxx.so.4*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%doc AUTHORS README NEWS
%doc %{_infodir}/gmp.info*.gz
%{_libdir}/libgmp.a
%{_libdir}/libgmpxx.a
%{_libdir}/libgmp.so
%{_libdir}/libgmpxx.so
%{_libdir}/pkgconfig/gmp.pc
/usr/include/gmp.h
/usr/include/gmpxx.h
