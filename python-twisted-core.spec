%define rel 2

Summary:        Event-based framework for internet applications
Name:           python-twisted-core
Version:        2.5.0
Release:        %mkrel %rel
Source0:        http://tmrc.mit.edu/mirror/twisted/Twisted/2.5/TwistedCore-%{version}.tar.bz2
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/projects/core/
BuildRoot:      %{_tmppath}/%{name}-buildroot
Requires:       pycrypto
Requires:       python-OpenSSL python-zope-interface
BuildRequires:	python-devel python-zope-interface
Conflicts:      python-twisted < 2.0.0

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
Summary:        %name documentation

%description  doc
Documentation files for %name.
This consist mainly of the twist api for the core component.

%prep
%setup -q -n TwistedCore-%{version}

%build
%__python setup.py build

%install
%__rm -rf %buildroot
%__python setup.py install --root  %buildroot
# no need for c source code 
find %buildroot/%_libdir/python%pyver/site-packages/twisted -type f -name '*.c' | xargs rm -f 
# remove them to gain some diskspace
find %buildroot/%_libdir/python%pyver/site-packages/twisted -type f -name '*.pyc' | xargs rm -f 

%__install -d                      %buildroot%_mandir/man1
%__install -m 644 doc/man/*.1      %buildroot%_mandir/man1

%clean
%__rm -rf %buildroot


%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc CREDITS LICENSE README 
%py_platsitedir/*wisted*
%_mandir/man1/*

%files  doc
# ChangeLog.Old is here as this is big
%doc doc/ ChangeLog.Old  

