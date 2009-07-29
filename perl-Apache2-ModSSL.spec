%define upstream_name    Apache2-ModSSL
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Apache2::ModSSL - a Perl Interface to mod_ssl functions
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/O/OP/OPI/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	apache-devel
BuildRequires:	apache-mod_perl
BuildRequires:	apache-mod_perl-devel
BuildRequires:	apache-mod_ssl
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Perl interface to mod_ssl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
#%{__perl} Makefile.PL INC="-I`%{_sbindir}/apxs -q INCLUDEDIR` `apr-1-config --includes` `apu-1-config --includes`" INSTALLDIRS=vendor
%{__perl} Makefile.PL -apxs %{_sbindir}/apxs INSTALLDIRS=vendor
%make

#export APACHE_TEST_HTTPD="%{_sbindir}/httpd"
#make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/*/auto/Apache2/ModSSL
%{perl_vendorlib}/*/auto/Apache2/ModSSL/ModSSL.so
%{perl_vendorlib}/*/Apache2/ModSSL.pm
%{_mandir}/*/*
