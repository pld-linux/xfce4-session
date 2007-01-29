#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Xfce session manager
Summary(pl):	Zarz±dca sesji Xfce
Name:		xfce4-session
Version:	4.4.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	03132946280bae3107101e02fbad0ba8
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce-mcs-manager-devel >= %{version}
BuildRequires:	xfce4-dev-tools >= %{version}
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
Requires:	xfce-mcs-manager >= %{version}
Obsoletes:	xfce4-toys
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-session is the session manager for the Xfce desktop environment.

%description -l pl
xfce4-session jest zarz±dc± sesji dla ¶rodowiska Xfce.

%package libs
Summary:	Xfce Session Manager library
Summary(pl):	Biblioteka zarz±dcy sesji dla ¶rodowiska Xfce
Group:		Libraries

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
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-dbus \
	--enable-session-screenshots \
	%{!?with_static_libs:--disable-static} \
	ICEAUTH=/usr/X11R6/bin/iceauth
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

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

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
%{_sysconfdir}/xdg/autostart/*.desktop
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

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxfsm-*.a
%endif
