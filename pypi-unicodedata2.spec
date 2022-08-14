#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-unicodedata2
Version  : 14.0.0
Release  : 34
URL      : https://files.pythonhosted.org/packages/e8/10/85680b43276df4c485f1f14598681d8fd654aebd52872a8be405607cabaa/unicodedata2-14.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e8/10/85680b43276df4c485f1f14598681d8fd654aebd52872a8be405607cabaa/unicodedata2-14.0.0.tar.gz
Summary  : Unicodedata backport updated to the latest Unicode version.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-unicodedata2-filemap = %{version}-%{release}
Requires: pypi-unicodedata2-lib = %{version}-%{release}
Requires: pypi-unicodedata2-license = %{version}-%{release}
Requires: pypi-unicodedata2-python = %{version}-%{release}
Requires: pypi-unicodedata2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
[![Githun CI Status](https://github.com/fonttools/unicodedata2/workflows/Build%20+%20Deploy/badge.svg)](https://github.com/fonttools/unicodedata2/actions?query=workflow%3A%22Build+%2B+Deploy%22)
[![PyPI](https://img.shields.io/pypi/v/unicodedata2.svg)](https://pypi.org/project/unicodedata2/)

%package filemap
Summary: filemap components for the pypi-unicodedata2 package.
Group: Default

%description filemap
filemap components for the pypi-unicodedata2 package.


%package lib
Summary: lib components for the pypi-unicodedata2 package.
Group: Libraries
Requires: pypi-unicodedata2-license = %{version}-%{release}
Requires: pypi-unicodedata2-filemap = %{version}-%{release}

%description lib
lib components for the pypi-unicodedata2 package.


%package license
Summary: license components for the pypi-unicodedata2 package.
Group: Default

%description license
license components for the pypi-unicodedata2 package.


%package python
Summary: python components for the pypi-unicodedata2 package.
Group: Default
Requires: pypi-unicodedata2-python3 = %{version}-%{release}

%description python
python components for the pypi-unicodedata2 package.


%package python3
Summary: python3 components for the pypi-unicodedata2 package.
Group: Default
Requires: pypi-unicodedata2-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(unicodedata2)

%description python3
python3 components for the pypi-unicodedata2 package.


%prep
%setup -q -n unicodedata2-14.0.0
cd %{_builddir}/unicodedata2-14.0.0
pushd ..
cp -a unicodedata2-14.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656364396
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-unicodedata2
cp %{_builddir}/unicodedata2-14.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-unicodedata2/c700a8b9312d24bdc57570f7d6a131cf63d89016
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-unicodedata2

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-unicodedata2/c700a8b9312d24bdc57570f7d6a131cf63d89016

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
