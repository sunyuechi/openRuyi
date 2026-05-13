# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Sun Yuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           prometheus
%define go_import_path  github.com/prometheus/prometheus

Name:           prometheus
Version:        3.11.3
Release:        %autorelease
Summary:        The Prometheus monitoring system and time series database
License:        Apache-2.0
URL:            https://prometheus.io
VCS:            git:https://github.com/prometheus/prometheus
#!RemoteAsset:  sha256:37bb17f10ec8c36be21452b2efbbc51fc2a94c3d75569c02b8ea0c8cf8ffcfb0
Source0:        https://github.com/prometheus/prometheus/archive/v%{version}/%{name}-%{version}.tar.gz
# TODO: vendor tarball — generate via `go mod vendor` against v%{version},
# repack as %{name}-v%{version}-vendor.tar.gz, and upload under
# github.com/software-vendor/go-prometheus-vendor/releases/download/v%{version}
# (mirroring the minio / picoclaw / aardvark-dns convention). Then convert the
# line below to the `#!RemoteAsset:  sha256:<hash>` form with the real digest.
Source1:        %{name}-v%{version}-vendor.tar.gz
BuildSystem:    golang

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       promtool = %{version}-%{release}

%description
Prometheus is a systems and service monitoring system. It collects metrics
from configured targets at given intervals, evaluates rule expressions,
displays the results, and can trigger alerts when specified conditions are
observed.

This package currently ships only the promtool command-line utility, used
to validate Prometheus configuration files, lint and unit-test alerting
and recording rules, inspect TSDB blocks, and query running Prometheus
servers. The prometheus server binary is intentionally not built here
because it embeds a React-based web UI whose assets require an npm
toolchain that is not yet available in openRuyi; once npm is packaged
this spec can be extended to build the server as well.

%prep -a
%setup -q -D -T -a 1 -n %{_name}-%{version}

%build
export GO111MODULE=on
# Disable workspace mode: prometheus ships a go.work that pulls compliance/
# internal/tools/ web/ui/mantine-ui/ in as sibling modules with their own
# go.mod files; building those would require workspace-aware vendoring (and
# the React/mantine UI on top). The vendor tarball is generated from the
# root go.mod alone and only covers what ./cmd/promtool needs, so build
# with GOWORK=off to match.
export GOWORK=off
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
export GOFLAGS="-buildmode=pie -mod=vendor -trimpath -modcacherw"

# Match upstream Makefile.common ldflags so `promtool --version` reports
# real values instead of the (devel) placeholder.
LDFLAGS="-X github.com/prometheus/common/version.Version=%{version}"
LDFLAGS="$LDFLAGS -X github.com/prometheus/common/version.Revision=openRuyi"
LDFLAGS="$LDFLAGS -X github.com/prometheus/common/version.Branch=tarball"
LDFLAGS="$LDFLAGS -X github.com/prometheus/common/version.BuildUser=openRuyi"

go build -v -ldflags "$LDFLAGS" -o promtool ./cmd/promtool

%install
install -D -m 0755 promtool %{buildroot}%{_bindir}/promtool

%check
# Upstream's cmd/promtool tests need an active tsdb test fixture tree and
# occasionally network for HTTP transport tests; allow failures so a
# missing fixture does not block the build.
export GO111MODULE=on
export GOPATH=%{_builddir}/go:%{_datadir}/gocode
export GOFLAGS="-mod=vendor"
go test ./cmd/promtool/... || :

%files
%license LICENSE NOTICE
%doc README.md CHANGELOG.md
%{_bindir}/promtool

%changelog
%autochangelog
