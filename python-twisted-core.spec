%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

Summary:        Event-based framework for internet applications
Name:           python-twisted-core
Version:        13.0.0
Release:        1
Source0:        https://pypi.python.org/packages/source/T/Twisted/Twisted-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/projects/core/
Requires:       pycrypto
Requires:       python-OpenSSL python-zope-interface
BuildRequires:	python-devel python-zope-interface
Conflicts:      python-twisted < 2.0.0

Patch1:		TwistedCore-13.0.0-sagemath.patch

%description
Twisted is a framework, written in Python, for writing networked
applications. It includes implementations of a number of commonly used
network services such as a web server, an IRC chat server, a mail
server, a relational database interface and an object broker. Developers
can build applications using all of these services as well as custom
services that they write themselves. Twisted also includes a user
authentication system that controls access to services and provides
services with user context information to implement their own security
models.

%package  doc
Group:          Development/Python
Summary:        %{name} documentation

%description  doc
Documentation files for %name.
This consist mainly of the twist api for the core component.

%prep
%setup -q -n Twisted-%{version}
%patch1	-p1

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot}

# no need for c source code
find %{buildroot}/%{py_platsitedir}/twisted -type f -name '*.c' | xargs rm -f

%__install -d %{buildroot}%{_mandir}/man1
%__install -m 644 doc/*/man/*.1 %{buildroot}%{_mandir}/man1

%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc LICENSE NEWS README
%dir %py_platsitedir/twisted
%py_platsitedir/twisted/*
%py_platsitedir/*.egg-info
%_mandir/man1/*

%files doc
# ChangeLog.Old is here as this is big
%doc doc/



%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 10.1.0-3mdv2011.0
+ Revision: 668040
- mass rebuild

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 10.1.0-2mdv2011.0
+ Revision: 590086
- rebuild for python 2.7

* Tue Jul 20 2010 Lev Givon <lev@mandriva.org> 10.1.0-1mdv2011.0
+ Revision: 555029
- Update to 10.1.0.

* Thu Mar 04 2010 Lev Givon <lev@mandriva.org> 10.0.0-1mdv2010.1
+ Revision: 514221
- Update to 10.0.0.

  + Frederik Himpe <fhimpe@mandriva.org>
    - Fix source URL

* Sat Jan 02 2010 Frederik Himpe <fhimpe@mandriva.org> 9.0.0-1mdv2010.1
+ Revision: 485495
- Update to new version 9.0.0
- Remove python 2.6 patch

* Wed Aug 12 2009 Paulo Andrade <pcpa@mandriva.com.br> 8.2.0-2mdv2010.0
+ Revision: 415247
- Add tls interface adapted from sagemath patches
- Correct python 2.6 deprecated warning about sha1 and md5 modules

* Sat Jan 03 2009 Jérôme Soyer <saispo@mandriva.org> 8.2.0-1mdv2009.1
+ Revision: 323850
- New upstream release

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 8.1.0-2mdv2009.1
+ Revision: 318639
- rebuild for python 2.6

* Fri Jun 13 2008 Michael Scherer <misc@mandriva.org> 8.1.0-1mdv2009.0
+ Revision: 219006
- new version 8.1.0

* Thu Mar 20 2008 Michael Scherer <misc@mandriva.org> 2.5.0-3mdv2008.1
+ Revision: 189239
- rebuild to take less space, blino's request
- split doc and remove .pyc to make some free space on mandriva one

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 2.5.0-2mdv2008.0
+ Revision: 64825
- rebuild


* Mon Jan 15 2007 Michael Scherer <misc@mandriva.org> 2.5.0-1mdv2007.0
+ Revision: 109056
- update to 2.5

* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 2.4.0-2mdv2007.1
+ Revision: 88390
- fix file list

  + Nicolas Lécureuil <neoclust@mandriva.org>
    - Really fix files section
    - Fix  File List
    - Rebuild against new python
    - import python-twisted-core-2.4.0-1mdk


