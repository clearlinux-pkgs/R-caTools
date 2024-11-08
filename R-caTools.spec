#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v18
# autospec commit: f35655a
#
Name     : R-caTools
Version  : 1.18.3
Release  : 63
URL      : https://cran.r-project.org/src/contrib/caTools_1.18.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/caTools_1.18.3.tar.gz
Summary  : Tools: Moving Window Statistics, GIF, Base64, ROC AUC, etc
Group    : Development/Tools
License  : GPL-3.0
Requires: R-caTools-lib = %{version}-%{release}
Requires: R-bitops
BuildRequires : R-bitops
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n caTools
pushd ..
cp -a caTools buildavx2
popd
pushd ..
cp -a caTools buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725492292

%install
export SOURCE_DATE_EPOCH=1725492292
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
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

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/caTools/NEWS
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

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/caTools/libs/caTools.so
/V4/usr/lib64/R/library/caTools/libs/caTools.so
/usr/lib64/R/library/caTools/libs/caTools.so
