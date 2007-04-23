%define	name	pam_usb
%define	version	0.3.3
%define	rel	2
%define	release	%mkrel %{rel}

Summary:	PAM module through external storage
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.pamusb.org/
Source0:	http://www.pamusb.org/releases/%{name}-%{version}.tar.bz2
Source1:	%{name}-doc.tar.bz2
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pam-devel 
BuildRequires:  openssl-devel 
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel

%description
pam_usb is a PAM module that enables authentication using an USB-Storage device
(such as an USB Pen) through DSA private/public keys.

It can also work with other devices, such as floppy disks or cdroms.

%prep
%setup -q -a1

%build
%make CFLAGS="%optflags -I ../../src -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_lib}/security $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/usbhotplug
mkdir -p $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}/html

%makeinstall_std PAM_MODULES=$RPM_BUILD_ROOT/%{_lib}/security

# (blino) use udev rule to replace deprecated hotplug.d script
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/hotplug.d/default/pamusb.hotplug
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d
cat >$RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/pamusb.rules <<EOF
SUBSYSTEM=="usb", RUN+="%{_bindir}/usbhotplug usb"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc html/* AUTHORS Changelog README
%defattr(-,root,root)
/%{_lib}/security/*
%{_bindir}/*
%{_mandir}/*/*
%{_sysconfdir}/udev/rules.d/pamusb.rules
%{_sysconfdir}/pam_usb/handlers/xlock.sh
%config(noreplace) %{_sysconfdir}/pam_usb/hotplug.conf
%config(noreplace) %{_sysconfdir}/pam.d/usbhotplug/usbhotplug.pam
