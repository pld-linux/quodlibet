#
# TODO:
# - check what's up with gstreamer backend
#
# Conditional build:
%bcond_without	home_etc	# don't use home_etc
#
%define		date 20050731
#
Summary:	Quod Libet - GTK+-based audio player
Summary(pl):	Quod Libet - odtwarzacz d¼wiêku oparty na GTK+
Name:		quodlibet
Version:	0.14
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.sacredchao.net/~piman/software/%{name}-%{version}.tar.gz
# Source0-md5:	b79a701d3fb769e37e0ec1aab49c4d65
Patch0:		%{name}-home_etc.patch
Patch1:		%{name}-Makefile.patch
URL:		http://www.sacredchao.net/quodlibet/wiki
BuildRequires:	gtk+2-devel >= 2.6.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
%pyrequires_eq	python-modules
Requires:	gtk+2 >= 2.6.0
Requires:	python-pygtk-gtk >= 2.6.0
Requires:	python-gnome-gconf
Requires:	python-gstreamer
Requires:	gstreamer-GConf
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

%description -l pl
Quod Libet to oparty na GTK+ odtwarzacz d¼wiêku napisany w Pythonie.
Jest zaprojektowany w oparciu o ideê, ¿e sami wiemy lepiej, jak chcemy
organizowaæ swoj± muzykê. Odtwarzacz pozwala tworzyæ playlisty w
oparciu o wyra¿enia regularne (nie jest to powód do zmartwienia,
zwyk³e wyszukiwanie te¿ dzia³a). Pozwala wy¶wietlaæ i modyfikowaæ
dowolne znaczniki w pliku. Umo¿liwia to dla wszystkich obs³ugiwanych
formatów d¼wiêkowych: Ogg Vorbis, FLAC, MP3, Musepack i MOD.

Aby u¿ywaæ wszystkich mo¿liwo¶ci Quod Libet (w³±cznie z odtwarzaniem
d¼wiêku) potrzebne s± tak¿e nastêpuj±ce pakiety: python-pyvorbis,
python-pyao, python-mad, python-pyid3lib.

%prep
%setup -q
%{?with_home_etc:%patch0 -p1}
%patch1 -p1

%build
%{__make} extensions
%{__make} po-data

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
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
- python-mad and gstreamer-mad (for MP3s)
- python-pyvorbis and gstreamer-vorbis (for Ogg Vorbis)
and audio output:
- gstreamer-audiosink-(alsa|oss|esd) (for ALSA,OSS or ESD output)
EOF

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.py
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.png
%{_libdir}/%{name}/*.zip
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man1/*
