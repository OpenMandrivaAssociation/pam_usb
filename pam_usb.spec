%define	name	pam_usb
%define	version	0.5.0
%define	rel	1
%define	release	%mkrel %{rel}

Summary:	PAM module through external storage
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.pamusb.org/
Source0:	http://ovh.dl.sourceforge.net/sourceforge/pamusb/%{name}-%{version}.tar.gz
Source1:	%{name}-doc.tar.bz2
License:	GPLv2+
Group:		System/Libraries
BuildRequires:	dbus-devel pkgconfig(libxml-2.0)
BuildRequires:	pam-devel 
BuildRequires:  pkgconfig(openssl) 
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(ncurses)

%description
pam_usb is a PAM module that enables authentication using an USB-Storage device
(such as an USB Pen) through DSA private/public keys.

It can also work with other devices, such as floppy disks or cdroms.

%prep
%setup -q -a1

%build
%make

%install
%makeinstall_std \
  PAM_USB_DEST=%{buildroot}/%{_lib}/security \
  DOCS_DEST=%{buildroot}%{_docdir}/%{name}-%{version}

cp -a html %{buildroot}%{_docdir}/%{name}-%{version}


%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%defattr(-,root,root)
/%{_lib}/security/%{name}.so
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_sysconfdir}/pamusb.conf
