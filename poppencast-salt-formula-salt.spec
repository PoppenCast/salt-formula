%global forgeurl https://github.com/PoppenCast/salt-formula
%global tag poppencast-salt-formula-salt-0.0.1-1
%forgemeta

Name:    poppencast-salt-formula-salt
Version: 0.0.1
Release: 1%{?dist}
Summary: SaltStack formula for salt

License: Apache-2.0
URL:     %{forgeurl}
Source:  %{forgesource}

Requires: salt
Enhances: salt-minion
Enhances: salt-master

BuildRequires: systemd-rpm-macros
BuildArch:     noarch

%global _description %{expand:
SaltStack formula to set up and configure salt.}

%description %_description

%prep
%forgesetup

%build
# TODO: build and testing, for now this package only "zips up"

%install
install -d -m 755 %{buildroot}%{_datadir}/salt/formulas/salt
cp -R --no-dereference --preserve=mode,links -v salt %{buildroot}%{_datadir}/salt/formulas/salt/

%check
# TODO: build and testing, for now this package only "zips up"

%files
%{_datadir}/salt/formulas/salt/
%doc docs/README.rst
%license LICENSE

%changelog
