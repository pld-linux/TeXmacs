Summary:	A wysiwyg mathematical text editor
Name:		TeXmacs
Version:	0.3.0
Release:	7
Requires:	tetex
License:	GPL
Group:		Applications/Editors
Group(de):	Applikationen/Editors
Group(pl):	Aplikacje/Edytory
Group(pt):	Aplicações/Editores
Source0:	ftp://ftp.dante.de/tex-archive/systems/unix/TeXmacs/%{name}-%{version}-7-src.tar.gz
Vendor:		Jo the ripper software
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

%prep
mkdir -p $RPM_BUILD_ROOT/usr
cd $RPM_BUILD_ROOT
zcat $RPM_SOURCE_DIR/TeXmacs-0.3.0-5-src.tar.gz | tar -xvf -

%build
cd $RPM_BUILD_ROOT/TeXmacs-0.3.0-5-src
./configure --prefix=$RPM_BUILD_ROOT%{_prefix}
%{__make} CXXFLAGS="-O3 -fexpensive-optimizations -malign-loops=2 -malign-jumps=2 -malign-functions=2" STATIC_TEXMACS

%install
rm -rf $RPM_BUILD_ROOT
cd $RPM_BUILD_ROOT/TeXmacs-0.3.0-5-src
%{__make} install
./configure --prefix=%{_prefix}
chmod 755 TeXmacs-0.3.0-5/bin/*
cp TeXmacs-0.3.0-5/bin/fig2ps $RPM_BUILD_ROOT%{_bindir}
cp TeXmacs-0.3.0-5/bin/texmacs $RPM_BUILD_ROOT%{_bindir}
export GUILE_DATA_PATH=`guile-config info pkgdatadir`
export GUILE_LOAD_PATH=`find $GUILE_DATA_PATH -type d | grep ice-9`
cp -r -f $GUILE_LOAD_PATH $RPM_BUILD_ROOT%{_datadir}/TeXmacs-0.3.0-5/progs
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
