Name:		exfat-utils
Summary:	Utilities for exFAT file system
Version:	1.3.0
Release:	3
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		https://github.com/relan/exfat
Source0:	https://github.com/relan/exfat/releases/download/v%{version}/%{name}-%{version}.tar.gz
# (tpg) from upstream
Patch0:		0001-Validate-UTF-8-byte-sequence.patch
Requires:	fuse-exfat

%description
A set of utilities for creating, checking, dumping and labeling exFAT file
system.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

# (tpg) install man
mkdir -p %{buildroot}%{_mandir}/man8
install -m644 dump/dumpexfat.8 %{buildroot}%{_mandir}/man8/
install -m644 fsck/exfatfsck.8 %{buildroot}%{_mandir}/man8/
install -m644 label/exfatlabel.8 %{buildroot}%{_mandir}/man8/
install -m644 mkfs/mkexfatfs.8 %{buildroot}%{_mandir}/man8/

%files
%{_sbindir}/*
%{_mandir}/man8/*.8.*
