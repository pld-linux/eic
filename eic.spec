Summary:	C language interpreter
Name:		eic
Version:	4.3.0
%define	dir	4_3_0
Release:	1
License:	Artistic License (generally free)
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Source0:	http://www.kd-dev.com/~eic/download/eicdist/%{dir}/EiCsrc_%{version}.tgz
URL:		http://www.kd-dev.com/~eic
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EiC is a freely available C language interpreter in both source and
binary form. EiC allows you to write C programs, and then "execute"
them as if they were a script (like a Perl script or a shell script). You
can even embed EiC in your own programs, allowing your
application to have a "scripting" language that is syntactically
equivalent to C. It is also possible to let an EiC "script" call compiled
library code and for compiled code to make callbacks to EiC user
defined functions. 

%prep
%setup -q -n EiC



%build
#echo "INSTALL_DIR = %{_bindir}" >> project.params
./config/makeconfig

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
