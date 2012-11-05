%define keepstatic 1
Name:           gmp
Version:        5.0.5
Release:        0
License:        GPL-3.0+ ; LGPL-3.0+
Summary:        The GNU MP Library
Url:            http://gmplib.org/
Group:          System/Libraries
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRequires:  gcc-c++

%description
A library for calculating huge numbers (integer and floating point).

%package -n libgmp
Summary:        Shared library for the GNU MP Library
Group:          System/Libraries

%description -n libgmp
Shared library for the GNU MP Library.

%package -n libgmpxx
Summary:        C++ bindings for the GNU MP Library
Group:          System/Libraries
Requires:       libgmp = %{version}

%description -n libgmpxx
C++ bindings for the GNU MP Library.

%package -n libmp
Summary:        BSD libmp bindings for the GNU MP Library
Group:          System/Libraries
Requires:       libgmp = %{version}

%description -n libmp
BSD libmp bindings for the GNU MP Library.

%package devel
Summary:        Include Files and Libraries for Development with the GNU MP Library
Group:          Development/Languages/C and C++
Requires:       libgmp = %{version}
Requires:       libgmpxx = %{version}
Requires:       libmp = %{version}

%description devel
These libraries are needed to develop programs which calculate with
huge numbers (integer and floating point).

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fexceptions";
./configure --build=%{_build} --host=%{_host} \
         --program-prefix=%{?_program_prefix} \
         --prefix=%{_prefix} \
         --exec-prefix=%{_exec_prefix} \
         --bindir=%{_bindir} \
         --sbindir=%{_sbindir} \
         --sysconfdir=%{_sysconfdir} \
         --datadir=%{_datadir} \
         --includedir=%{_includedir} \
         --libdir=%{_libdir} \
         --libexecdir=%{_libexecdir} \
         --localstatedir=%{_localstatedir} \
         --sharedstatedir=%{_sharedstatedir} \
         --mandir=%{_mandir} \
         --infodir=%{_infodir} \
         --enable-mpbsd --enable-cxx
make %{?_smp_mflags}

%check
# do not disable "make check", FIX THE BUGS!
make check

%install
%make_install

%post -n libgmp -p /sbin/ldconfig

%post -n libgmpxx -p /sbin/ldconfig

%post -n libmp -p /sbin/ldconfig


%postun -n libgmp -p /sbin/ldconfig

%postun -n libgmpxx -p /sbin/ldconfig

%postun -n libmp -p /sbin/ldconfig

%files
%doc AUTHORS README NEWS

%files -n libgmp
%defattr(-,root,root)
%{_libdir}/libgmp.so.10*

%files -n libgmpxx
%defattr(-,root,root)
%{_libdir}/libgmpxx.so.4*

%files -n libmp
%defattr(-,root,root)
%{_libdir}/libmp.so.3*

%files devel
%defattr(-,root,root)
%doc AUTHORS README NEWS
%doc %{_infodir}/gmp.info*.gz
%{_libdir}/libgmp.a
%{_libdir}/libmp.a
%{_libdir}/libgmpxx.a
%{_libdir}/libgmp.so
%{_libdir}/libgmpxx.so
%{_libdir}/libmp.so
/usr/include/gmp.h
/usr/include/gmpxx.h
/usr/include/mp.h

%changelog
