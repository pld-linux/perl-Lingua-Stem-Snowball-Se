#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Lingua
%define		pnam	Snowball-Swedish
Summary:	Lingua::Stem::Snowball::Se - Porter's stemming algorithm for Sweedish
Summary(pl.UTF-8):	Lingua::Stem::Snowball::Se - algorytm Portera określający rdzenie słów dla języka szwedzkiego
Name:		perl-Lingua-Stem-Snowball-Se
Version:	1.2
Release:	2
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	e2ed0f5c2a9fc7e500c61553c4c1e9c9
URL:		http://search.cpan.org/dist/Lingua-Snowball-Swedish/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The stem function takes a scalar as a parameter and stems the word
according to Martin Porter's Swedish stemming algorithm, which can be
found at the Snowball website: http://snowball.tartarus.org/.

%description -l pl.UTF-8
Funkcja określająca rdzenie słów pobiera skalarny parametr i korzysta
z algorytmu dla języka szwedzkiego autorstwa Martina Portera. Algorytm
ten można znaleźć na stronie Snowballa: http://snowball.tartarus.org/.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
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
%attr(755,root,root) %{_bindir}/stemmer-se.pl
%{perl_vendorlib}/Lingua/Stem/Snowball/*.pm
%{_mandir}/man3/*
