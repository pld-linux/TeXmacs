Summary:	A wysiwyg mathematical text editor
Summary(pl):	Edytor WYSIWYG do tekstów matematycznych
Name:		TeXmacs
Version:	1.0.2.10
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	ftp://ftp.texmacs.org/pub/TeXmacs/targz/%{name}-%{version}-src.tar.gz
# Source0-md5:	70862234c6f33febb06643280227bccb
Patch0:		%{name}-c++.patch
URL:		http://www.texmacs.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	guile-devel >= 1.4.1
BuildRequires:	libstdc++-devel
Requires:	tetex
Requires:	guile-devel
Requires:	ghostscript
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
matematycznych, zainspirowanym przez TeXa i GNU Emacsa. Ma
zaimplementowany wysokiej jako¶ci sk³ad tekstu przy u¿yciu fontów TeXa
a tak¿e udostêpnia przyjazny interfejs u¿ytkownika.

Wysoka jako¶æ sk³adu jest zachowana przy automatycznie generowanych
wzorach i jest mo¿liwe u¿ywanie TeXmacsa jako interfejsu do systemów
algebry. GNU TeXmacs obs³uguje tak¿e jêzyk rozszerzeñ Guile/Scheme, co
umo¿liwia adaptowanie interfejsu u¿ytkownika do specyficznych potrzeb,
a tak¿e rozszerzanie mo¿liwo¶ci edytora.

%prep
%setup -q -n %{name}-%{version}-src
#%patch0 -p1

%build
%configure

# DO NOT add -fno-rtti -fno-implicit-templates, it BREAKS build
%{__make} CXXOPTIMIZE="%{rpmcflags} -fno-exceptions"

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
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/bin
%attr(755,root,root) %{_libdir}/%{name}/bin/*
%{_datadir}/%{name}
%{_mandir}/man?/*
