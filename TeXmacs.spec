Summary:	A wysiwyg mathematical text editor
Summary(pl):	Edytor WYSIWYG do tekst�w matematycznych
Name:		TeXmacs
Version:	0.3.0
%define	veradd	7
Release:	7
License:	GPL
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplica��es/Editores
Source0:	ftp://ftp.dante.de/tex-archive/systems/unix/TeXmacs/%{name}-%{version}-%{veradd}-src.tar.gz
Vendor:		Jo the ripper software
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
GNU TeXmacs jest wolnodost�pnym edytorem typu WYSIWYG do tekst�w
matematycznych, zainspirowanym przez TeX-a i GNU Emacsa. Ma
zaimplementowany wysokiej jako�ci sk�ad przy u�yciu font�w TeX-a, ale
udost�pnia tak�e przyjazny interfejs u�ytkownika.

Wysoka jako�� sk�adu jest zachowana przy automatycznie generowanych
wzorach i jest mo�liwe u�ywanie TeXmacsa jako interfejsu do system�w
algebry. GNU TeXmacs obs�uguje tak�e j�zyk rozszerze� Guile/Scheme, co
umo�liwia adaptowanie interfejsu u�ytkownika do specyficznych potrzeb,
a tak�e rozszerzanie edytora.

%prep
%setup -q -n %{name}-%{version}-%{veradd}-src

%build
./configure --prefix=$RPM_BUILD_ROOT%{_prefix}
%{__make} CXXFLAGS="%{rpmcflags}" STATIC_TEXMACS

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install
./configure --prefix=%{_prefix}
install bin/fig2ps $RPM_BUILD_ROOT%{_bindir}
install bin/texmacs $RPM_BUILD_ROOT%{_bindir}
GUILE_DATA_PATH=`guile-config info pkgdatadir`
GUILE_LOAD_PATH=`find $GUILE_DATA_PATH -type d | grep ice-9`
cp -rf $GUILE_LOAD_PATH $RPM_BUILD_ROOT%{_datadir}/TeXmacs-0.3.0-5/progs
chmod 755 $RPM_BUILD_ROOT%{_datadir}/TeXmacs-0.3.0-5/progs/ice-9
rm -f $RPM_BUILD_ROOT%{_datadir}/TeXmacs-0.3.0-5/lib/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/texmacs
%attr(755,root,root) %{_bindir}/fig2ps
%{_includedir}/TeXmacs.h
%{_mandir}/man1/texmacs.1*
%{_datadir}/TeXmacs-0.3.0-5
