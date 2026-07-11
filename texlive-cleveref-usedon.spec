%global tl_name cleveref-usedon
%global tl_revision 70491

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4.0
Release:	%{tl_revision}.1
Summary:	Adds forward-referencing functionality to the cleveref package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/cleveref-usedon
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref-usedon.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref-usedon.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cleveref-usedon.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Imagine you are reading a long mathematical text such as a text book or
a thesis. There are plenty of supplementary lemmas, propositions,
theorems and/or exercises throughout the whole text. You ask yourself
"Gosh, while Lemma 1.12 is certainly an interesting result, where is
this result used later on in this long text? I really would find that
helpful to decide why I should read the proof." You can, of course, use
the PDF search function of your viewer to look up the string "Lemma
1.12", but wouldn't it be more helpful if Lemma 1.12 already indicated
all or at least its most useful/crucial applications via an info
message? This is what this package tries to address: The info message
"Used on p. 40, 43-45 and 101." would then be printed to the header of
Lemma 1.12. This is done by extending the \cref and \Cref commands and
giving them an optional argument UsedOn. Every time you wish to record a
reference in the "used on page list", you would simply type
\cref[UsedOn]{<LabelName>}. If you use \cref without this optional
argument, this reference won't be recorded in this page list.

