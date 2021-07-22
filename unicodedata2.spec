#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : unicodedata2
Version  : 13.0.0.post2
Release  : 21
URL      : https://files.pythonhosted.org/packages/b8/db/a5d9a7649c2eb2681c30850617b83e1295c3a5bebcdb05908e1da11ed8b7/unicodedata2-13.0.0.post2.tar.gz
Source0  : https://files.pythonhosted.org/packages/b8/db/a5d9a7649c2eb2681c30850617b83e1295c3a5bebcdb05908e1da11ed8b7/unicodedata2-13.0.0.post2.tar.gz
Summary  : Unicodedata backport for Python 2/3 updated to the latest Unicode version.
Group    : Development/Tools
License  : Apache-2.0
Requires: unicodedata2-license = %{version}-%{release}
Requires: unicodedata2-python = %{version}-%{release}
Requires: unicodedata2-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
unicodedata2
        ============
        
        [unicodedata] backport/updates to Python 3 and Python 2.
        
        The versions of this package match Unicode versions, so unicodedata2==13.0.0 is data from Unicode 13.0.0.
        Additionally this backports support for named aliases and named sequences to Python 2.
        
        Pre-compiled wheel packages are available on [PyPI] and can be installed via pip.

%package license
Summary: license components for the unicodedata2 package.
Group: Default

%description license
license components for the unicodedata2 package.


%package python
Summary: python components for the unicodedata2 package.
Group: Default
Requires: unicodedata2-python3 = %{version}-%{release}

%description python
python components for the unicodedata2 package.


%package python3
Summary: python3 components for the unicodedata2 package.
Group: Default
Requires: python3-core
Provides: pypi(unicodedata2)

%description python3
python3 components for the unicodedata2 package.


%prep
%setup -q -n unicodedata2-13.0.0.post2
cd %{_builddir}/unicodedata2-13.0.0.post2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603407058
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/unicodedata2
cp %{_builddir}/unicodedata2-13.0.0.post2/LICENSE %{buildroot}/usr/share/package-licenses/unicodedata2/c700a8b9312d24bdc57570f7d6a131cf63d89016
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/unicodedata2/c700a8b9312d24bdc57570f7d6a131cf63d89016

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
