# TODO:
# - update pl-translation
Summary:	A wysiwyg scientific text editor
Summary(pl):	Edytor WYSIWYG do tekstów naukowych
Name:		TeXmacs
Version:	1.0.4
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	ftp://ftp.texmacs.org/pub/TeXmacs/targz/%{name}-%{version}-src.tar.gz
# Source0-md5:	ebec9edf0872def83e42a1faa54f7d2a
Source1:	%{name}.desktop
URL:		http://www.texmacs.org/
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	guile-devel >= 1.4.1
BuildRequires:	libstdc++-devel
Requires:	kpathsea
Requires:	tetex
Requires:	tetex-dvips
Requires:	tetex-metafont
Requires:	ghostscript
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU TeXmacs is a free scientific text editor, which was both inspired
by TeX and GNU Emacs. The editor allows you to write structured
documents via a wysiwyg (what-you-see-is-what-you-get) and user
friendly interface. New styles may be created by the user. The program
implements high-quality typesetting algorithms and TeX fonts, which
help you to produce professionally looking documents.

The high typesetting quality still goes through for automatically
generated formulas, which makes TeXmacs suitable as an interface for
computer algebra systems. TeXmacs also supports the Guile/Scheme
extension language, so that you may customize the interface and write
your own extensions to the editor.

Converters exist for TeX/LaTeX and they are under development for
Html/MathML/Xml. In the future, TeXmacs is planned to evolve towards a
complete scientific office suite, with spreadsheet capacities, a
technical drawing editor and a presentation mode.

%description -l pl
GNU TeXmacs jest wolnodostêpnym edytorem typu WYSIWYG do tekstów
naukowych, zainspirowanym przez TeXa i GNU Emacsa. Ma zaimplementowany
wysokiej jako¶ci sk³ad tekstu przy u¿yciu fontów TeXa a tak¿e
udostêpnia przyjazny interfejs u¿ytkownika.

Wysoka jako¶æ sk³adu jest zachowana przy automatycznie generowanych
wzorach i jest mo¿liwe u¿ywanie TeXmacsa jako interfejsu do systemów
algebry. GNU TeXmacs obs³uguje tak¿e jêzyk rozszerzeñ Guile/Scheme, co
umo¿liwia adaptowanie interfejsu u¿ytkownika do specyficznych potrzeb,
a tak¿e rozszerzanie mo¿liwo¶ci edytora.

%prep
%setup -q -n %{name}-%{version}-src

%build
cp -f %{_datadir}/automake/config.sub .
%configure2_13

# DO NOT add -fno-rtti -fno-implicit-templates, it BREAKS build
%{__make} \
	CXXOPTIMIZE="%{rpmcflags} -fno-exceptions"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

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
%{_desktopdir}/*.desktop
%{_mandir}/man?/*
