%global theme_name    Korora

Name:           gnome-shell-theme-korora
Version:        0.5
Release:        1%{?dist}
Summary:        Gnome shell theme for Korora

Group:          User Interface/Desktops
License:        GPLv2
URL:            https://github.com/kororaproject/kp-pharlap
Source0:        %{name}-%{version}.tar.gz
Requires:       adobe-source-sans-pro-fonts
BuildArch:      noarch

%description
The %{theme_name} theme for GNOME Shell.

%prep
%setup -q

%install

mkdir -p -m755 %{buildroot}%{_datadir}/themes/%{theme_name}/gnome-shell
cp -pr gnome-shell/* %{buildroot}%{_datadir}/themes/%{theme_name}/gnome-shell

%clean
rm -rf %{buildroot}

%files
%{_datadir}/themes/%{theme_name}/gnome-shell/

%changelog
* Mon Jul 16 2015 Ian Firns <firnsy@kororaproject.org> - 0.5-1
- Don't use symbolic icons for panel app-icons until themes have
  better coverage.

* Mon Jul  6 2015 Ian Firns <firnsy@kororaproject.org> - 0.4-1
- Updated for latest dash-to-dock

* Thu Jan  8 2015 Ian Firns <firnsy@kororaproject.org> - 0.3-1
- Added theming support for workspaces-to-dock

* Wed Dec 31 2014 Ian Firns <firnsy@kororaproject.org> - 0.2-1
- Tweaks to font and calendar

* Wed Dec 17 2014 Ian Firns <firnsy@kororaproject.org> - 0.1-1
- Initial spec.
