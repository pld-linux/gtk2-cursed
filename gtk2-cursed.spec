
%define		snap		20030828
%define		bin_version	2.2.0

Summary:	Text console port of GTK+, based on ncurses
Summary(pl):	Port GTK+ na konsole tekstow±, oparty o ncurses
Name:		gtk2-cursed
Version:	2.2.2
Release:	0.%{snap}.1
License:	LGPL
Group:		Libraries
Source0:	http://ep09.pld-linux.org/~misi3k/snap/gtk+-cursed-%{snap}.tar.bz2
# Source0-md5:	6387fa9b3a0aec376133841b3948dbec
Patch0:		%{name}-am.patch
Patch1:		%{name}-ncurses.patch
BuildRequires:	atk-devel >= 1.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gpm-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2.2
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pango-devel >= 1:1.2.0
Requires(post):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text console port of GTK+, based on ncurses.

%description -l pl
Port GTK+ na konsole tekstow±, oparty o ncurses.

%package devel
Summary:	Development tools for cursed GTK+
Summary(pl):	Narzêdzia programisty dla GTK+ opartego na curses
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pango-devel >= 1:1.2.0
Requires:	atk-devel >= 1.0.0
Requires:	glib2-devel >= 2.2.0

%description devel
The gtk+-cursed-devel package contains the header files for the cursed
port of GTK+ widget toolkit.

%description devel -l pl
Pakiet gtk+-cursed-devel zawiera narzêdzia i pliki nag³ówkowe s³u¿±ce
do tworzenia opartych na curses widgetów GTK+.

%prep
%setup -q -n gtk+
%patch0 -p1
%patch1	-p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-gtk-doc \
	--with-gdktarget=cursed

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	RUN_QUERY_IMMODULES_TEST=false \
	RUN_QUERY_LOADER_TEST=false

./mkinstalldirs $RPM_BUILD_ROOT%{_sysconfdir}/gtk-cursed-2.0

# useless (modules are dlopened through libgmodule)
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-cursed-2.0/*/{immodules,loaders}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
%{_bindir}/gtk-cursed-query-immodules-2.0 > %{_sysconfdir}/gtk-cursed-2.0/gtk.immodules
# ? this program is from normal gtk+2
#%{_bindir}/gdk-pixbuf-query-loaders > %{_sysconfdir}/gtk-cursed-2.0/gdk-pixbuf.loaders

%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gtk-cursed-demo
%attr(755,root,root) %{_bindir}/gtk-cursed-query-immodules-2.0
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/gtk-cursed-2.0
%attr(755,root,root) %{_libdir}/gtk-cursed-2.0/%{bin_version}/immodules/*.so
%attr(755,root,root) %{_libdir}/gtk-cursed-2.0/%{bin_version}/loaders/*.so
%{_datadir}/gtk-cursed-2.0
%dir %{_sysconfdir}/gtk-cursed-2.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/gtk-cursed-2.0/include
%{_includedir}/gtk-cursed-2.0
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc
