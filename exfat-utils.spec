Name:		exfat-utils
Summary:	Utilities for exFAT file system
Version:	1.2.5
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		https://github.com/relan/exfat
Source0:	https://github.com/relan/exfat/releases/download/v%{version}/%{name}-%{version}.tar.gz

%description
A set of utilities for creating, checking, dumping and labeling exFAT file
system.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

# (tpg) install man
mkdir -p %{buildroot}%{_mandir}/man8
install -m644 dump/dumpexfat.8 %{buildroot}%{_mandir}/man8/
install -m644 fsck/exfatfsck.8 %{buildroot}%{_mandir}/man8/
install -m644 label/exfatlabel.8 %{buildroot}%{_mandir}/man8/
install -m644 mkfs/mkexfatfs.8 %{buildroot}%{_mandir}/man8/

%files
%{_sbindir}/*
%{_mandir}/man8/*.8.*
