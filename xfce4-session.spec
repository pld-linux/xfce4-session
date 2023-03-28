%define		xfce_version	4.18.0
Summary:	Xfce session manager
Summary(pl.UTF-8):	Zarządca sesji Xfce
Name:		xfce4-session
Version:	4.18.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://archive.xfce.org/src/xfce/xfce4-session/4.18/%{name}-%{version}.tar.bz2
# Source0-md5:	0362631bae9673f6fc6c579a4eb8e4d9
URL:		https://www.xfce.org/projects/xfce4-session
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-devel >= 1.0.0
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-tools
BuildRequires:	gtk+3-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libwnck-devel
BuildRequires:	libxfce4ui-devel >= 4.18.2
BuildRequires:	libxfce4util-devel >= %{xfce_version}
BuildRequires:	pkgconfig
BuildRequires:	polkit-devel
BuildRequires:	rpmbuild(macros) >= 2.000
BuildRequires:	systemd-devel
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xfconf-devel >= %{xfce_version}
BuildRequires:	xorg-lib-libSM-devel
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	upower
Requires:	xfce-polkit
Requires:	xfce4-dirs >= 4.6
Requires:	xorg-app-iceauth
Obsoletes:	xfce-utils
Obsoletes:	xfce4-session-devel < 4.16.0
Obsoletes:	xfce4-session-libs < 4.16.0
Obsoletes:	xfce4-session-static < 4.16.0
Obsoletes:	xfce4-toys
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-session is the session manager for the Xfce desktop environment.

%description -l pl.UTF-8
xfce4-session jest zarządcą sesji dla środowiska Xfce.

%prep
%setup -q

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

# just a copy or ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK
# unsupported
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{fa_IR,hye,ie}
# unify
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS TODO
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
