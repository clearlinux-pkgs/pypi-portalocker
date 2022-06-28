#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE81444E9CE1F695D (wolph@wol.ph)
#
Name     : pypi-portalocker
Version  : 2.4.0
Release  : 21
URL      : https://files.pythonhosted.org/packages/dc/60/9646b57d473d38fd23af22f18dce6baa4d591f37024e0c3dcd2d66814d50/portalocker-2.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/dc/60/9646b57d473d38fd23af22f18dce6baa4d591f37024e0c3dcd2d66814d50/portalocker-2.4.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/dc/60/9646b57d473d38fd23af22f18dce6baa4d591f37024e0c3dcd2d66814d50/portalocker-2.4.0.tar.gz.asc
Summary  : Wraps the portalocker recipe for easy usage
Group    : Development/Tools
License  : Python-2.0
Requires: pypi-portalocker-license = %{version}-%{release}
Requires: pypi-portalocker-python = %{version}-%{release}
Requires: pypi-portalocker-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pywin32)

%description
############################################
portalocker - Cross-platform locking library
############################################

%package license
Summary: license components for the pypi-portalocker package.
Group: Default

%description license
license components for the pypi-portalocker package.


%package python
Summary: python components for the pypi-portalocker package.
Group: Default
Requires: pypi-portalocker-python3 = %{version}-%{release}

%description python
python components for the pypi-portalocker package.


%package python3
Summary: python3 components for the pypi-portalocker package.
Group: Default
Requires: python3-core
Provides: pypi(portalocker)
Requires: pypi(pywin32)

%description python3
python3 components for the pypi-portalocker package.


%prep
%setup -q -n portalocker-2.4.0
cd %{_builddir}/portalocker-2.4.0
pushd ..
cp -a portalocker-2.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656395028
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-portalocker
cp %{_builddir}/portalocker-2.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-portalocker/63e1288b0ebc7a7a559b2939a4f5f9a7ee2e673f
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-portalocker/63e1288b0ebc7a7a559b2939a4f5f9a7ee2e673f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
