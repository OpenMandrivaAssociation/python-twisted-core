%define mainver %(echo %{version} | sed -e 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')

Summary:	Event-based framework for internet applications
Name:		python-twisted-core
Version:	13.0.0
Release:	2
License:	MIT
Group:		Development/Python
Url:		http://twistedmatrix.com/projects/core/
Source0:	http://twistedmatrix.com/Releases/Core/13.0/TwistedCore-%{version}.tar.bz2
Patch1:	TwistedCore-13.0.0-sagemath.patch
BuildRequires:	python-zope-interface
BuildRequires:	pkgconfig(python)
Requires:	pycrypto
Requires:	python-OpenSSL
Requires:	python-zope-interface
Conflicts:	python-twisted < 2.0.0

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
Group:		Development/Python
Summary:	%{name} documentation

%description  doc
Documentation files for %name.
This consist mainly of the twist api for the core component.

%prep
%setup -qn TwistedCore-%{version}
%apply_patches

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot}

# no need for c source code
find %{buildroot}/%{py_platsitedir}/twisted -type f -name '*.c' | xargs rm -f

install -d %{buildroot}%{_mandir}/man1
install -m 644 doc/man/*.1 %{buildroot}%{_mandir}/man1

%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc LICENSE NEWS README
%dir %{py_platsitedir}/twisted
%{py_platsitedir}/twisted/*
%{py_platsitedir}/*.egg-info
%{_mandir}/man1/*

%files doc
# ChangeLog.Old is here as this is big
%doc doc/

