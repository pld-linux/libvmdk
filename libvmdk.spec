#
# Conditional build:
%bcond_without	python	# Python (3) bindings
%bcond_without	python3	# CPython 3.x bindings
#
%if %{without python}
%undefine	with_python2
%undefine	with_python3
%endif
# see m4/${libname}.m4 />= for required version of particular library
%define		libbfio_ver		20201125
%define		libcdata_ver		20220115
%define		libcerror_ver		20120425
%define		libcfile_ver		20160409
%define		libclocale_ver		20120425
%define		libcnotify_ver		20120425
%define		libcpath_ver		20180716
%define		libcsplit_ver		20120701
%define		libcthreads_ver		20160404
%define		libfcache_ver		20191109
%define		libfdata_ver		20201129
%define		libfvalue_ver		20200711
%define		libuna_ver		20210801
Summary:	Library to access the VMware Virtual Disk (VMDK) format
Summary(pl.UTF-8):	Biblioteka dostępu do formatu VMware Virtual Disk (VMDK)
Name:		libvmdk
Version:	20231123
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libvmdk/releases
Source0:	https://github.com/libyal/libvmdk/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	5989ffa55f771e794ad0aa19398369ec
URL:		https://github.com/libyal/libvmdk/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libbfio-devel >= %{libbfio_ver}
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcpath-devel >= %{libcpath_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libfcache-devel >= %{libfcache_ver}
BuildRequires:	libfdata-devel >= %{libfdata_ver}
BuildRequires:	libfvalue-devel >= %{libfvalue_ver}
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
%{?with_python3:BuildRequires:	python3-devel >= 1:3.2}
BuildRequires:	zlib-devel >= 1.2.5
Requires:	libbfio >= %{libbfio_ver}
Requires:	libcdata >= %{libcdata_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcfile >= %{libcfile_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcpath >= %{libcpath_ver}
Requires:	libcsplit >= %{libcsplit_ver}
Requires:	libcthreads >= %{libcthreads_ver}
Requires:	libfcache >= %{libfcache_ver}
Requires:	libfdata >= %{libfdata_ver}
Requires:	libfvalue >= %{libfvalue_ver}
Requires:	libuna >= %{libuna_ver}
Requires:	zlib >= 1.2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libvmdk is a library to access the VMware Virtual Disk (VMDK) image
format.

Read supported formats:
- RAW (flat)
- COWD version 1 (sparse)
- VMDK version 1, 2 and 3 (sparse)

Supported VMDK format features:
* delta links
* grain compression (as of version 20131209)
* data markers (as of version 20140416)

VMDK format features not supported at the moment:
- images that use a physical device
- changed block tracking (CBT) (supported by VMDK version 3 (sparse))
 / change tracking file

Work in progress:
- Dokan library support
- Thread-safety in handle API functions

%description -l pl.UTF-8
libvmdk to biblioteka służąca do dostępu do formatu obrazów VMware
Virtual Disk (VMDK).

Obsługuje odczyt formatów:
- RAW (płaski)
- COWD w wersji 1 (rzadki)
- VMDK w wersji 1, 2 i 3 (rzadki)

Obsługiwana funkcjonalność obrazów:
- dowiązania różnic
- kompresja ziarnista (w wersji 20131209)
- znaczniki danych (w wersji 20140416)

Funkcjonalność formatu VMDK obecnie nie obsługiwana:
- obrazy wykorzystujące urządzenia fizyczne
- śledzenie zmienionych bloków (CBT) (obsługiwane przez rzadkie VMDK w
  wersji 3) / pliki śledzenia zmian

W trakcie implementacji:
- obsługa biblioteki Dokan
- obsługa wątków w funkcjach API uchwytów

%package devel
Summary:	Header files for libvmdk library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvmdk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libbfio-devel >= %{libbfio_ver}
Requires:	libcdata-devel >= %{libcdata_ver}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libcfile-devel >= %{libcfile_ver}
Requires:	libclocale-devel >= %{libclocale_ver}
Requires:	libcnotify-devel >= %{libcnotify_ver}
Requires:	libcpath-devel >= %{libcpath_ver}
Requires:	libcsplit-devel >= %{libcsplit_ver}
Requires:	libcthreads-devel >= %{libcthreads_ver}
Requires:	libfcache-devel >= %{libfcache_ver}
Requires:	libfdata-devel >= %{libfdata_ver}
Requires:	libfvalue-devel >= %{libfvalue_ver}
Requires:	libuna-devel >= %{libuna_ver}
Requires:	zlib-devel >= 1.2.5

%description devel
Header files for libvmdk library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvmdk.

%package static
Summary:	Static libvmdk library
Summary(pl.UTF-8):	Statyczna biblioteka libvmdk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libvmdk library.

%description static -l pl.UTF-8
Statyczna biblioteka libvmdk.

%package tools
Summary:	Tools to support the VMware Virtual Disk (VMDK) format
Summary(pl.UTF-8):	Narzędzia obsługujące format VMware Virtual Disk (VMDK)
Group:		Applications/File
Requires:	%{name} = %{version}-%{release}
Requires:	libfuse >= 2.6

%description tools
Tools to support the VMware Virtual Disk (VMDK) format.

%description tools -l pl.UTF-8
Narzędzia obsługujące format VMware Virtual Disk (VMDK).

%package -n python3-pyvmdk
Summary:	Python 3 bindings for libvmdk library
Summary(pl.UTF-8):	Wiązania Pythona 3 do biblioteki libvmdk
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-pyvmdk
Python 3 bindings for libvmdk library.

%description -n python3-pyvmdk -l pl.UTF-8
Wiązania Pythona 3 do biblioteki libvmdk.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON_VERSION=3 \
	%{?with_python3:--enable-python}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvmdk.la

%if %{with python3}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/pyvmdk.{la,a}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libvmdk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvmdk.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvmdk.so
%{_includedir}/libvmdk
%{_includedir}/libvmdk.h
%{_pkgconfigdir}/libvmdk.pc
%{_mandir}/man3/libvmdk.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libvmdk.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vmdkinfo
%attr(755,root,root) %{_bindir}/vmdkmount
%{_mandir}/man1/vmdkinfo.1*

%if %{with python3}
%files -n python3-pyvmdk
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/pyvmdk.so
%endif
