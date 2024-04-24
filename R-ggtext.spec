#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-ggtext
Version  : 0.1.2
Release  : 1
URL      : https://cran.r-project.org/src/contrib/ggtext_0.1.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ggtext_0.1.2.tar.gz
Summary  : Improved Text Rendering Support for 'ggplot2'
Group    : Development/Tools
License  : GPL-2.0
Requires: R-ggplot2
Requires: R-gridtext
Requires: R-rlang
Requires: R-scales
BuildRequires : R-dplyr
BuildRequires : R-ggplot2
BuildRequires : R-gridtext
BuildRequires : R-rlang
BuildRequires : R-scales
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
complex formatted plot labels (titles, subtitles, facet labels,
    axis labels, etc.). Text boxes with automatic word wrap are also
    supported.

%prep
%setup -q -n ggtext

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713979211

%install
export SOURCE_DATE_EPOCH=1713979211
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ggtext/DESCRIPTION
/usr/lib64/R/library/ggtext/INDEX
/usr/lib64/R/library/ggtext/Meta/Rd.rds
/usr/lib64/R/library/ggtext/Meta/features.rds
/usr/lib64/R/library/ggtext/Meta/hsearch.rds
/usr/lib64/R/library/ggtext/Meta/links.rds
/usr/lib64/R/library/ggtext/Meta/nsInfo.rds
/usr/lib64/R/library/ggtext/Meta/package.rds
/usr/lib64/R/library/ggtext/Meta/vignette.rds
/usr/lib64/R/library/ggtext/NAMESPACE
/usr/lib64/R/library/ggtext/NEWS.md
/usr/lib64/R/library/ggtext/R/ggtext
/usr/lib64/R/library/ggtext/R/ggtext.rdb
/usr/lib64/R/library/ggtext/R/ggtext.rdx
/usr/lib64/R/library/ggtext/doc/index.html
/usr/lib64/R/library/ggtext/doc/plotting_text.R
/usr/lib64/R/library/ggtext/doc/plotting_text.Rmd
/usr/lib64/R/library/ggtext/doc/plotting_text.html
/usr/lib64/R/library/ggtext/doc/theme_elements.R
/usr/lib64/R/library/ggtext/doc/theme_elements.Rmd
/usr/lib64/R/library/ggtext/doc/theme_elements.html
/usr/lib64/R/library/ggtext/help/AnIndex
/usr/lib64/R/library/ggtext/help/aliases.rds
/usr/lib64/R/library/ggtext/help/figures/README-unnamed-chunk-10-1.png
/usr/lib64/R/library/ggtext/help/figures/README-unnamed-chunk-3-1.png
/usr/lib64/R/library/ggtext/help/figures/README-unnamed-chunk-4-1.png
/usr/lib64/R/library/ggtext/help/figures/README-unnamed-chunk-5-1.png
/usr/lib64/R/library/ggtext/help/figures/README-unnamed-chunk-6-1.png
/usr/lib64/R/library/ggtext/help/figures/README-unnamed-chunk-7-1.png
/usr/lib64/R/library/ggtext/help/figures/README-unnamed-chunk-8-1.png
/usr/lib64/R/library/ggtext/help/figures/README-unnamed-chunk-9-1.png
/usr/lib64/R/library/ggtext/help/ggtext.rdb
/usr/lib64/R/library/ggtext/help/ggtext.rdx
/usr/lib64/R/library/ggtext/help/paths.rds
/usr/lib64/R/library/ggtext/html/00Index.html
/usr/lib64/R/library/ggtext/html/R.css
/usr/lib64/R/library/ggtext/tests/figs/deps.txt
/usr/lib64/R/library/ggtext/tests/figs/element-markdown/margins-match-w-ggtext-and-ggplot2.svg
/usr/lib64/R/library/ggtext/tests/figs/element-textbox/plot-title-with-fixed-width.svg
/usr/lib64/R/library/ggtext/tests/figs/element-textbox/plot-title-with-styling.svg
/usr/lib64/R/library/ggtext/tests/figs/element-textbox/rotated-box-as-y-axis-title.svg
/usr/lib64/R/library/ggtext/tests/figs/element-textbox/simple-textbox-as-plot-title.svg
/usr/lib64/R/library/ggtext/tests/figs/geom-richtext/rotated-labels-w-colors.svg
/usr/lib64/R/library/ggtext/tests/figs/geom-textbox/rotated-boxes-w-colors-and-alignments.svg
/usr/lib64/R/library/ggtext/tests/testthat.R
/usr/lib64/R/library/ggtext/tests/testthat/helper-vdiffr.R
/usr/lib64/R/library/ggtext/tests/testthat/test-element-markdown.R
/usr/lib64/R/library/ggtext/tests/testthat/test-element-textbox.R
/usr/lib64/R/library/ggtext/tests/testthat/test-geom-richtext.R
/usr/lib64/R/library/ggtext/tests/testthat/test-geom-textbox.R