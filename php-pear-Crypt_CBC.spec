%include	/usr/lib/rpm/macros.php
%define		_class		Crypt
%define		_subclass	CBC
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - A class to emulate Perl's Crypt::CBC module
Summary(pl):	%{_pearname} - Klasa emuluj±ca perlowy modu³ Crypt::CBC
Name:		php-pear-%{_pearname}
Version:	0.4
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	0463f7e12758b9ae1104af4e357da125
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Crypt_CBC/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A class to emulate Perl's Crypt::CBC module.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa emuluj±ca perlowy modu³ Crypt::CBC.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
