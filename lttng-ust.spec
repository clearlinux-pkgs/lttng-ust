#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: ab27b0e
#
# Source0 file verified with key 0x17280A9781186ACF (mathieu.desnoyers@efficios.com)
#
Name     : lttng-ust
Version  : 2.13.7
Release  : 20
URL      : https://lttng.org/files/lttng-ust/lttng-ust-2.13.7.tar.bz2
Source0  : https://lttng.org/files/lttng-ust/lttng-ust-2.13.7.tar.bz2
Source1  : https://lttng.org/files/lttng-ust/lttng-ust-2.13.7.tar.bz2.asc
Summary  : The LTTng Userspace Tracer (UST) is a library accompanied by a set of tools to trace userspace code.
Group    : Development/Tools
License  : LGPL-2.1
Requires: lttng-ust-bin = %{version}-%{release}
Requires: lttng-ust-lib = %{version}-%{release}
Requires: lttng-ust-license = %{version}-%{release}
Requires: lttng-ust-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : buildreq-configure
BuildRequires : cmake
BuildRequires : grep
BuildRequires : numactl-dev
BuildRequires : pkgconfig(liburcu)
BuildRequires : sed
BuildRequires : xmlto
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Require-liburcu-at-build-time.patch

%description
To build the examples from the source tree, the BUILD_EXAMPLES_FROM_TREE
environment variable must be defined. This will ensure the examples'
Makefiles use the source tree's public header files and binaries.

%package bin
Summary: bin components for the lttng-ust package.
Group: Binaries
Requires: lttng-ust-license = %{version}-%{release}

%description bin
bin components for the lttng-ust package.


%package dev
Summary: dev components for the lttng-ust package.
Group: Development
Requires: lttng-ust-lib = %{version}-%{release}
Requires: lttng-ust-bin = %{version}-%{release}
Provides: lttng-ust-devel = %{version}-%{release}
Requires: lttng-ust = %{version}-%{release}

%description dev
dev components for the lttng-ust package.


%package doc
Summary: doc components for the lttng-ust package.
Group: Documentation
Requires: lttng-ust-man = %{version}-%{release}

%description doc
doc components for the lttng-ust package.


%package lib
Summary: lib components for the lttng-ust package.
Group: Libraries
Requires: lttng-ust-license = %{version}-%{release}

%description lib
lib components for the lttng-ust package.


%package license
Summary: license components for the lttng-ust package.
Group: Default

%description license
license components for the lttng-ust package.


%package man
Summary: man components for the lttng-ust package.
Group: Default

%description man
man components for the lttng-ust package.


%prep
%setup -q -n lttng-ust-2.13.7
cd %{_builddir}/lttng-ust-2.13.7
%patch -P 1 -p1
pushd ..
cp -a lttng-ust-2.13.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1704922546
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1704922546
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lttng-ust
cp %{_builddir}/lttng-ust-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/lttng-ust/c39d4570996f6e319110b282ee8bffde6cebdfce || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lttng-gen-tp

%files dev
%defattr(-,root,root,-)
/usr/include/lttng/tp/lttng-ust-tracef.h
/usr/include/lttng/tp/lttng-ust-tracelog.h
/usr/include/lttng/tracef.h
/usr/include/lttng/tracelog.h
/usr/include/lttng/tracepoint-event.h
/usr/include/lttng/tracepoint-rcu.h
/usr/include/lttng/tracepoint-types.h
/usr/include/lttng/tracepoint.h
/usr/include/lttng/urcu/pointer.h
/usr/include/lttng/urcu/static/pointer.h
/usr/include/lttng/urcu/static/urcu-ust.h
/usr/include/lttng/urcu/urcu-ust.h
/usr/include/lttng/ust-abi.h
/usr/include/lttng/ust-api-compat.h
/usr/include/lttng/ust-arch.h
/usr/include/lttng/ust-cancelstate.h
/usr/include/lttng/ust-clock.h
/usr/include/lttng/ust-common.h
/usr/include/lttng/ust-compiler.h
/usr/include/lttng/ust-config.h
/usr/include/lttng/ust-ctl.h
/usr/include/lttng/ust-endian.h
/usr/include/lttng/ust-error.h
/usr/include/lttng/ust-events.h
/usr/include/lttng/ust-fork.h
/usr/include/lttng/ust-getcpu.h
/usr/include/lttng/ust-libc-wrapper.h
/usr/include/lttng/ust-ringbuffer-context.h
/usr/include/lttng/ust-sigbus.h
/usr/include/lttng/ust-thread.h
/usr/include/lttng/ust-tracepoint-event-nowrite.h
/usr/include/lttng/ust-tracepoint-event-reset.h
/usr/include/lttng/ust-tracepoint-event-write.h
/usr/include/lttng/ust-tracepoint-event.h
/usr/include/lttng/ust-tracer.h
/usr/include/lttng/ust-utils.h
/usr/include/lttng/ust-version.h
/usr/lib64/liblttng-ust-common.so
/usr/lib64/liblttng-ust-ctl.so
/usr/lib64/liblttng-ust-cyg-profile-fast.so
/usr/lib64/liblttng-ust-cyg-profile.so
/usr/lib64/liblttng-ust-dl.so
/usr/lib64/liblttng-ust-fd.so
/usr/lib64/liblttng-ust-fork.so
/usr/lib64/liblttng-ust-libc-wrapper.so
/usr/lib64/liblttng-ust-pthread-wrapper.so
/usr/lib64/liblttng-ust-tracepoint.so
/usr/lib64/liblttng-ust.so
/usr/lib64/pkgconfig/lttng-ust-ctl.pc
/usr/lib64/pkgconfig/lttng-ust.pc
/usr/share/man/man3/do_tracepoint.3
/usr/share/man/man3/lttng-ust-cyg-profile.3
/usr/share/man/man3/lttng-ust-dl.3
/usr/share/man/man3/lttng-ust.3
/usr/share/man/man3/lttng_ust_do_tracepoint.3
/usr/share/man/man3/lttng_ust_tracef.3
/usr/share/man/man3/lttng_ust_tracelog.3
/usr/share/man/man3/lttng_ust_tracepoint.3
/usr/share/man/man3/lttng_ust_tracepoint_enabled.3
/usr/share/man/man3/lttng_ust_vtracef.3
/usr/share/man/man3/lttng_ust_vtracelog.3
/usr/share/man/man3/tracef.3
/usr/share/man/man3/tracelog.3
/usr/share/man/man3/tracepoint.3
/usr/share/man/man3/tracepoint_enabled.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/lttng\-ust/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/liblttng-ust-common.so.1.0.0
/V3/usr/lib64/liblttng-ust-ctl.so.5.0.0
/V3/usr/lib64/liblttng-ust-cyg-profile-fast.so.1.0.0
/V3/usr/lib64/liblttng-ust-cyg-profile.so.1.0.0
/V3/usr/lib64/liblttng-ust-dl.so.1.0.0
/V3/usr/lib64/liblttng-ust-fd.so.1.0.0
/V3/usr/lib64/liblttng-ust-fork.so.1.0.0
/V3/usr/lib64/liblttng-ust-libc-wrapper.so.1.0.0
/V3/usr/lib64/liblttng-ust-pthread-wrapper.so.1.0.0
/V3/usr/lib64/liblttng-ust-tracepoint.so.1.0.0
/V3/usr/lib64/liblttng-ust.so.1.0.0
/usr/lib64/liblttng-ust-common.so.1
/usr/lib64/liblttng-ust-common.so.1.0.0
/usr/lib64/liblttng-ust-ctl.so.5
/usr/lib64/liblttng-ust-ctl.so.5.0.0
/usr/lib64/liblttng-ust-cyg-profile-fast.so.1
/usr/lib64/liblttng-ust-cyg-profile-fast.so.1.0.0
/usr/lib64/liblttng-ust-cyg-profile.so.1
/usr/lib64/liblttng-ust-cyg-profile.so.1.0.0
/usr/lib64/liblttng-ust-dl.so.1
/usr/lib64/liblttng-ust-dl.so.1.0.0
/usr/lib64/liblttng-ust-fd.so.1
/usr/lib64/liblttng-ust-fd.so.1.0.0
/usr/lib64/liblttng-ust-fork.so.1
/usr/lib64/liblttng-ust-fork.so.1.0.0
/usr/lib64/liblttng-ust-libc-wrapper.so.1
/usr/lib64/liblttng-ust-libc-wrapper.so.1.0.0
/usr/lib64/liblttng-ust-pthread-wrapper.so.1
/usr/lib64/liblttng-ust-pthread-wrapper.so.1.0.0
/usr/lib64/liblttng-ust-tracepoint.so.1
/usr/lib64/liblttng-ust-tracepoint.so.1.0.0
/usr/lib64/liblttng-ust.so.1
/usr/lib64/liblttng-ust.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lttng-ust/c39d4570996f6e319110b282ee8bffde6cebdfce

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lttng-gen-tp.1
