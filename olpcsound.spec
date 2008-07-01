Summary: Csound - sound synthesis language and library, OLPC subset
Name:   olpcsound        
Version: 5.08.92
Release: 1%{?dist}
URL: http://csound.sourceforge.net/
License: LGPLv2+
Group: Applications/Multimedia
Source: http://downloads.sourceforge.net/csound/olpcsound-%version.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: swig python scons alsa-lib-devel liblo-devel libsndfile-devel 
BuildRequires: libpng-devel libjpeg-devel libvorbis-devel libogg-devel gettext python-devel
%define python_site_dir %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

%description
olpcsound is a subset of the Csound sound and music 
synthesis system, tailored specifically for  XO platform. 

%package devel
Summary: Csound development files and libraries
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Headers and libraries for Csound-based application development

%prep
%setup -q

%build
%{_bindir}/scons buildOLPC=1 customCCFLAGS="%{optflags}" customCXXFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__python} install-olpc.py --install-python --install-headers --instdir=%{buildroot}
%find_lang csound5

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
 
%postun -p /sbin/ldconfig

%files -f csound5.lang
%defattr(-,root,root,-)
%{_bindir}/*
%dir %{_libdir}/csound
%dir %{_libdir}/csound/plugins
%{_libdir}/csound/plugins/*
%{_libdir}/libcsound.so.5.1
%{_libdir}/libcsnd.so.5.1
%{python_site_dir}/*
%dir %{_datadir}/doc/csound
%{_datadir}/doc/csound/*

%files devel
%defattr(-,root,root,0755)
%dir %{_includedir}/csound
%{_includedir}/csound/*
%{_libdir}/libcsound.so
%{_libdir}/libcsnd.so


%changelog
* Thur May 29 2008  Victor.Lazzarini <vlazzarini@nuim.ie> - 5.08.92-2
  - fixed version format in changelog
  - fixed permissions of Opcodes/hrtfopcodes.c and Util/mixer.c in srcs

* Mon May 19 2008 Victor.Lazzarini <vlazzarini@nuim.ie> - 5.08.92-1
  - fixed license
  - removed -fomit-frame-pointer from SConstruct
  - fixed description

* Mon May 19 2008 Victor.Lazzarini <vlazzarini@nuim.ie>
  5.08.92-0
 - fixed licensing issues and removed non-free sources/binaries
 - fixed requires for -devel
 - removed -ffast-math option from SConstruct 
 - added _bindir macro
 - added ownership of /usr/lib/csound
 - removed redundant build working directory for csound5.lang
 - removed stripping commands from install-olpc.py script
 - added AUTHORS to docs, removed INSTALL and readme-csound5.txt
 - shortened the description and added EVR to this changelog

* Fri May 02 2008 Victor Lazzarini <vlazzarini@nuim.ie>
 - fixed method of obtaining python site directory
 - fixed license code
 - fixed ownership of directories
 - added dist tag to version
 - added fedora flags

* Wed Apr 02 2008  Victor Lazzarini <vlazzarini@nuim.ie>
 - initial version of this spec
