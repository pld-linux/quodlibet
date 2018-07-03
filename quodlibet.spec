# TODO: /usr/share/gnome-shell/search-providers/quodlibet-search-provider.ini
#
%define		module		quodlibet
%define		egg_name	quodlibet
Summary:	Quod Libet - GTK+-based audio player
Summary(pl.UTF-8):	Quod Libet - odtwarzacz dźwięku oparty na GTK+
Name:		quodlibet
Version:	4.0.2
Release:	2
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	https://github.com/quodlibet/quodlibet/releases/download/release-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f8f282e7cc43f2ec2148dd2e9d93808d
Patch0:		%{name}-nopy.patch
URL:		https://quodlibet.readthedocs.org
BuildRequires:	gettext-tools
BuildRequires:	intltool
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.719
Requires:	gdk-pixbuf2
Requires:	gobject-introspection
Requires:	gstreamer >= 1.0
#Requires:	gstreamer-GConf >= 1.0
Requires:	gstreamer-audio-effects-base >= 1.0
Requires:	gstreamer-plugins-base >= 1.0
Requires:	gtk+3
Requires:	pango
#Requires:	python-dbus
#Requires:	python-gstreamer >= 0.10.2-2
#Requires:	python-pygobject3
Requires:	python3-feedparser
Requires:	python3-mutagen >= 1.14
Suggests:	%{name}-plugins
Suggests:	gstreamer-audiosink
Suggests:	gstreamer-mad
Suggests:	gstreamer-musepack
Suggests:	gstreamer-vorbis
Suggests:	libgpod
Suggests:	libmodplug
#Suggests:	python-keybinder
Suggests:	udev-libs
Conflicts:	quodlibet-plugins < 2.9.82
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quod Libet is a GTK+-based audio player written in Python. It's
designed around the idea that you know better than we do how to
organize your music. It lets you make playlists based on regular
expressions (don't worry, regular searches work too). It lets you
display and edit any tags you want in the file. And it lets you do
this for all the file formats it supports -- Ogg Vorbis, FLAC, MP3,
Musepack, and MOD.

To use all of Quod Libet features (including audio playback) you will
also need the following packages: python-pyvorbis, python-pyao,
python-mad, python-pyid3lib.

%description -l pl.UTF-8
Quod Libet to oparty na GTK+ odtwarzacz dźwięku napisany w Pythonie.
Jest zaprojektowany w oparciu o ideę, że sami wiemy lepiej, jak chcemy
organizować swoją muzykę. Odtwarzacz pozwala tworzyć playlisty w
oparciu o wyrażenia regularne (nie jest to powód do zmartwienia,
zwykłe wyszukiwanie też działa). Pozwala wyświetlać i modyfikować
dowolne znaczniki w pliku. Umożliwia to dla wszystkich obsługiwanych
formatów dźwiękowych: Ogg Vorbis, FLAC, MP3, Musepack i MOD.

Aby używać wszystkich możliwości Quod Libet (włącznie z odtwarzaniem
dźwięku) potrzebne są także następujące pakiety: python-pyvorbis,
python-pyao, python-mad, python-pyid3lib.

%package -n exfalso
Summary:	Tag editor for various music files
Group:		X11/Applications/Multimedia
Requires:	gnome-icon-theme-symbolic
Requires:	gtk+3 >= 3.18
Requires:	gtk-webkit4
Requires:	hicolor-icon-theme
Requires:	libsoup >= 2.44
Requires:	pkgconfig
Requires:	python-pygobject3 >= 3.18
Requires:	python3 >= 1:3.5
Requires:	python3-feedparser
Requires:	python3-mutagen >= 1.14
# for musicbrainz plugin
#Requires:	python3-musicbrainzngs

%description -n exfalso
Ex Falso is a tag editor with the same tag editing interface as Quod
Libet, but it does not play files. Supported file formats include Ogg
Vorbis, MP3, FLAC, MOD/XM/IT, Musepack, Wavpack, and MPEG-4 AAC.

%prep
%setup -q
#%patch0 -p1

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

# adjust for pld path (no vendor support yet)
install -d $RPM_BUILD_ROOT%{zsh_compdir}
mv $RPM_BUILD_ROOT{%{_datadir}/zsh/vendor-completions,%{zsh_compdir}}/_quodlibet

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/operon
%attr(755,root,root) %{_bindir}/quodlibet
%{_mandir}/man1/operon.1*
%{_mandir}/man1/quodlibet.1*
%{_desktopdir}/quodlibet.desktop
%{_iconsdir}/hicolor/*/apps/quodlibet.png
%{_iconsdir}/hicolor/scalable/apps/quodlibet-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/quodlibet.svg
%{_datadir}/appdata/quodlibet.appdata.xml
%{_datadir}/dbus-1/services/net.sacredchao.QuodLibet.service
%{zsh_compdir}/_quodlibet
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%{py3_sitescriptdir}/%{module}

%files -n exfalso
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/exfalso
%{_mandir}/man1/exfalso.1*
%{_desktopdir}/exfalso.desktop
%{_iconsdir}/hicolor/*/apps/exfalso.png
%{_iconsdir}/hicolor/scalable/apps/exfalso-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/exfalso.svg
%{_datadir}/appdata/exfalso.appdata.xml
