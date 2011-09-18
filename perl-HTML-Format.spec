Name:           perl-HTML-Format
Version:        2.04
Release: 	11.1%{?dist}
Summary:        HTML formatter modules

Group: 		Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/HTML-Format/
Source0:       	http://www.cpan.org/authors/id/S/SB/SBURKE/HTML-Format-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTML::Element) >= 3.15
BuildRequires:	perl(Font::AFM) >= 1.17

# These must match
# %FontFamilies in lib/HTML/FormatPS.pm
Requires: 	perl(Font::Metrics::Courier)
Requires: 	perl(Font::Metrics::CourierBold)
Requires: 	perl(Font::Metrics::CourierBoldOblique)
Requires: 	perl(Font::Metrics::CourierOblique)
Requires: 	perl(Font::Metrics::Helvetica)
Requires: 	perl(Font::Metrics::HelveticaBold)
Requires: 	perl(Font::Metrics::HelveticaBoldOblique)
Requires: 	perl(Font::Metrics::HelveticaOblique)
Requires: 	perl(Font::Metrics::TimesBold)
Requires: 	perl(Font::Metrics::TimesBoldItalic)
Requires: 	perl(Font::Metrics::TimesItalic)
Requires: 	perl(Font::Metrics::TimesRoman)


%description
A collection of modules that formats HTML as plaintext, PostScript or RTF.

%prep
%setup -q -n HTML-Format-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/HTML
%{_mandir}/man3/HTML*

%changelog
* Fri Jan 22 2010 Dennis Gregorovic <dgregor@redhat.com> - 2.04-11.1
- Rebuilt for RHEL 6
Related: rhbz#543948

* Thu Jul 02 2009 Jeff Fearn <jfearn@redhat.com> - 2.04-11
- bump for RHEL

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.04-8
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.04-7
- rebuild for new perl

* Mon Sep 03 2007 Ralf Corsépius <rc040203@freenet.de> - 2.04-6
- Update license tag.
- BR: perl(ExtUtils::MakeMaker).

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 2.04-5
- Mass rebuild.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 2.04-4
- Rebuild for perl-5.8.8.

* Wed Aug 31 2005 Ralf Corsepius <rc040203@freenet.de>	- 2.04-3
- Improve summary.

* Fri Aug 26 2005 Ralf Corsepius <ralf@links2linux.de>	- 2.04-2
- Add Requires: perl(Font::Metrics:*).
- Minor Spec cleanup.

* Thu Aug 18 2005 Ralf Corsepius <ralf@links2linux.de>	- 2.04-1
- FE submission.
