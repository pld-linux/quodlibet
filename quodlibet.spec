# TODO: /usr/share/gnome-shell/search-providers/quodlibet-search-provider.ini
#
Summary:	Quod Libet - GTK+-based audio player
Summary(pl.UTF-8):	Quod Libet - odtwarzacz dźwięku oparty na GTK+
Name:		quodlibet
Version:	3.0.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://quodlibet.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	38803746fc7b33ac3f692c384617a942
Patch0:		%{name}-nopy.patch
Patch1:		%{name}-desktop.patch
URL:		http://code.google.com/p/quodlibet/
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	rpm-pythonprov
Requires:	gdk-pixbuf2
Requires:	gobject-introspection
Requires:	gstreamer >= 1.0
#Requires:	gstreamer-GConf >= 1.0
Requires:	gstreamer-audio-effects-base >= 1.0
Requires:	gstreamer-plugins-base >= 1.0
Requires:	gtk+3
Requires:	pango
Requires:	python-dbus
Requires:	python-gstreamer >= 0.10.2-2
Requires:	python-modules >= 1:2.6
Requires:	python-mutagen >= 1.14
Requires:	python-pygobject3
Suggests:	%{name}-plugins
Suggests:	gstreamer-audiosink
Suggests:	gstreamer-mad
Suggests:	gstreamer-musepack
Suggests:	gstreamer-vorbis
Suggests:	libgpod
Suggests:	libmodplug
Suggests:	python-feedparser
Suggests:	python-keybinder
Suggests:	udev-libs
Conflicts:	quodlibet-plugins < 2.9.82
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%{__rm} po/gl_ES.po
mv po/cs{_CZ,}.po

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
%{__python} ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{py_sitedir}/%{name}/plugins/{editing,events,playorder,songsmenu}

%{__python} -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitedir} \
	--optimize=2

install quodlibet/images/hicolor/64x64/apps/{exfalso,quodlibet}.png $RPM_BUILD_ROOT%{_pixmapsdir}

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*.egg-info
%dir %{py_sitedir}/%{name}
%{py_sitedir}/%{name}/*.py[co]
%{py_sitedir}/%{name}/browsers
#%dir %{py_sitedir}/%{name}/debug
#%{py_sitedir}/%{name}/debug/*.py[co]
%{py_sitedir}/%{name}/devices
%dir %{py_sitedir}/%{name}/formats
%{py_sitedir}/%{name}/formats/*.py[co]
%{py_sitedir}/%{name}/images
%dir %{py_sitedir}/%{name}/library
%{py_sitedir}/%{name}/library/*.py[co]
%dir %{py_sitedir}/%{name}/parse
%{py_sitedir}/%{name}/parse/*.py[co]
%dir %{py_sitedir}/%{name}/player
%{py_sitedir}/%{name}/player/*.py[co]
%dir %{py_sitedir}/%{name}/plugins
%{py_sitedir}/%{name}/plugins/*.py[co]
%dir %{py_sitedir}/%{name}/plugins/editing
%dir %{py_sitedir}/%{name}/plugins/events
%dir %{py_sitedir}/%{name}/plugins/playorder
%dir %{py_sitedir}/%{name}/plugins/songsmenu
%dir %{py_sitedir}/%{name}/qltk
%{py_sitedir}/%{name}/qltk/*.py[co]
%dir %{py_sitedir}/%{name}/util
%{py_sitedir}/%{name}/util/*.py[co]
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_mandir}/man1/*
