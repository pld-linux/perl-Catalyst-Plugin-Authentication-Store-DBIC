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
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DK/DKAMHOLZ/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	796f4b369f3717fc289126f6758a7ba9
URL:		http://search.cpan.org/dist/Catalyst-Plugin-Authentication-Store-DBIC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.49
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
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Plugin/Authentication/Store/*.pm
%{perl_vendorlib}/Catalyst/Plugin/Authentication/Store/DBIC
%{_mandir}/man3/*
