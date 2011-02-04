#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Xfce session manager
Summary(pl.UTF-8):	Zarządca sesji Xfce
Name:		xfce4-session
Version:	4.6.2
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.xfce.org/archive/xfce-%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	9d9890130e45e0e9476591ed9ba2c9d5
# Source1-md5:	bf19add3364c0b0d804a7490c1a1fcbe
Source1:	http://www.blues.gda.pl/SOURCES/%{name}-ubuntu_icons.tar.bz2
Patch0:		%{name}-ubuntu_icons.patch
URL:		http://www.xfce.org/projects/xfce4-session/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.12.0
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.6.0
BuildRequires:	xfconf-devel >= %{version}
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-libs = %{version}-%{release}
Requires:	xfce4-dirs >= 4.6
Requires:	xorg-app-iceauth
Obsoletes:	xfce4-toys
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-session is the session manager for the Xfce desktop environment.

%description -l pl.UTF-8
xfce4-session jest zarządcą sesji dla środowiska Xfce.

%package libs
Summary:	Xfce Session Manager library
Summary(pl.UTF-8):	Biblioteka zarządcy sesji dla środowiska Xfce
Group:		X11/Libraries

%description libs
Xfce Session Manager library.

%description libs -l pl.UTF-8
Biblioteka zarządcy sesji dla środowiska Xfce.

%package devel
Summary:	Header files for Xfce Session Manager library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki zarządcy sesji dla środowiska Xfce
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libxfcegui4-devel >= %{version}
Requires:	xfconf-devel >= %{version}

%description devel
Header files for Xfce Session Manager library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki zarządcy sesji dla środowiska Xfce.

%package static
Summary:	Static Xfce Session Manager library
Summary(pl.UTF-8):	Statyczna biblioteka zarządcy sesji dla środowiska Xfce
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Xfce Session Manager library.

%description static -l pl.UTF-8
Statyczna biblioteka zarządcy sesji dla środowiska Xfce.

%prep
%setup -q -a1
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-session-screenshots \
	%{!?with_static_libs:--disable-static} \
	ICEAUTH=/usr/bin/iceauth

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/splash/engines/*.{la,a}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

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
%attr(755,root,root) %{_bindir}/xfce4-session
%attr(755,root,root) %{_bindir}/xfce4-session-logout
%attr(755,root,root) %{_bindir}/xfce4-session-settings
%attr(755,root,root) %{_bindir}/xfce4-tips
%attr(755,root,root) %{_libdir}/balou-export-theme
%attr(755,root,root) %{_libdir}/balou-install-theme
%attr(755,root,root) %{_libdir}/xfsm-shutdown-helper
%dir %{_libdir}/xfce4/splash
%dir %{_libdir}/xfce4/splash/engines
%attr(755,root,root) %{_libdir}/xfce4/splash/engines/*.so
%{_sysconfdir}/xdg/autostart/*.desktop
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-session.xml
%{_datadir}/xfce4/tips

%{_datadir}/themes/Default/balou
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/*.1*

%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*.png
%lang(fr) %{_datadir}/xfce4/doc/fr/*.html
%lang(fr) %{_datadir}/xfce4/doc/fr/images/*.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfsm-4.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfsm-4.6.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfsm-4.6.so
%{_libdir}/libxfsm-4.6.la
%{_includedir}/xfce4/xfce4-session-4.6
%{_pkgconfigdir}/xfce4-session-2.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxfsm-4.6.a
%endif
