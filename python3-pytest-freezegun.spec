#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Wrap tests with fixtures in freeze_time
Summary(pl.UTF-8):	Obudowywanie testów z wyposażeniem w zamrożonym czasie
Name:		python3-pytest-freezegun
Version:	0.4.2
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-freezegun/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-freezegun/pytest-freezegun-%{version}.zip
# Source0-md5:	ab9915f280a4e37fafc118af1311cc41
URL:		https://pypi.org/project/pytest-freezegun/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-freezegun >= 0.3
BuildRequires:	python3-pytest >= 3.0.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wrap tests with fixtures in freeze_time.

%description -l pl.UTF-8
Obudowywanie testów z wyposażeniem w czasie zamrożonym przez
freeze_time.

%prep
%setup -q -n pytest-freezegun-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/pytest_freezegun.py
%{py3_sitescriptdir}/__pycache__/pytest_freezegun.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_freezegun-%{version}-py*.egg-info
