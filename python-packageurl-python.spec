Name:		python-packageurl-python
Version:	0.17.5
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/packageurl-python/packageurl_python-%{version}.tar.gz
Summary:	A purl aka. Package URL parser and builder
URL:		https://pypi.org/project/packageurl-python/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
A purl aka. Package URL parser and builder

%files
%{py_sitedir}/packageurl
%{py_sitedir}/packageurl_python-*.*-info
