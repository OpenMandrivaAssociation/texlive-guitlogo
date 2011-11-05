# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/GuIT/GuITlogo
# catalog-date 2009-11-09 22:36:07 +0100
# catalog-license lppl
# catalog-version 0.9.1
Name:		texlive-guitlogo
Version:	0.9.1
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
