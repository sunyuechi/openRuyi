# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           seastar
Version:        25.05.0
Release:        %autorelease
Summary:        Advanced C++ framework for high-performance server applications
License:        Apache-2.0
URL:            https://seastar.io/
VCS:            git:https://github.com/scylladb/seastar
#!RemoteAsset:  sha256:6e0405706a539af5a0ee307278bbd1fd965a2d97f7c8b970b7daa64d4ddfae11
Source0:        https://github.com/scylladb/seastar/archive/refs/tags/seastar-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DSeastar_API_LEVEL=6
BuildOption(conf):  -DSeastar_DEPRECATED_OSTREAM_FORMATTERS:BOOL=OFF
BuildOption(conf):  -DSeastar_DOCS:BOOL=OFF
BuildOption(conf):  -DSeastar_DPDK:BOOL=OFF
BuildOption(conf):  -DSeastar_INSTALL:BOOL=ON
BuildOption(conf):  -DSeastar_TESTING:BOOL=ON

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libpciaccess-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(hwloc)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(liburing) >= 2.0
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  python3-pyyaml
BuildRequires:  ragel
BuildRequires:  systemtap-sdt-devel
BuildRequires:  xfsprogs-devel

Provides:       %{name}-libs = %{version}-%{release}

%patchlist
# https://github.com/scylladb/seastar/pull/3047
0001-util-adapt-to-fmt-12.0.0-API-changes.patch
# libstdc++ 16 / C++26 stream insertion concept + boost-test 1.89 print_helper
# break BOOST_CHECK_EQUAL on std::vector<T>. Not yet sent upstream.
0002-tests-avoid-printing-std-vector-in-BOOST_CHECK_EQUAL.patch
# https://github.com/scylladb/seastar/commit/2cbe79c66228
# Fixes scylladb/seastar#3413 (ragel 6.10 -G2 + unsigned-char default char
# on aarch64/riscv64 wrongly rejects obs_text 0x80..0xff in HTTP headers).
0003-http-declare-unsigned-char-alphabet-in-ragel-parsers.patch
# Initial RISC-V port: cache_line_size, huge_page_size, cpu_relax (Zihintpause),
# SIGSEGV PC extraction, .cfi_undefined ra. Not yet sent upstream.
2000-core-util-add-initial-RISC-V-port.patch

%description
Seastar is an advanced, open-source C++ framework for high-performance
server applications on modern hardware. Seastar uses a shared-nothing
model that shards all requests onto individual cores, communicating via
explicit message passing instead of locks and atomic instructions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       lksctp-tools-devel
Requires:       pkgconfig(fmt)
Requires:       pkgconfig(gnutls)
Requires:       pkgconfig(hwloc)
Requires:       pkgconfig(libcares)
Requires:       pkgconfig(liblz4)
Requires:       pkgconfig(liburing)
Requires:       pkgconfig(protobuf)
Requires:       pkgconfig(yaml-cpp)

%description    devel
This package contains the header files, libraries, pkg-config and CMake
configuration files for developing applications that use Seastar.

%prep
# GitHub archive expands to seastar-seastar-<ver>/, override the autosetup name.
%autosetup -n %{name}-%{name}-%{version} -p1

%check
# Tests require host sysctl tuning (fs.aio-max-nr, kernel.perf_event_paranoid),
# /dev/shm 1777 bind, and public-network access (dns/tls tests), none of which
# the OBS chroot can provide. Validation is done manually on sg2044_recv.

%files
%license LICENSE NOTICE
%doc README.md HACKING.md
# Upstream CMake ships unversioned .so without SONAME.
%{_libdir}/libseastar.so
%{_libdir}/libseastar_testing.so
%{_libdir}/libseastar_perf_testing.so
%{_bindir}/seastar-json2code.py

%files devel
%{_includedir}/seastar/
%{_libdir}/cmake/Seastar/
%{_libdir}/pkgconfig/seastar.pc
%{_libdir}/pkgconfig/seastar-testing.pc

%changelog
%autochangelog
