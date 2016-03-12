Name:		exfat-utils
Summary:	Utilities for exFAT file system
Version:	1.2.3
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

%files
/sbin/*
%{_mandir}/man8/*
