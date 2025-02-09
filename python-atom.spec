Name:		python-atom
Version:	0.11.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/atom/atom-%{version}.tar.gz
Summary:	Memory efficient Python objects
URL:		https://pypi.org/project/atom/
License:	BSD
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(cppy)
BuildSystem:	python

%description
Memory efficient Python objects

%prep
%autosetup -p1 -n atom-%{version}

%files
%{py_platsitedir}/atom
%{py_platsitedir}/atom-*.*-info
