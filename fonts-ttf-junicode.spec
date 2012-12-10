%define version 0.6.11
%define fversion 0-6-11
%define release %mkrel 8

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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires: fontconfig
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

%files
%defattr(-,root,root,-)
%doc ChangeLog
%{_datadir}/fonts/ttf/junicode
%{_sysconfdir}/X11/fontpath.d/ttf-junicode:pri=50


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.6.11-8mdv2011.0
+ Revision: 675574
- br fontconfig for fc-query used in new rpm-setup-build

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.11-7mdv2011.0
+ Revision: 610734
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.6.11-6mdv2010.1
+ Revision: 494147
- fc-cache is now called by an rpm filetrigger

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.6.11-5mdv2010.0
+ Revision: 428849
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.6.11-4mdv2009.0
+ Revision: 245280
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.6.11-2mdv2008.1
+ Revision: 136417
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 06 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 0.6.11-2mdv2008.0
+ Revision: 49189
- fontpath.d conversion (#31756)
- Import fonts-ttf-junicode




* Thu Aug 31 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.6.11-1mdv2007.0
- new release (#22092)
- use %%mkrel
- new URL
- fix source0

* Wed Feb 08 2006 Frederic Crozat <fcrozat@mandriva.com> 0.6.4-2mdk
- Fix prereq
- Fix post/postun scripts

* Thu Dec 23 2004 Abel Cheung <deaddog@mandrake.org> 0.6.4-1mdk
- First Mandrakelinux package submitted by
  Roberto Rosselli Del Turco <rosselli@ling.unipi.it>
