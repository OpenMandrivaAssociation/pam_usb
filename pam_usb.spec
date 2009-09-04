%define	name	pam_usb
%define	version	0.4.2
%define	rel	2
%define	release	%mkrel %{rel}

Summary:	PAM module through external storage
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.pamusb.org/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/pamusb/%{name}-%{version}.tar.gz
Source1:	%{name}-doc.tar.bz2
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	dbus-devel libxml2-devel hal-devel
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
%make CFLAGS="%optflags -fPIC `pkg-config --cflags dbus-1 hal libxml-2.0`"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std \
  PAM_USB_DEST=$RPM_BUILD_ROOT/%{_lib}/security \
  DOCS_DEST=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

cp -a html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%defattr(-,root,root)
/%{_lib}/security/%{name}.so
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_sysconfdir}/pamusb.conf
