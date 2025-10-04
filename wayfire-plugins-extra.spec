%define _disable_ld_no_undefined 1

Name:           wayfire-plugins-extra
Version:        0.10.0
Release:        1
Summary:        Additional plugins for Wayfire
License:        MIT
URL:            https://github.com/WayfireWM/wayfire-plugins-extra
Source0:        https://github.com/WayfireWM/wayfire-plugins-extra/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Patch taken from https://gist.githubusercontent.com/dr460nf1r3/e5c52144372e0948229e96e2f1936e35/raw/4d4ab455c9ed781939edc1d07e5fc990f6ebea69/gistfile1.txt
#Patch0:         compile-fix.patch

BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  meson
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(giomm-2.4)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(wayfire)
BuildRequires:  pkgconfig(wf-config)
BuildRequires:  pkgconfig(wlroots-0.19)
Requires:       wayfire

%description
Additional plugins for Wayfire
The plugins that come here are plugins that have external dependencies, for ex. giomm.

%prep
%autosetup -p1

%build
%meson \
         -Denable_pixdecor=true \
         -Denable_filters=true \
         -Denable_wayfire_shadows=true \
         -Denable_focus_request=true
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_libdir}/wayfire/*.so
%{_datadir}/wayfire/metadata/*.xml
