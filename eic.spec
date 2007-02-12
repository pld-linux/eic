Summary:	C language interpreter
Summary(pl.UTF-8):	Interpreter języka C
Name:		eic
Version:	4.3.0
%define	dir	4_3_0
Release:	1
License:	Artistic (generally free)
Group:		Development/Languages
Source0:	http://www.kd-dev.com/~eic/download/eicdist/%{dir}/EiCsrc_%{version}.tgz
# Source0-md5:	4d026568a86f7672bc1417e391c14488
Source1:	%{name}.h
Patch0:		%{name}-make.patch
URL:		http://www.kd-dev.com/~eic/
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EiC is a freely available C language interpreter in both source and
binary form. EiC allows you to write C programs, and then "execute"
them as if they were a script (like a Perl script or a shell script).
You can even embed EiC in your own programs, allowing your application
to have a "scripting" language that is syntactically equivalent to C.
It is also possible to let an EiC "script" call compiled library code
and for compiled code to make callbacks to EiC user defined functions.

%description -l pl.UTF-8
EiC jest darmowym, ogólnodostępnym interpreterem języka C zarówno w
formie źródłowej jak i binarnej. EiC pozwala na pisanie programów w C,
a następnie ich "wykonywanie" tak jakby były skryptami (takimi samymi
jak skrypty Perla czy powłoki). Możesz nawet włączyć obsługę języka
skryptowego syntaktycznie zgodnego z C do swoich programów.

%package lib
Summary:	Static eic library for embedding
Summary(pl.UTF-8):	Biblioteka statyczna eic
Group:		Development/Libraries

%description lib
Static library that allows to embed EiC in your own programs, allowing
your application to have a "scripting" language that is syntactically
equivalent to C.

%description lib -l pl.UTF-8
Statyczne biblioteki pozwalające włączyć EiC do swoich własnych
programów dodając tym samym obsługę "języka skryptowego" syntaktycznie
zgodnego z C.

%prep
%setup -q -n EiC
%patch0 -p1
touch module/link.libs

%build
./config/makeconfig
OPT="%{rpmcflags}" %{__make}
cd doc && %{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

%{__make} install \
	INSTALL_DIR="$RPM_BUILD_ROOT%{_bindir}"

install lib/*.a		$RPM_BUILD_ROOT%{_libdir}
install	%{SOURCE1}	$RPM_BUILD_ROOT%{_includedir}

cd doc
%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html doc/EiC.ps
%attr(755,root,root) %{_bindir}/*

%files lib
%defattr(644,root,root,755)
%doc main/README main/examples/embedEiC.c
%{_includedir}/*.h
%{_libdir}/*.a
