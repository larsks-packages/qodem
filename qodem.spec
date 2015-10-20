%global commit_id 4753513

Name:		qodem
Version:	1.0
Release:	2%{?dist}.git%{commit_id}
Summary:	A Qmodem clone for Linux

License:	CC0
URL:		https://github.com/klamonte/qodem
Source0:	%{name}-%{version}-%{commit_id}.tar.gz

BuildRequires:	automake
BuildRequires:	SDL-devel
BuildRequires:	ncurses-devel

%description
Qodem is a from-scratch clone implementation of the Qmodem communications
program made popular in the days when Bulletin Board Systems ruled the night.
Qodem emulates the dialing directory and the terminal screen features of Qmodem
over both modem and Internet connections.


%prep
%autosetup -n %{name}-%{version}-%{commit_id}

aclocal
automake


%build
# building upnp support is causing linking failures at the moment.
# fixing that is left as an exercise to the motivated reader.
%configure --disable-upnp
make %{?_smp_mflags}


%install
%make_install

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/xqodem.1*
rm -f $RPM_BUILD_ROOT%{_bindir}/xqodem

%files
%license COPYING
%doc README.md

%{_bindir}/qodem
%{_mandir}/man1/qodem.1*

%changelog
* Tue Oct 20 2015 Lars Kellogg-Stedman <lars@redhat.com> - 1.0-1.git4753513
- initial packaging

