Summary:	Library for storing and retrieving passwords and other secrets
Name:		libsecret
Version:	0.16
Release:	3
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libsecret/0.16/%{name}-%{version}.tar.xz
# Source0-md5:	321ef07775faed2305da08f989dfa41b
URL:		https://live.gnome.org/Libsecret
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libxslt-progs
BuildRequires:	pkg-config
BuildRequires:	vala-vapigen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsecret is a library for storing and retrieving passwords and other
secrets. It communicates with the "Secret Service" using DBus.
gnome-keyring and KSecretService are both implementations of a Secret
Service.

%package devel
Summary:	Header files for libsecret library
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libgcrypt-devel

%description devel
Header files for libsecret library.

%package apidocs
Summary:	libsecret API documentation
Group:		Documentation

%description apidocs
libsecret API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang libsecret

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f libsecret.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_bindir}/secret-tool
%attr(755,root,root) %ghost %{_libdir}/libsecret-1.so.0
%attr(755,root,root) %{_libdir}/libsecret-1.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib
%{_mandir}/man1/secret-tool.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libsecret-1
%{_libdir}/libsecret-*.so
%{_pkgconfigdir}/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

