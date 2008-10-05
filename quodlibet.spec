#
# Conditional build:
%bcond_without	home_etc	# don't use home_etc
#
Summary:	Quod Libet - GTK+-based audio player
Summary(pl.UTF-8):	Quod Libet - odtwarzacz dźwięku oparty na GTK+
Name:		quodlibet
Version:	2.0
Release:	0.2
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://quodlibet.googlecode.com/files/quodlibet-%{version}.tar.gz
# Source0-md5:	4ec9703b3ef7ecf5c6ecf1b8ac7773f4
Patch0:		%{name}-home_etc.patch
Patch2:		%{name}-paned.patch
URL:		http://code.google.com/p/quodlibet/
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
BuildRequires:  rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	gstreamer-GConf
Requires:	gstreamer-audio-effects-base
Requires:	gtk+2 >= 2:2.6.0
Requires:	python-gnome-gconf
Requires:	python-gstreamer >= 0.10.2-2
Requires:	python-mutagen >= 1.11
# for python-ctypes
Requires:	python-modules >= 1:2.5
Requires:	python-pygtk-gtk >= 2:2.10.0
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
mv po/gl_ES.po po/gl.po

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--install-purelib=%{py_sitedir} \
	--prefix=$RPM_BUILD_ROOT%{_prefix} \
	--install-scripts=%{_bindir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%find_lang %{name}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner %{name} -e << EOF
Remember to install appropriate python modules for files
you want to play:
- gstreamer-mad (for MP3s)
- gstreamer-vorbis (for Ogg Vorbis)
- gstreamer-musepack (for MPCs)
and audio output:
- gstreamer-audiosink-(alsa|oss|esd) (for ALSA, OSS or ESD output)
EOF

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitedir}/quodlibet
%dir %{py_sitedir}/quodlibet/browsers
%dir %{py_sitedir}/quodlibet/debug
%dir %{py_sitedir}/quodlibet/devices
%dir %{py_sitedir}/quodlibet/formats
%dir %{py_sitedir}/quodlibet/library
%dir %{py_sitedir}/quodlibet/parse
%dir %{py_sitedir}/quodlibet/player
%dir %{py_sitedir}/quodlibet/plugins
%dir %{py_sitedir}/quodlibet/qltk
%dir %{py_sitedir}/quodlibet/util
%dir %{py_sitedir}/quodlibet/images
%{py_sitedir}/quodlibet/*.py[co]
%{py_sitedir}/quodlibet/browsers/*.py[co]
%{py_sitedir}/quodlibet/debug/*.py[co]
%{py_sitedir}/quodlibet/devices/*.py[co]
%{py_sitedir}/quodlibet/formats/*.py[co]
%{py_sitedir}/quodlibet/library/*.py[co]
%{py_sitedir}/quodlibet/parse/*.py[co]
%{py_sitedir}/quodlibet/player/*.py[co]
%{py_sitedir}/quodlibet/plugins/*.py[co]
%{py_sitedir}/quodlibet/qltk/*.py[co]
%{py_sitedir}/quodlibet/util/*.py[co]
%{py_sitedir}/quodlibet/images/*.svg
%{py_sitedir}/quodlibet/images/*.png
%attr(755,root,root) %{py_sitedir}/quodlibet/*.so
%{py_sitedir}/*.egg-info
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
