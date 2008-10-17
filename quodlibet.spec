#
# Conditional build:
%bcond_without	home_etc	# don't use home_etc
#
Summary:	Quod Libet - GTK+-based audio player
Summary(pl.UTF-8):	Quod Libet - odtwarzacz dźwięku oparty na GTK+
Name:		quodlibet
# 2.0 on DEVEL, finish it there first
Version:	1.0
Release:	2
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.sacredchao.net/~piman/software/%{name}-%{version}.tar.gz
# Source0-md5:	5c925b754bd8505a7a66f2ffcc5b5fe4
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-Makefile.patch
Patch2:		%{name}-paned.patch
URL:		http://www.sacredchao.net/quodlibet/wiki
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
Requires:       python-pycairo
Requires:	python-pygtk-gtk >= 2:2.6.0
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
%patch2 -p0
sed -i -e 's#lib/quodlibet#%{_lib}/%{name}#g' quodlibet.py

%build
%{__make} extensions
%{__make} po-data

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	TODEP="%{_lib}/%{name}" \
	LIBDIR=%{_libdir} \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

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
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.py
%dir %attr(755,root,root) %{_libdir}/%{name}/library
%attr(755,root,root) %{_libdir}/%{name}/library/*.py
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_libdir}/%{name}/browsers
%{_libdir}/%{name}/devices
%{_libdir}/%{name}/formats
%{_libdir}/%{name}/parse
%{_libdir}/%{name}/plugins
%{_libdir}/%{name}/qltk
%{_libdir}/%{name}/util
%{_libdir}/%{name}/*.png
%{_libdir}/%{name}/*.svg
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
