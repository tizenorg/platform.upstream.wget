Name:           wget
Version:        1.13.4
Release:        0
Summary:        A Tool for Mirroring FTP and HTTP Servers
License:        GPL-3.0+
Group:          Productivity/Networking/Web/Utilities
Url:            http://www.gnu.org/software/wget/
Source:         %name-%version.tar.bz2
BuildRequires:  automake
BuildRequires:  libidn-devel
BuildRequires:  openssl-devel
BuildRequires:  pkg-config

%description
Wget enables you to retrieve WWW documents or FTP files from a server.
This can be done in script files or via the command line.

%prep
%setup -q

%build
%configure --with-ssl=openssl
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}

%lang_package

%files
%defattr(-,root,root)
%license COPYING
%doc doc/sample.wgetrc util/rmold.pl
%{_mandir}/*/wget*
%{_infodir}/wget*
%config(noreplace) %{_sysconfdir}/wgetrc
%{_bindir}/*

%changelog
