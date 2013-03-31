Summary:	GNOME calculator
Name:		gnome-calculator
Version:	3.8.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Math
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-calculator/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	69947f4c6703c373513e339078d9c0ef
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	yelp-tools
Requires(post,postun):	glib-gio-gsettings
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gcalctool is a simple calculator that performs a variety of functions.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-compile	\
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ca@valencia,en@shaw}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/gcalccmd
%attr(755,root,root) %{_bindir}/gnome-calculator
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%{_desktopdir}/*.desktop
%{_mandir}/man1/*

