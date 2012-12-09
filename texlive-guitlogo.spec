# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/GuIT/GuITlogo
# catalog-date 2009-11-09 22:36:07 +0100
# catalog-license lppl
# catalog-version 0.9.1
Name:		texlive-guitlogo
Version:	0.9.1
Release:	2
Summary:	Macros for typesetting the GuIT logo
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/GuIT/GuITlogo
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitlogo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitlogo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/guitlogo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Guit provides some commands useful to correctly write the logo
of "Gruppo Utilizzatori Italiani di TeX" (Italian TeX User
Group), using the default document color or any other color the
user may ever choose, in conformity with logo's scheme as seen
on the Group web site (http://www.guit.sssup.it). Likewise,
commands are provided that simplify the writing of GuIT
acronym's complete expansion, of the addresses of Group's
internet site and public forum and 'GuITmeeting' logo.
Optionally, using hyperref, the outputs of the above cited
commands can become hyperlinks to Group's site. Documentation
is available in Italian, only.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/guitlogo/guit.cfg
%{_texmfdistdir}/tex/latex/guitlogo/guit.sty
%doc %{_texmfdistdir}/doc/latex/guitlogo/README
%doc %{_texmfdistdir}/doc/latex/guitlogo/guit.pdf
%doc %{_texmfdistdir}/doc/latex/guitlogo/guittest.pdf
%doc %{_texmfdistdir}/doc/latex/guitlogo/guittest.tex
#- source
%doc %{_texmfdistdir}/source/latex/guitlogo/guit.dtx
%doc %{_texmfdistdir}/source/latex/guitlogo/guit.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9.1-2
+ Revision: 752455
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.9.1-1
+ Revision: 718593
- texlive-guitlogo
- texlive-guitlogo
- texlive-guitlogo
- texlive-guitlogo

