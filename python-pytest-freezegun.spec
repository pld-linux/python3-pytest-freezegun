#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Wrap tests with fixtures in freeze_time
Summary(pl.UTF-8):	Obudowywanie testów z wyposażeniem w zamrożonym czasie
Name:		python-pytest-freezegun
# keep 0.3.x here for python2 support
Version:	0.3.0.post1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-freezegun/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-freezegun/pytest-freezegun-%{version}.zip
# Source0-md5:	2bf9d50fa0c78d20c193e7ded635bc2f
URL:		https://pypi.org/project/pytest-freezegun/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-freezegun >= 0.3
BuildRequires:	python-pytest >= 3.0.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-freezegun >= 0.3
BuildRequires:	python3-pytest >= 3.0.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wrap tests with fixtures in freeze_time.

%description -l pl.UTF-8
Obudowywanie testów z wyposażeniem w czasie zamrożonym przez
freeze_time.

%package -n python3-pytest-freezegun
Summary:	Wrap tests with fixtures in freeze_time
Summary(pl.UTF-8):	Obudowywanie testów z wyposażeniem w zamrożonym czasie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pytest-freezegun
Wrap tests with fixtures in freeze_time.

%description -n python3-pytest-freezegun -l pl.UTF-8
Obudowywanie testów z wyposażeniem w czasie zamrożonym przez
freeze_time.

%prep
%setup -q -n pytest-freezegun-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/pytest_freezegun.py[co]
%{py_sitescriptdir}/pytest_freezegun-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-freezegun
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pytest_freezegun.py
%{py3_sitescriptdir}/__pycache__/pytest_freezegun.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_freezegun-%{version}-py*.egg-info
%endif
