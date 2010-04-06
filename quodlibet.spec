#
# Conditional build:
%bcond_without	home_etc	# don't use home_etc
#
Summary:	Quod Libet - GTK+-based audio player
Summary(pl.UTF-8):	Quod Libet - odtwarzacz dźwięku oparty na GTK+
Name:		quodlibet
Version:	2.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://quodlibet.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	8e2bf197afbfca98975d0f2103629d2d
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-nopy.patch
URL:		http://code.google.com/p/quodlibet/
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
# 2.5 needed for ctypes
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pygtk-devel >= 2:2.6.0
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	gstreamer-GConf
Requires:	gstreamer-audio-effects-base
Requires:	gtk+2 >= 2:2.6.0
Requires:	python-gnome-gconf
Requires:	python-gstreamer >= 0.10.2-2
Requires:	python-mutagen >= 1.11
Requires:	python-pycairo
Requires:	python-pygtk-gtk >= 2:2.6.0
Suggests:	gstreamer-audiosink
Suggests:	gstreamer-mad
Suggests:	gstreamer-vorbis
Suggests:	gstreamer-musepack
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
%{?with_home_etc:%patch0 -p1}
%patch1 -p1
rm -f po/gl_ES.po

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
%{__python} ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitedir} \
	--optimize=2

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
%dir %{py_sitedir}/%{name}/debug
%{py_sitedir}/%{name}/debug/*.py[co]
%{py_sitedir}/%{name}/devices
%dir %{py_sitedir}/%{name}/formats
%{py_sitedir}/%{name}/formats/*.py[co]
%dir %{py_sitedir}/%{name}/images
%{py_sitedir}/%{name}/images/*.png
%{py_sitedir}/%{name}/images/*.svg
%dir %{py_sitedir}/%{name}/library
%{py_sitedir}/%{name}/library/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{name}/*.so
%dir %{py_sitedir}/%{name}/parse
%{py_sitedir}/%{name}/parse/*.py[co]
%dir %{py_sitedir}/%{name}/player
%{py_sitedir}/%{name}/player/*.py[co]
%dir %{py_sitedir}/%{name}/plugins
%{py_sitedir}/%{name}/plugins/*.py[co]
%dir %{py_sitedir}/%{name}/qltk
%{py_sitedir}/%{name}/qltk/*.py[co]
%dir %{py_sitedir}/%{name}/util
%{py_sitedir}/%{name}/util/*.py[co]
%{_desktopdir}/*.desktop
#%{_pixmapsdir}/*
%{_mandir}/man1/*
