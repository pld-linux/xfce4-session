
# What about two header files? Is there need for devel package?

%define		_snap 20040813

Summary:	XFce Session manager
Summary(pl):	Zarz±dca sesji XFce
Name:		xfce4-session
Version:	4.1.14
Release:	0.%{_snap}.1
License:	BSD
Group:		X11/Applications
Source0:	http://ep09.pld-linux.org/~havner/xfce4/%{name}-%{_snap}.tar.bz2
# Source0-md5:	2f1f1fe6a79a0b62fbcbc542402037e5
URL:		http://www.xfce.org/
BuildRequires:	libxfcegui4-devel >= 4.1.24
BuildRequires:	libxfce4mcs-devel >= 4.1.1
BuildRequires:	xfce-mcs-manager-devel >= 4.1.0
Requires:	libxfcegui4 >= 4.1.24
Requires:	libxfce4mcs >= 4.1.1
Requires:	xfce-mcs-manager >= 4.1.0
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
rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/splash/engines/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog ChangeLog.pre-xfce-devel NEWS README TODO
%{_mandir}/man1/%{name}.1.*

#%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/*
%attr(755,root,root) %{_bindir}/*
#%attr(4755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%{_sysconfdir}/xdg/%{name}/%{name}.rc

%{_datadir}/themes/*/balou
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*
