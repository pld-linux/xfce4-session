Summary:	Xfce Session manager
Summary(pl):	Zarz±dca sesji Xfce
Name:		xfce4-session
Version:	4.3.90.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/xfce4-session-%{version}.tar.bz2
# Source0-md5:	f0ec9fcc3f6211e105f2f00c847ed1b1
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	xfce4-dev-tools
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libxfce4mcs >= %{version}
Requires:	libxfcegui4 >= %{version}
Requires:	xfce-mcs-manager >= %{version}
Requires:	xorg-app-iceauth
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-session is the session manager for the Xfce desktop environment.

%description -l pl
xfce4-session jest zarz±dc± sesji dla ¶rodowiska Xfce.

%package libs
Summary:	Xfce Session Manager library
Summary(pl):	Biblioteka zarz±dcy sesji dla ¶rodowiska Xfce
Group:		Libraries
Requires:	libxfcegui4 >= %{version}

%description libs
Xfce Session Manager library.

%description libs -l pl
Biblioteka zarz±dcy sesji dla ¶rodowiska Xfce.

%package devel
Summary:	Header files for Xfce Session Manager library
Summary(pl):	Pliki nag³ówkowe biblioteki zarz±dcy sesji dla ¶rodowiska Xfce
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libxfcegui4-devel >= %{version}

%description devel
Header files for Xfce Session Manager library.

%description devel -l pl
Pliki nag³ówkowe biblioteki zarz±dcy sesji dla ¶rodowiska Xfce.

%package static
Summary:	Static Xfce Session Manager library
Summary(pl):	Statyczna biblioteka zarz±dcy sesji dla ¶rodowiska Xfce
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Xfce Session Manager library.

%description static -l pl
Statyczna biblioteka zarz±dcy sesji dla ¶rodowiska Xfce.

%prep
%setup -q
%patch0 -p1

mv -f po/{nb_NO,nb}.po
mv -f po/{pt_PT,pt}.po

%build
%{__libtoolize}
%{__aclocal} -I %{_datadir}/xfce4/dev-tools/m4macros
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	ICEAUTH=/usr/bin/iceauth
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
%{_datadir}/xfce4/tips

%{_datadir}/themes/Default/balou
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/*.1*

%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/C/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*
#%lang(he) %{_datadir}/xfce4/doc/he/*

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
