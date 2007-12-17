%define version 0.6.11
%define fversion 0-6-11
%define release %mkrel 2

Summary:	Peter Baker's Junicode Fonts for medievalists
Name:		fonts-ttf-junicode
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Fonts/True type
URL:		http://junicode.sourceforge.net/
# (Abel) I'm lazy; zip file at http://www.engl.virginia.edu/OE/junicode/
Source0:	junicode-%fversion.zip
# from http://heanet.dl.sourceforge.net/sourceforge/junicode/junicode-source-0.6.11.tar.gz:
Source1:	junicode-changelog-0.6.11
Requires(post): fontconfig
Requires(postun): fontconfig
BuildArch:	noarch
BuildRequires:	freetype-tools

%description
This package contains the excellent Junicode font created by Peter
S. Baker. This font is especially suited for medievalists, as it offers
many characters common in languages as Old English, Old Norse, etc.,
but it is beautiful and elegant enough to be used for other purposes.

%prep
%setup -q -c %name-%version
install -m 644 %SOURCE1 ChangeLog

# clean useless dirs
rm -rf docs/.xvpics

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/junicode

cp *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/junicode
ttmkfdir $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/junicode > $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/junicode/fonts.dir
ln -s fonts.dir $RPM_BUILD_ROOT%{_datadir}/fonts/ttf/junicode/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/ttf/junicode \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-junicode:pri=50

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache 

%postun
if [ "$1" = 0 ]; then
  [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi

%files
%defattr(-,root,root,-)
%doc ChangeLog
%{_datadir}/fonts/ttf/junicode
%{_sysconfdir}/X11/fontpath.d/ttf-junicode:pri=50
