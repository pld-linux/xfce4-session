#
# Conditional build:
%bcond_with	static_libs	# don't build static library
#
%define		xfce_version	4.12.0
Summary:	Xfce session manager
Summary(pl.UTF-8):	Zarządca sesji Xfce
Name:		xfce4-session
Version:	4.13.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/%{name}/4.13/%{name}-%{version}.tar.bz2
# Source0-md5:	94eca4dd2280910292abf9692304ce2c
Source1:	http://www.blues.gda.pl/SOURCES/%{name}-ubuntu_icons.tar.bz2
# Source1-md5:	bf19add3364c0b0d804a7490c1a1fcbe
Patch0:		%{name}-ubuntu_icons.patch
URL:		http://www.xfce.org/projects/xfce4-session
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-tools
BuildRequires:	gtk+3-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	systemd-devel
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xfconf-devel >= %{xfce_version}
BuildRequires:	xorg-lib-libSM-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	upower
Requires:	xfce4-dirs >= 4.6
Requires:	xfce-polkit
Requires:	xorg-app-iceauth
Obsoletes:	xfce4-toys
Obsoletes:	xfce-utils
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
Requires:	libxfce4ui-devel >= %{xfce_version}
Requires:	xfconf-devel >= %{xfce_version}

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
	--enable-systemd \
	%{!?with_static_libs:--disable-static} \
	--disable-silent-rules \
	ICEAUTH=/usr/bin/iceauth

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

# just a copy or ur
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ie
# unify
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

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
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/startxfce4
%attr(755,root,root) %{_bindir}/xflock4
%attr(755,root,root) %{_bindir}/xfce4-session
%attr(755,root,root) %{_bindir}/xfce4-session-logout
%attr(755,root,root) %{_bindir}/xfce4-session-settings
%dir %{_libdir}/xfce4/session
%attr(755,root,root) %{_libdir}/xfce4/session/xfsm-shutdown-helper
%{_sysconfdir}/xdg/autostart/*.desktop
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-session.xml
%{_sysconfdir}/xdg/xfce4/Xft.xrdb
%{_sysconfdir}/xdg/xfce4/xinitrc

%{_datadir}/polkit-1/actions/org.xfce.session.policy
%{_datadir}/xsessions/xfce.desktop
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfsm-4.6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxfsm-4.6.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxfsm-4.6.so
#%{_includedir}/xfce4/xfce4-session-4.6
%{_pkgconfigdir}/xfce4-session-2.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxfsm-4.6.a
%endif
