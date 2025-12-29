%define oname packageurl_python

Name:		python-packageurl-python
Version:	0.17.6
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/packageurl-python/%{oname}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	A purl aka. Package URL parser and builder
URL:		https://pypi.org/project/packageurl-python/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
A purl aka. Package URL parser and builder

%prep
%autosetup -p1 -n %{oname}-%{version}
# Remove bundled egg-info
rm -rf src/%{oname}.egg-info/
# Remove thirdparty dir
rm -rfv thirdparty/

%files
%doc README.rst
%license mit.LICENSE
%{py_sitedir}/packageurl
%{py_sitedir}/%{oname}-%{version}*.*-info
