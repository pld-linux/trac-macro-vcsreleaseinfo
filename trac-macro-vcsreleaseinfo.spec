%define		trac_ver	0.12
%define		plugin		vcsreleaseinfo
Summary:	VCS Release Info Macro for Trac
Name:		trac-macro-%{plugin}
Version:	0.1
Release:	3
License:	BSD-like
Group:		Applications/WWW
Source0:	http://trac-hacks.org/changeset/latest/vcsreleaseinfomacro?old_path=/&filename=vcsreleaseinfomacro&format=zip#/%{plugin}-%{version}.zip
# Source0-md5:	4673db3ed8eaa877919974a63d6b008a
URL:		http://trac-hacks.org/wiki/VcsReleaseInfoMacro
BuildRequires:	unzip
# if 0.13 cames into play, can sanitize this again
Requires:	trac >= %{trac_ver}-6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		plugindir	%{_datadir}/trac/plugins

%description
VCS Release Info macro takes list of tags from your project VCS and
formats the list.

%prep
%setup -qc
mv %{plugin}macro/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
install -p *.py $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
trac-enableplugin 'VcsReleaseInfoMacro.*' || :

%files
%defattr(644,root,root,755)
%{plugindir}/VcsReleaseInfoMacro.py
