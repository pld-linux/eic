Summary:	C language interpreter
Summary(pl):	Interpreter jêzyka C
Name:		eic
Version:	4.3.0
%define	dir	4_3_0
Release:	1
License:	Artistic License (generally free)
Group:		Development/Languages
Source0:	http://www.kd-dev.com/~eic/download/eicdist/%{dir}/EiCsrc_%{version}.tgz
Source1:	%{name}.h
Patch0:		%{name}-make.patch
URL:		http://www.kd-dev.com/~eic
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

%description -l pl
EiC jest darmowym, ogólnodostêpnym interpreterem jêzyka C zarówno w
formie ¼ród³owej jak i binarnej. EiC pozwala na pisanie programów w C,
a nastêpnie ich "wykonywanie" tak jakby by³y skryptami (takimi samymi
jak skrypty Perla czy pow³oki). Mo¿esz nawet w³±czyæ obs³ugê jêzyka
skryptowego syntaktycznie zgodnego z C do swoich programów.

%package lib
Summary:	Static eic library for embedding
Summary(pl):	Biblioteka statyczna eic
Group:		Development/Libraries

%description lib
Static library that allows to embed EiC in your own programs, allowing
your application to have a "scripting" language that is syntactically
equivalent to C.

%description lib -l pl
Statyczne biblioteki pozwalaj±ce w³±czyæ EiC do swoich w³asnych
programów dodaj±c tym samym obs³ugê "jêzyka skryptowego" syntaktycznie
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
