%global         forgeurl https://gitlab.gnome.org/World/design/icon-library
%global         uuid org.gnome.design.IconLibrary
%global         tag 0.0.12

Name:      icon-library
Version:   0.0.12
Release:   %autorelease
Summary:   GNOME symbolic icons for your apps.

%forgemeta

License:   GPL-3.0-or-later
URL:       https://gitlab.gnome.org/World/design/icon-library
Source0:   %{forgesource}

BuildRequires:  meson
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) 
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  rust-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
A tool for browsing symbolic GNOME icons, you can download icons and use them in your apps.

%prep
%forgeautosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%license LICENSE.md
%doc README.md
%{_bindir}/icon-library
%{_datadir}/icon-library/*
%{_metainfodir}/%{uuid}.appdata.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/glib-2.0/schemas/%{uuid}.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg

%changelog
%autochangelog
