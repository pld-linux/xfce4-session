#
%define		snap 20040617
#
Summary:	XFce Session manager
Summary(pl):	Zarz±dca sesji XFce
Name:		xfce4-session
Version:	4.1.0
Release:	0.%{snap}.1
License:	BSD
Group:		X11/Applications
Source0:	%{name}-snap-%{snap}.tar.bz2
# Source0-md5:	ba52e510e728447551be7e51bd744f11
URL:		http://www.xfce.org/
BuildRequires:	libxfcegui4-devel >= 3.99.2
BuildRequires:	libxfce4mcs-devel >= 3.99.2
BuildRequires:	xfce-mcs-manager-devel >= 3.99.2
Requires:	libxfcegui4 >= 3.99.2
Requires:	libxfce4mcs >= 3.99.2
Requires:	xfce-mcs-manager >= 3.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce4-session is the session manager for the XFce desktop environment

%description -l pl
xfce4-session jest zarz±dc± sesji dla ¶rodowiska XFce

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog ChangeLog.pre-xfce-devel NEWS README TODO
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/*
%attr(755,root,root) %{_bindir}/*
#%attr(4755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%{_sysconfdir}/xdg/%{name}/%{name}.rc

%{_datadir}/themes/*/xfsm4
%{_desktopdir}/xfce-session-settings.desktop
%{_iconsdir}/hicolor/*/apps/*.png

%{_mandir}/man1/%{name}.1.*
