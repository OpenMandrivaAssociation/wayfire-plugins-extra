%define _disable_ld_no_undefined 1

Name:           wayfire-plugins-extra
Version:        0.11.2
Release:        1
Summary:        Additional plugins for Wayfire
License:        MIT
URL:            https://github.com/WayfireWM/wayfire-plugins-extra
Source0:        https://github.com/WayfireWM/wayfire-plugins-extra/releases/download/v%{version}/%{name}-%{version}.tar.xz

Source1:         https://github.com/timgott/wayfire-shadows/archive/wayfire-shadows-4bfdbbf1abe40519183b9a1e1648a732bc656f13.tar.gz
Source2:         https://gitlab.com/wayfireplugins/focus-request/-/archive/focus-request-b5c5029f1a695bcd79e2fa0de615cd8028f64f62.tar.gz
Source3:         https://github.com/soreau/pixdecor/archive/pixdecor-d74909d3056565a8f2cbfbc33c6951960d486e63.tar.gz
Source4:         https://github.com/soreau/filters/archive/filters-ecfe09aa87e812cd11c13eff60414c106d5accef.tar.gz

# Try enable later
#Source5:         https://github.com/dkondor/wstroke/archive/wstroke-95c390f072071071a202cde06b79026eb8691421.tar.gz

BuildRequires:  meson
BuildRequires:  git
BuildRequires:  gettext
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(giomm-2.4)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(libglvnd)
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

mkdir -p subprojects

tar -xzf %{SOURCE1} -C subprojects
mv subprojects/wayfire-shadows-4bfdbbf1abe40519183b9a1e1648a732bc656f13 \
   subprojects/wayfire-shadows

tar -xzf %{SOURCE2} -C subprojects
mv subprojects/focus-request-b5c5029f1a695bcd79e2fa0de615cd8028f64f62 \
   subprojects/focus-request

tar -xzf %{SOURCE3} -C subprojects
mv subprojects/pixdecor-d74909d3056565a8f2cbfbc33c6951960d486e63 \
   subprojects/pixdecor

tar -xzf %{SOURCE4} -C subprojects
mv subprojects/filters-ecfe09aa87e812cd11c13eff60414c106d5accef \
   subprojects/filters

rm -f subprojects/*.wrap

mv locale/ro/wf-plugin-fisheye.po locale/ro/LC_MESSAGES/

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
