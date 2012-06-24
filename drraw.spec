Summary:	Draw Round Robin Archives on the Web
Summary(pl):	Drraw Rysowanie wykres�w RRD na www
Name:		drraw
Version:	2.1.1
Release:	0
License:	BSD
Group:		Applications/Databases
Source0:	http://web.taranis.org/drraw/dist/%{name}-%{version}.tgz
#Patch0:		%{name}-perl-install.patch
URL:		http://web.taranis.org/drraw/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
drraw is a simple web based presentation front-end for RRDtool that allows you to interactively build graphs of your own design. A graph definition can be turned into a template which may be applied to many Round Robin Database files. drraw specializes in providing an easy mean of displaying data stored with RRDtool and does not care about how the data is collected, making it a great complement to other RRDtool front-ends.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CONTRIBUTORS README TODO doc/*.html
%attr(755,root,root) %{_bindir}/rrd*
%{perl_vendorlib}/RRDp.pm
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/RRDs
%{perl_vendorarch}/auto/RRDs/RRDs.bs
%attr(755,root,root) %{perl_vendorarch}/auto/RRDs/RRDs.so
%{_mandir}/man1/*
