%define upstream_name    Apache2-ModSSL
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version 0.10
Release:	1

Summary:	Apache2::ModSSL - a Perl Interface to mod_ssl functions
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/O/OP/OPI/Apache2-ModSSL-0.10.tar.gz

BuildRequires:	perl-devel
BuildRequires:	apache-devel
BuildRequires:	apache-mod_perl
BuildRequires:	apache-mod_perl-devel
BuildRequires:	apache-mod_ssl

%description
Perl interface to mod_ssl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
#%{__perl} Makefile.PL INC="-I`%{_sbindir}/apxs -q INCLUDEDIR` `apr-1-config --includes` `apu-1-config --includes`" INSTALLDIRS=vendor
%__perl Makefile.PL -apxs %{_bindir}/apxs INSTALLDIRS=vendor
%make

#export APACHE_TEST_HTTPD="%{_sbindir}/httpd"
#make test

%install
%makeinstall_std

%files
%doc Changes README
%dir %{perl_vendorlib}/*/auto/Apache2/ModSSL
%{perl_vendorlib}/*/auto/Apache2/ModSSL/ModSSL.so
%{perl_vendorlib}/*/Apache2/ModSSL.pm
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.80.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1
+ Revision: 684736
- update to new version 0.08

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.70.0-3
+ Revision: 680464
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 555666
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 402971
- rebuild using %%perl_convert_version

* Fri Nov 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdv2009.1
+ Revision: 300643
- nouvelle version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.06-2mdv2009.0
+ Revision: 268367
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2009.0
+ Revision: 195210
- new version

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 0.03-3mdv2008.1
+ Revision: 151815
- rebuild

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-2mdv2008.1
+ Revision: 138099
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-1mdv2007.0
+ Revision: 73256
- import perl-Apache2-ModSSL-0.03-1mdv2007.0

* Thu Sep 14 2006 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdv2007.0
- rebuild
- disable the tests for now

* Sat Jul 16 2005 Oden Eriksson <oeriksson@mandriva.com> 0.03-1mdk
- initial Mandriva package


