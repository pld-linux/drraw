#
# TODO:	move do %{_datadir}/%{name} (use webapps)
#
Summary:	Draw Round Robin Archives on the Web
Summary(pl.UTF-8):	Drraw - rysowanie wykresów RRD na WWW
Name:		drraw
Version:	2.2
Release:	0.b1.1
License:	BSD
Group:		Applications/Databases
Source0:	http://web.taranis.org/drraw/dist/%{name}-%{version}b1.tar.gz
# Source0-md5:	dde40cc5957d0aa82f58fb39a25e68d7
Patch0:		%{name}-conf.patch
URL:		http://web.taranis.org/drraw/
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
drraw is a simple web based presentation front-end for RRDtool that
allows you to interactively build graphs of your own design. A graph
definition can be turned into a template which may be applied to many
Round Robin Database files. drraw specializes in providing an easy
mean of displaying data stored with RRDtool and does not care about
how the data is collected, making it a great complement to other
RRDtool front-ends.

%description -l pl.UTF-8
drraw jest prostym, opartym na WWW front-endem dla RRDtoola, który
pozwala w sposób interaktywny tworzyć wykresy według własnego pomysłu.
Definicja wykresu może być zmieniona na szablon, a ten naniesiony
na wiele plików RRD.

%prep
%setup -q -n %{name}-%{version}b1
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/home/services/html/cgi-bin/icons
install -d $RPM_BUILD_ROOT/home/services/drraw

install drraw.{cgi,conf} $RPM_BUILD_ROOT/home/services/html/cgi-bin
install icons/* $RPM_BUILD_ROOT/home/services/html/cgi-bin/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL LICENSE README.EVENTS
%attr(755,root,root) /home/services/html/cgi-bin/drraw.cgi
%attr(755,http,http) /home/services/drraw/
/home/services/html/cgi-bin/icons/*
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) /home/services/html/cgi-bin/drraw.conf
