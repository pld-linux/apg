Summary:	apg - Automated Password Generator
Summary(pl):	apg - automatyczny generator hase³
Name:		apg
Version:	2.2.3
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://www.adel.nursat.kz/apg/download/%{name}-%{version}.tar.gz
# Source0-md5:	3b3fc4f11e90635519fe627c1137c9ac
URL:		http://www.adel.nursat.kz/apg/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
apg generates several random passwords. It uses several password
generation algorithms (currently two) and a built-in pseudo random
number generator.

%description -l pl
apg generuje losowe has³a. Korzysta z kilku (aktualnie dwóch)
algorytmów i wbudowanego generatora liczb pseudolosowych.

%prep
%setup  -q

%build
%{__make} \
	CC="%{__cc}" \
	FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install apg apgbfm $RPM_BUILD_ROOT%{_bindir}
install doc/man/{apgbfm,apg}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES THANKS TODO doc/APG_TIPS
%attr(755,root,root) %{_bindir}/apg
%attr(755,root,root) %{_bindir}/apgbfm
%{_mandir}/man1/*
