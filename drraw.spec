Summary:	Draw Round Robin Archives on the Web
Summary(pl):	Drraw - rysowanie wykresów RRD na WWW
Name:		drraw
Version:	2.1.3
Release:	0.1
License:	BSD
Group:		Applications/Databases
Source0:	http://web.taranis.org/drraw/dist/%{name}-%{version}.tgz
# Source0-md5:	99466034678b46784fcd4463882b6c8a
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

%description -l pl
drraw jest prostym, opartym na WWW front-endem dla RRDtoola, który
pozwala w sposób interaktywny tworzyæ wykresy wed³ug w³asnego pomys³u.
Definicja wykresu mo¿e byæ zmieniona na szablon, a ten naniesiony 
na wiele plików RRD.

%prep
%setup -q
%patch -p1
sed -i 's@^#! /usr/local/bin/perl@#!/usr/bin/perl@' drraw.cgi

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
%doc CHANGES INSTALL LICENSE README.EVENTS WISHLIST 
%attr(755,root,root) /home/services/html/cgi-bin/drraw.cgi
%attr(755,http,http) /home/services/drraw/
/home/services/html/cgi-bin/icons/*
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) /home/services/html/cgi-bin/drraw.conf
