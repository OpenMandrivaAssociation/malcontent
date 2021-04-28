%define api		0
%define major		0
%define gi_major	0
%define libname		%mklibname malcontent %major
%define develname	%mklibname -d malcontent
%define girname		%mklibname malcontent-gir %gi_major

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		malcontent
Version:	0.10.1
Release:	1
Summary:	Library for parental controls support
Group:		System/Libraries
License:	LGPLv2+
URL:		https://gitlab.freedesktop.org/pwithnall/malcontent
Source0:	https://gitlab.freedesktop.org/pwithnall/malcontent/-/archive/%{version}/malcontent-%{version}.tar.bz2

BuildRequires:	gettext-devel
BuildRequires:	gtk-doc
BuildRequires:	meson
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0) >= 2.17.3
BuildRequires:	pkgconfig(glib-2.0) >= 2.19.0
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(glib-testing-0)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(accountsservice)
BuildRequires:	pkgconfig(appstream-glib)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(flatpak)
BuildRequires:  pam-devel
BuildRequires:	itstool

%description
%{name} implements parental controls support which can be used by applications
%to filter or limit the access of child accounts to inappropriate content.

%package i18n
Summary:	Library for parental controls support - translations
Group:		System/Internationalization
BuildArch:	noarch

%description i18n
%{name} implements parental controls support which can be used by applications
%to filter or limit the access of child accounts to inappropriate content.

%package -n %{libname}
Summary:	Library for parental controls support
Group:		System/Libraries
Requires:	%{name}-i18n >= %{version}-%{release}
Requires:	%{name} >= %{version}-%{release}

%description -n %{libname}
%{name} implements parental controls support which can be used by applications
%to filter or limit the access of child accounts to inappropriate content.


%package -n %develname
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains libraries and header files for
developing applications that use %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%prep
%autosetup -p1

%build
%meson -Dinstalled_tests=false
%meson_build

%install
%meson_install

%find_lang malcontent --with-gnome

%files i18n -f malcontent.lang

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}{,.*}
%{_libdir}/lib%{name}-ui-%{api}.so.%{major}{,.*}

%files -n %{develname}
#%%doc %%{_datadir}/gtk-doc/html/%{name}/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/pkgconfig/%{name}-ui-%{api}.pc

%{_datadir}/gir-1.0/Malcontent-%{gi_major}.gir
%{_datadir}/gir-1.0/MalcontentUi-%{gi_major}.gir

%files -n %{girname}
%{_libdir}/girepository-1.0/Malcontent-%{gi_major}.typelib
%{_libdir}/girepository-1.0/MalcontentUi-%{gi_major}.typelib

%files
%{_bindir}/malcontent-client
%{_bindir}/malcontent-control
%{_mandir}/man8/malcontent-client.8*
%{_libdir}/security/pam_malcontent.so
%{_datadir}/accountsservice/interfaces/com.endlessm.ParentalControls.AccountInfo.xml
%{_datadir}/accountsservice/interfaces/com.endlessm.ParentalControls.AppFilter.xml
%{_datadir}/accountsservice/interfaces/com.endlessm.ParentalControls.SessionLimits.xml
%{_datadir}/applications/org.freedesktop.MalcontentControl.desktop
%{_datadir}/dbus-1/interfaces/com.endlessm.ParentalControls.AccountInfo.xml
%{_datadir}/dbus-1/interfaces/com.endlessm.ParentalControls.AppFilter.xml
%{_datadir}/dbus-1/interfaces/com.endlessm.ParentalControls.SessionLimits.xml
%{_datadir}/icons/hicolor/scalable/apps/org.freedesktop.MalcontentControl.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.freedesktop.MalcontentControl-symbolic.svg
%{_datadir}/metainfo/org.freedesktop.MalcontentControl.appdata.xml
%{_datadir}/polkit-1/actions/com.endlessm.ParentalControls.policy
%{_datadir}/polkit-1/actions/org.freedesktop.MalcontentControl.policy
%{_datadir}/polkit-1/rules.d/com.endlessm.ParentalControls.rules
