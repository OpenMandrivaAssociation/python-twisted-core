%define name python-twisted-core
%define version 10.1.0
%define rel 3
%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

Summary:        Event-based framework for internet applications
Name:           %{name}
Version:        %{version}
Release:        %mkrel %rel
Source0:        http://tmrc.mit.edu/mirror/twisted/Core/%{mainver}/TwistedCore-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/projects/core/
BuildRoot:      %{_tmppath}/%{name}-buildroot
Requires:       pycrypto
Requires:       python-OpenSSL python-zope-interface
BuildRequires:	python-devel python-zope-interface
Conflicts:      python-twisted < 2.0.0

Patch0:		TwistedCore-8.2.0-python-2.6.patch
Patch1:		TwistedCore-10.1.0-sagemath.patch

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
%setup -q -n TwistedCore-%{version}
%patch1	-p1

%build
%__python setup.py build

%install
%__rm -rf %buildroot
%__python setup.py install --root=%{buildroot}

# no need for c source code
find %{buildroot}/%{py_platsitedir}/twisted -type f -name '*.c' | xargs rm -f

%__install -d %{buildroot}%{_mandir}/man1
%__install -m 644 doc/man/*.1 %{buildroot}%{_mandir}/man1

%clean
%__rm -rf %{buildroot}

%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc CREDITS LICENSE NEWS README
%dir %py_platsitedir/twisted
%py_platsitedir/twisted/*
%py_platsitedir/*.egg-info
%_mandir/man1/*

%files doc
# ChangeLog.Old is here as this is big
%doc doc/ ChangeLog.Old

