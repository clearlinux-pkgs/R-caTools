#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-caTools
Version  : 1.17.1
Release  : 5
URL      : https://cran.r-project.org/src/contrib/caTools_1.17.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/caTools_1.17.1.tar.gz
Summary  : Tools: moving window statistics, GIF, Base64, ROC AUC, etc.
Group    : Development/Tools
License  : GPL-3.0
Requires: R-caTools-lib
Requires: R-bitops
Requires: R-fields
BuildRequires : R-bitops
BuildRequires : R-fields
BuildRequires : clr-R-helpers

%description
(rolling, running) window statistic functions, read/write for
        GIF and ENVI binary files, fast calculation of AUC, LogitBoost
        classifier, base64 encoder/decoder, round-off-error-free sum
        and cumsum, etc.

%package lib
Summary: lib components for the R-caTools package.
Group: Libraries

%description lib
lib components for the R-caTools package.


%prep
%setup -q -c -n caTools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523293482

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523293482
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library caTools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library caTools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library caTools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library caTools|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/caTools/DESCRIPTION
/usr/lib64/R/library/caTools/INDEX
/usr/lib64/R/library/caTools/Meta/Rd.rds
/usr/lib64/R/library/caTools/Meta/features.rds
/usr/lib64/R/library/caTools/Meta/hsearch.rds
/usr/lib64/R/library/caTools/Meta/links.rds
/usr/lib64/R/library/caTools/Meta/nsInfo.rds
/usr/lib64/R/library/caTools/Meta/package.rds
/usr/lib64/R/library/caTools/NAMESPACE
/usr/lib64/R/library/caTools/R/caTools
/usr/lib64/R/library/caTools/R/caTools.rdb
/usr/lib64/R/library/caTools/R/caTools.rdx
/usr/lib64/R/library/caTools/help/AnIndex
/usr/lib64/R/library/caTools/help/aliases.rds
/usr/lib64/R/library/caTools/help/caTools.rdb
/usr/lib64/R/library/caTools/help/caTools.rdx
/usr/lib64/R/library/caTools/help/paths.rds
/usr/lib64/R/library/caTools/html/00Index.html
/usr/lib64/R/library/caTools/html/R.css
/usr/lib64/R/library/caTools/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/caTools/libs/caTools.so
/usr/lib64/R/library/caTools/libs/caTools.so.avx2
/usr/lib64/R/library/caTools/libs/caTools.so.avx512