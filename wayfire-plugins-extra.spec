%define _disable_ld_no_undefined 1

Name:           wayfire-plugins-extra
Version:        0.11.2
Release:        1
Summary:        Additional plugins for Wayfire
License:        MIT
URL:            https://github.com/WayfireWM/wayfire-plugins-extra
Source0:        https://github.com/WayfireWM/wayfire-plugins-extra/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  meson
BuildRequires:  git
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(giomm-2.4)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(wayfire)
BuildRequires:  pkgconfig(wf-config)
BuildRequires:  pkgconfig(wlroots-0.20)
Requires:       wayfire

%description
Additional plugins for Wayfire
The plugins that come here are plugins that have external dependencies, for ex. giomm.

%prep
%autosetup -p1

%build
%meson \
         -Dpixdecor=true \
         -Dfilters=true \
         -Dwayfire_shadows=true \
         -Dfocus_request=true
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_libdir}/wayfire/*.so
%{_datadir}/wayfire/metadata/*.xml
