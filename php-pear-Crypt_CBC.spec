%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	CBC
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - A class to emulate Perl's Crypt::CBC module
Summary(pl):	%{_pearname} - Klasa emuluj�ca perlowy modu� Crypt::CBC
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A class to emulate Perl's Crypt::CBC module.

%description -l pl
Klasa emuluj�ca perlowy modu� Crypt::CBC.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
