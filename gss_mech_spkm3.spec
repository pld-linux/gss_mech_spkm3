Summary:	SPKM-3 GSS mechanism implementation
Summary(pl.UTF-8):	Implementacja mechanizmu GSS SPKM-3
Name:		gss_mech_spkm3
Version:	1.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/spkm-tars/gss_mech_spkm.tar.gz
# Source0-md5:	54c99f6a6a69222f0f5faede4b371dbe
Patch0:		%{name}-link.patch
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	libgssglue-devel
BuildRequires:	librpcsecgss-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SPKM-3 GSS mechanism implementation.

%description -l pl.UTF-8
Implementacja mechanizmu GSS SPKM-3.

%package devel
Summary:	Header files for GSS SPKM-3 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GSS SPKM-3
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	db-devel
Requires:	openssl-devel

%description devel
Header files for GSS SPKM-3 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GSS SPKM-3.

%package static
Summary:	Static GSS SPKM-3 library
Summary(pl.UTF-8):	Statyczna biblioteka GSS SPKM-3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GSS SPKM-3 library.

%description static -l pl.UTF-8
Statyczna biblioteka GSS SPKM-3.

%prep
%setup -q -n gss_mechs
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}
install spkm/spkm3/spkm3.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.gss_mechs
%attr(755,root,root) %{_libdir}/libgssapi_spkm3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgssapi_spkm3.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgssapi_spkm3.so
%{_libdir}/libgssapi_spkm3.la
%{_includedir}/spkm3.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libgssapi_spkm3.a
