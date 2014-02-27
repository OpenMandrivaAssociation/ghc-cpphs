%global debug_package %{nil}
%define module cpphs

Summary:	A liberalised re-implementation of cpp, the C pre-processor for Haskell
Name:		ghc-%{module}
Version:	1.17.1
Release:	2
License:	LGPLv2.1+
Group:		Development/Other
Url:		http://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/cpphs/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
Requires(post,preun):	ghc
Obsoletes:	%{module} < 1.17.1-2
Provides:	%{module} = %{EVRD}

%description
Cpphs is a re-implementation of the C pre-processor that is both more
compatible with Haskell, and itself written in Haskell so that it can be
distributed with compilers.

This version of the C pre-processor is pretty-much feature-complete and
compatible with traditional (K&R) pre-processors. Additional features
include:
- a plain-text mode;
- an option to unlit literate code files;
- and an option to turn off macro-expansion.

%files
%{_bindir}/%{module}
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

