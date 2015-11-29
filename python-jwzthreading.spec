%define		module	jwzthreading
Summary:	Implementation of algorithm for threading mail messages
Summary(pl.UTF-8):	Implementacja algorytmu wątkowania wiadomości pocztowych
Name:		python-%{module}
Version:	0.91
Release:	5
License:	BSD-like (see LICENSE)
Group:		Libraries/Python
Source0:	http://www.amk.ca/files/python/%{module}-%{version}.tar.gz
# Source0-md5:	567f17b0189d90f570961b8f5d487795
URL:		http://www.amk.ca/python/code/jwz.html
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an implementation of a fast and smart algorithm for threading
mail messages, as described by Jamie Zawinski at
http://www.jwz.org/doc/threading.html .

%description -l pl.UTF-8
Implementacja szybkiego i sprawnego algorytmu wątkowania poczty,
opisana przez Jamie Zawinskiego na stronie
http://www.jwz.org/doc/threading.html .

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_install

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE CHANGES.txt README
%{py_sitescriptdir}/%{module}.py?
