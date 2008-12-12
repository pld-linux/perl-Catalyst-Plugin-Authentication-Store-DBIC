#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-Authentication-Store-DBIC
Summary:	Authentication and authorization against a DBIx::Class or Class::DBI model
Summary(pl.UTF-8):	Uwierzytelnianie i autoryzacja względem modelu DBIx::Class lub Class::DBI
Name:		perl-Catalyst-Plugin-Authentication-Store-DBIC
Version:	0.11
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7743beb2c7bca430f906b6c04899eade
URL:		http://search.cpan.org/dist/Catalyst-Plugin-Authentication-Store-DBIC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.49
BuildRequires:	perl-Catalyst-Model-DBIC-Schema
BuildRequires:	perl-Catalyst-Plugin-Authentication >= 0.06
BuildRequires:	perl-DBI
BuildRequires:	perl-Set-Object >= 1.14
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin uses a DBIx::Class (or Class::DBI) object to authenticate
a user.

%description -l pl.UTF-8
Ta wtyczka wykorzystuje obiekt DBIx::Class (lub Class:DBI) do
uwierzytelniania użytkownika.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL --skipdeps \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Plugin/Authentication/Store/*.pm
%{perl_vendorlib}/Catalyst/Plugin/Authentication/Store/DBIC
%{_mandir}/man3/*
