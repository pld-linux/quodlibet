Summary:	Quod Libet - GTK+-based audio player
Summary(pl):	Quod Libet - odtwarzacz d¼wiêku oparty na GTK+
Name:		quodlibet
Version:	0.10.1
Release:	1
Epoch:		0
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://www.sacredchao.net/~piman/software/%{name}-%{version}.tar.gz
# Source0-md5:	9a8f843f9f55414ea9bb173762f1fe39
Patch0:		%{name}-non_utf8_filenames.patch
URL:		http://www.sacredchao.net/quodlibet/wiki
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
%pyrequires_eq	python-modules
Requires:	gtk+2 >= 2.6.0
Requires:	python-pygtk-gtk >= 2.4.0
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
%patch0 -p1

%build
%{__make} extensions

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

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
