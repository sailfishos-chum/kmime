%global pkgname kmime
%global  kde_version 25.08.2
%global  kf6_version 6.18.0

Name:       kde-kmime
Version:    25.08.2
Release:    1%{?dist}
License:    ASL-2.0 and BSD-3-Clause and CC0-1.0 and LGPLv2+
Summary:    Library to assist handling MIME data
Url:        https://invent.kde.org/pim/%{pkgname}
#Source0:    https://invent.kde.org/pim/%%{pkgname}/-/archive/v%%{version}/%%{pkgname}-v%%{version}.tar.bz2
Source0:    %{name}-%{version}.tar.bz2

Provides:   %{pkgname} = %{version}-%{release}

BuildRequires: kf6-extra-cmake-modules >= %kf6_version
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(shared-mime-info)

#BuildRequires: qt6-qtbase-devel
BuildRequires: pkgconfig(Qt6Core)
#BuildRequires: qt6-qtdeclarative-devel
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires:  qt6-qttools-devel

BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-karchive-devel
BuildRequires:  kf6-kcodecs-devel
BuildRequires:  kf6-kconfig-devel

%description
%{summary}.

%package    devel
Summary:    Development files for %{name}
License:    ASL-2.0 and BSD-3-Clause and CC0-1.0 and LGPLv2+
Requires:   %{name}%{?_isa} = %{version}-%{release}
Provides:   %{pkgname}-devel = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
#%%setup -q -n %%{pkgname}-v%%{version}
%autosetup -p1 -n %{name}-%{version}/upstream

%build

%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 libkmime6_qt

%files -f libkmime6_qt.lang
%defattr(-,root,root,-)
%{_kf6_datadir}/qlogging-categories6/*.categories
%{_kf6_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/KPim6/KMime/
%{_kf6_libdir}/*.so
%{_kf6_libdir}/cmake/KPim6Mime/
