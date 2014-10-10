Summary:	GNOME calculator
Name:		gnome-calculator
Version:	3.14.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Math
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-calculator/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	2b3cf2462385851182d6119006546483
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gtksourceview3-devel >= 3.14.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	yelp-tools
Requires(post,postun):	glib-gio-gsettings >= 1:2.42.0
Obsoletes:	gcalctool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/gnome-calculator

%description
GNOME calculator is a simple calculator that performs a variety
of functions.

%package shell-search-provider
Summary:	GNOME Shell search provider
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-shell

%description shell-search-provider
Search result provider for GNOME Shell.
%prep
%setup -q

# kill gnome common deps
%{__sed} -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
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
%{_datadir}/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%{_desktopdir}/*.desktop
%{_mandir}/man1/*

%files shell-search-provider
%defattr(644,root,root,755)
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gnome-calculator-search-provider
%{_datadir}/gnome-shell/search-providers/gnome-calculator-search-provider.ini
%{_datadir}/dbus-1/services/org.gnome.Calculator.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/gnome-calculator-search-provider.ini

