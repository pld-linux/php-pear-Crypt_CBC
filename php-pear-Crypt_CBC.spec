%include	/usr/lib/rpm/macros.php
%define		_pearname	Crypt_CBC
Summary:	Crypt_CBC - A class to emulate Perl's Crypt::CBC module
Summary(pl):	Crypt_CBC - Klasa emuluj±ca perlowy modu³ Crypt::CBC
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A class to emulate Perl's Crypt::CBC module.

%description -l pl
Klasa emuluj±ca perlowy modu³ Crypt::CBC.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/Crypt

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}/Crypt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/Crypt
%{php_pear_dir}/Crypt/*.php
