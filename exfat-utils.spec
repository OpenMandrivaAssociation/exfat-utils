Name:		exfat-utils
Summary:	Utilities for exFAT file system
Version:	1.0.1
Release:	5
License:	GPLv2+
Group:		System/Kernel and hardware
Source0:	http://exfat.googlecode.com/files/exfat-utils-%{version}.tar.gz

# A cumulative patch with changes since the release of 1.0.1 (SVN rev 342)
# till the newest revision at the moment (rev 392, 2014-01-18).
# The license also changed from GPLv3+ to GPLv2+.
Patch0: exfat-utils-r342-to-r392.patch

URL:		http://code.google.com/p/exfat/
BuildRequires:	scons

%description
A set of utilities for creating, checking, dumping and labeling exFAT file
system.

%prep
%setup -q
%patch0 -p1

%build
export CC=clang
export CXX=clang++
%scons

%install
export CC=clang
export CXX=clang++
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
