
%define		snap	20030828

Summary:	Text console port of GTK+, based on ncurses
Summary(pl):	Port GTK+ na konsole tekstow±, oparty o ncurses
Name:		gtk2-cursed
Version:	2.2.2
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://ep09.kernel.pl/~misi3k/snap/gtk+-cursed-%{snap}.tar.bz2
# Source0-md5:	6387fa9b3a0aec376133841b3948dbec
BuildRequires:	atk-devel >= 1.0.0
BuildRequires:	pango-devel >= 1.2.0
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	libtiff-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2.2
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	gpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text console port of GTK+, based on ncurses

%description -l pl
Port GTK+ na konsole tekstow±, oparty o ncurses

%package devel
Summary:	Development tools for cursed GTK+
Group:		Development/Libraries
Requires:	gtk2-cursed = %{version}
Requires:	pango-devel >= %{pango_version}
Requires:	atk-devel >= %{atk_version}
Requires:	glib2-devel >= %{glib2_version}

%description devel
The gtk+-cursed-devel package contains the header files for the cursed
port of GTK+ widget toolkit.

%prep
%setup -q -n gtk+

%build
%configure \
	--disable-gtk-doc \
	--with-gdktarget=cursed

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall RUN_QUERY_IMMODULES_TEST=false RUN_QUERY_LOADER_TEST=false

#%find_lang gtk20

./mkinstalldirs $RPM_BUILD_ROOT%{_sysconfdir}/gtk-cursed-2.0

# Remove unpackaged files
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
%{_bindir}/gtk-cursed-query-immodules-2.0 > %{_sysconfdir}/gtk-cursed-2.0/gtk.immodules
%{_bindir}/gdk-pixbuf-query-loaders > %{_sysconfdir}/gtk-cursed-2.0/gdk-pixbuf.loaders

%postun
/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gtk-cursed-demo
%attr(755,root,root) %{_bindir}/gtk-cursed-query-immodules-2.0
%{_libdir}/libgtk-cursed-2.0.so.*
%{_libdir}/libgdk-cursed-2.0.so.*
%{_libdir}/libgdk_cursed_pixbuf-2.0.so.*
%dir %{_libdir}/gtk-cursed-2.0
%{_libdir}/gtk-cursed-2.0/%{bin_version}
%{_datadir}/gtk-cursed-2.0
%dir %{_sysconfdir}/gtk-cursed-2.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.so
%dir %{_libdir}/gtk-cursed-2.0
%{_libdir}/gtk-cursed-2.0/include
%{_includedir}/*
%{_aclocaldir}/*
%{_libdir}/pkgconfig/*
