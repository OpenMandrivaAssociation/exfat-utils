Name:		exfat-utils
Summary:	Utilities for exFAT file system
Version:	1.2.3
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		https://github.com/relan/exfat
Source0:	https://github.com/relan/exfat/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	scons

%description
A set of utilities for creating, checking, dumping and labeling exFAT file
system.

%prep
%setup -q

%build
export CC=%{__cc}
export CXX=%{__cxx}

%scons

%install
export CC=%{__cc}
export CXX=%{__cxx}

scons install DESTDIR=%{buildroot}/sbin
mkdir -p %{buildroot}/%{_mandir}/man8/

install -m644 dump/dumpexfat.8 %{buildroot}/%{_mandir}/man8/dumpexfat.8
install -m644 fsck/exfatfsck.8 %{buildroot}/%{_mandir}/man8/exfatfsck.8
install -m644 mkfs/mkexfatfs.8 %{buildroot}/%{_mandir}/man8/mkexfatfs.8
install -m644 label/exfatlabel.8 %{buildroot}/%{_mandir}/man8/exfatlabel.8

pushd %{buildroot}/%{_mandir}/man8/
ln -s exfatfsck.8 fsck.exfat.8
ln -s mkexfatfs.8 mkfs.exfat.8
popd

%files
/sbin/dumpexfat
/sbin/exfatfsck
/sbin/fsck.exfat
/sbin/mkexfatfs
/sbin/mkfs.exfat
/sbin/exfatlabel
%{_mandir}/man8/*
