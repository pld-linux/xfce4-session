Summary:	XFce Session manager
Summary(pl):	Zarz±dca sesji XFce
Name:		xfce4-session
Version:	0.1.1
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://troll.2000-plus.pl/SOURCES/%{name}-%{version}.tar.gz
# Source0-md5:	a459bb78022158dfb90d249f4a8753e1
Source1:	xfce4-xsession.desktop
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
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/xfce4.desktop

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog ChangeLog.pre-xfce-devel NEWS README TODO
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/*
%attr(755,root,root) %{_bindir}/*
%attr(4755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%{_datadir}/xfce4/splash
%{_datadir}/xsessions/xfce4.desktop
