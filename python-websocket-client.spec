# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-websocket-client
Epoch: 100
Version: 1.3.3
Release: 1%{?dist}
BuildArch: noarch
Summary: WebSocket client for python
License: Apache-2.0
URL: https://github.com/websocket-client/websocket-client/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The websocket-client module is a WebSocket client for Python. This
provides the low-level APIs for WebSocket. All APIs are synchronous
functions.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-websocket-client
Summary: WebSocket client for python
Requires: python3
Provides: python3-websocket-client = %{epoch}:%{version}-%{release}
Provides: python3dist(websocket-client) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-websocket-client = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(websocket-client) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-websocket-client = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(websocket-client) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-websocket-client
The websocket-client module is a WebSocket client for Python. This
provides the low-level APIs for WebSocket. All APIs are synchronous
functions.

%files -n python%{python3_version_nodots}-websocket-client
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-websocket-client
Summary: WebSocket client for python
Requires: python3
Provides: python3-websocket-client = %{epoch}:%{version}-%{release}
Provides: python3dist(websocket-client) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-websocket-client = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(websocket-client) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-websocket-client = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(websocket-client) = %{epoch}:%{version}-%{release}

%description -n python3-websocket-client
The websocket-client module is a WebSocket client for Python. This
provides the low-level APIs for WebSocket. All APIs are synchronous
functions.

%files -n python3-websocket-client
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
