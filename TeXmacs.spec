Summary:	A wysiwyg mathematical text editor
Summary(pl):	Edytor WYSIWYG do tekstów matematycznych
Name:		TeXmacs
Version:	0.3.5.11
Release:	1
License:	GPL
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores
Source0:	ftp://ftp.texmacs.org/pub/TeXmacs/targz/%{name}-%{version}-src.tar.gz
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-polish.patch
URL:		http://www.texmacs.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	guile-devel
BuildRequires:	libstdc++-devel
Requires:	tetex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU TeXmacs is a free what-you-see-is-what-you-get mathematical text
editor, which was both inspired by TeX and GNU Emacs. The program
implements high quality typesetting using TeX fonts, but it is also
provides a user friendly interface.

The high typesetting quality still goes through for automatically
generated formulas, and it is possible to use TeXmacs as an interface
to computer algebra systems. GNU TeXmacs also supports the
Guile/Scheme extension language, which makes it possible to adapt the
user interface to specific needs and even to extend the editor.

%description -l pl
GNU TeXmacs jest wolnodostêpnym edytorem typu WYSIWYG do tekstów
matematycznych, zainspirowanym przez TeX-a i GNU Emacsa. Ma
zaimplementowany wysokiej jako¶ci sk³ad przy u¿yciu fontów TeX-a, ale
udostêpnia tak¿e przyjazny interfejs u¿ytkownika.

Wysoka jako¶æ sk³adu jest zachowana przy automatycznie generowanych
wzorach i jest mo¿liwe u¿ywanie TeXmacsa jako interfejsu do systemów
algebry. GNU TeXmacs obs³uguje tak¿e jêzyk rozszerzeñ Guile/Scheme, co
umo¿liwia adaptowanie interfejsu u¿ytkownika do specyficznych potrzeb,
a tak¿e rozszerzanie edytora.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf
%configure

%{__make} CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti -fno-implicit-templates"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*.h
%dir %{_libdir}/%{name}-%{version}
%dir %{_libdir}/%{name}-%{version}/bin
%dir %{_libdir}/%{name}-%{version}/lib
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/*
%attr(755,root,root) %{_libdir}/%{name}-%{version}/lib/*
%{_datadir}/%{name}-%{version}
%{_mandir}/man?/*
