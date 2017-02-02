
Name: app-rstudio-plugin
Epoch: 1
Version: 1.0.0
Release: 1%{dist}
Summary: RStudio Server Policies - Core
License: LGPLv3
Group: ClearOS/Libraries
Packager: eGloo
Vendor: Marc Laporte
Source: app-rstudio-plugin-%{version}.tar.gz
Buildarch: noarch

%description
RStudio Server Policies provide access control for the RStudio app.

%package core
Summary: RStudio Server Policies - Core
Requires: app-base-core
Requires: app-accounts-core

%description core
RStudio Server Policies provide access control for the RStudio app.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/rstudio_plugin
cp -r * %{buildroot}/usr/clearos/apps/rstudio_plugin/

install -D -m 0644 packaging/rstudio.php %{buildroot}/var/clearos/accounts/plugins/rstudio.php

%post core
logger -p local6.notice -t installer 'app-rstudio-plugin-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/rstudio_plugin/deploy/install ] && /usr/clearos/apps/rstudio_plugin/deploy/install
fi

[ -x /usr/clearos/apps/rstudio_plugin/deploy/upgrade ] && /usr/clearos/apps/rstudio_plugin/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-rstudio-plugin-core - uninstalling'
    [ -x /usr/clearos/apps/rstudio_plugin/deploy/uninstall ] && /usr/clearos/apps/rstudio_plugin/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/rstudio_plugin/packaging
%dir /usr/clearos/apps/rstudio_plugin
/usr/clearos/apps/rstudio_plugin/deploy
/usr/clearos/apps/rstudio_plugin/language
/var/clearos/accounts/plugins/rstudio.php
