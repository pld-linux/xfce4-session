Summary:	XFce Session manager
Summary(pl):	Zarz±dca sesji XFce
Name:		xfce4-session
Version:	4.1.99.1
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a0a08268026c3a2533a59d21403b5fd6
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= 4.1.91
BuildRequires:	libxfcegui4-devel >= 4.1.91
BuildRequires:	xfce-mcs-manager-devel >= 4.1.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libxfce4mcs >= 4.1.91
Requires:	xfce-mcs-manager >= 4.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-session is the session manager for the XFce desktop environment.

%description -l pl
xfce4-session jest zarz±dc± sesji dla ¶rodowiska XFce.

%package libs
Summary:	XFce Session Manager library
Summary(pl):	Biblioteka zarz±dcy sesji dla ¶rodowiska XFce
Group:		Libraries
Requires:	libxfcegui4 >= 4.1.91

%description libs
XFce Session Manager library.

%description libs -l pl
Biblioteka zarz±dcy sesji dla ¶rodowiska XFce.

%package devel
Summary:	Header files for XFce Session Manager library
Summary(pl):	Pliki nag³ówkowe biblioteki zarz±dcy sesji dla ¶rodowiska XFce
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libxfcegui4-devel >= 4.1.91

%description devel
Header files for XFce Session Manager library.

%description devel -l pl
Pliki nag³ówkowe biblioteki zarz±dcy sesji dla ¶rodowiska XFce.

%package static
Summary:	Static XFce Session Manager library
Summary(pl):	Statyczna biblioteka zarz±dcy sesji dla ¶rodowiska XFce
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XFce Session Manager library.

%description static -l pl
Statyczna biblioteka zarz±dcy sesji dla ¶rodowiska XFce.

%prep
%setup -q
%patch0 -p1

mv -f po/{no,nb}.po
mv -f po/{pt_PT,pt}.po

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
# why libxfsm_4_2_la_LIBADD on Cygwin only???
%{__make} \
	libxfsm_4_2_la_LIBADD="\$(LIBX11_LIBS) \$(LIBXFCEGUI4_LIBS)"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/splash/engines/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog ChangeLog.pre-xfce-devel NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/balou-*-theme
%attr(755,root,root) %{_libdir}/xfsm-shutdown-helper
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%dir %{_libdir}/xfce4/splash
%dir %{_libdir}/xfce4/splash/engines
%attr(755,root,root) %{_libdir}/xfce4/splash/engines/*.so
%dir %{_sysconfdir}/xdg/%{name}
%{_sysconfdir}/xdg/%{name}/%{name}.rc

%{_datadir}/themes/Default/balou
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/*.1*

%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfsm-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfsm-*.so
%{_libdir}/libxfsm-*.la
%{_includedir}/xfce4/xfce4-session-*
%{_pkgconfigdir}/xfce4-session-*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxfsm-*.a
