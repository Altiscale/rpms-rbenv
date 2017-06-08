%{!?version: %define version 1.0.0}
%{!?release: %define release 1}

# Break the version down
%define rbenv_major %(echo %{version} | %{__awk} -F\. '{print $1}')
%define rbenv_minor %(echo %{version} | %{__awk} -F\. '{print $2}')
%define rbenv_patch %(echo %{version} | %{__awk} -F\. '{print $3}')

# Specify the versions of ruby to build
%define Ruby0 2.3.1
%define Ruby1 2.3.3

# disable debug package
%define debug_package %{nil}

Summary: rbenv environment with prebuilt rubies and bundler
Name: rbenv
Version: %{version}
Release: %{release}
License: Open Source
Group: Development/Languages
Source0: https://github.com/Altiscale/rpms-rbenv/raw/alti6/rbenv.tar.gz
URL: https://github.com/rbenv

%description
This RPM provides rbenv for switching between rubies, the versions of ruby approved for development and production at Altiscale, and the bundler gem for installing additional gems.

%prep

%setup -q
mkdir -p opt/altiscale
git clone git@github.com:Altiscale/rbenv.git opt/altiscale/rbenv
git clone git@github.com:Altiscale/ruby-build.git opt/altiscale/rbenv/plugins/ruby-build

%build
export RBENV_ROOT=/opt/altiscale/rbenv
export PATH="$RBENV_ROOT/bin:$PATH"
eval "$(rbenv init -)"
rbenv install %{Ruby0} --verbose
rbenv shell %{Ruby0}
gem install bundler
rbenv shell --unset
rbenv install %{Ruby1} --verbose
rbenv shell %{Ruby1}
gem install bundler
rbenv shell --unset

%install
cp -r * $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir /opt/altiscale/rbenv

%changelog
