Name:           wacomcpl
Version:        0.10.0
Release:        3%{?dist}
Summary:        Wacom driver configuration tool

Group:          User Interface/X
License:        GPLv2+
URL:            http://people.redhat.com/~phuttere/wacomcpl/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:        http://people.redhat.com/~phuttere/wacomcpl/%{name}-%{version}.tar.bz2
Source1:        wacomcpl.desktop
Source2:        wacomcpl-icon.png

# For my sanity
Patch001: 0001-Check-for-AC_CHECK_LIB-success-when-testing-for-Tcl-.patch
Patch002: 0002-Rename-getDeviceOptionProc-to-updateDeviceOptionProc.patch
# Bug 711619 - wacomcpl - Fix set eraser mappings same as stylus
Patch003: 0003-Update-the-eraser-with-twinview-settings-711619.patch
# Bug 711618 - Allow multiple wacomcplrc files to be used 
Patch004: 0004-Allow-for-host-specific-wacomcplrc-711618.patch
# Bug 675672 - wacomcpl calibration slightly off with twiview set up to "leftOf"
Patch005: 0005-Read-default-area-values-before-starting-calibration.patch
Patch006: 0006-Calculate-the-device-relative-area-coordinates-not-s.patch
# related to Bug 711619
Patch007: 0007-When-resetting-TwinView-to-none-reset-the-TVResoluti.patch
# DTU-2231 support
Patch008: 0001-Add-DTU-2231-to-LCD-range.patch

# wacom driver doesn't exist on those
ExcludeArch:    s390 s390x

BuildRequires:  automake libtool
BuildRequires:  libX11-devel libXext-devel libXi-devel
BuildRequires:  tcl-devel tk-devel desktop-file-utils

Requires:       xorg-x11-drv-wacom >= 0.10.5-11
Requires:       libX11 libXi libXext
Requires:       tcl tk
# for xdpyinfo
Requires:       xorg-x11-utils

%description
%{name} is a graphical configuration tool for Wacom devices. It wraps the
xsetwacom command and provides an interface to some configuration options of
the xorg-x11-drv-wacom driver.

%prep
%setup -q
%patch001 -p1
%patch002 -p1
%patch003 -p1
%patch004 -p1
%patch005 -p1
%patch006 -p1
%patch007 -p1
%patch008 -p1

%build
autoreconf -v --force --install || exit 1
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

rm -f %{buildroot}%{_libdir}/TkXInput/libwacomxi.a %{buildroot}%{_libdir}/TkXInput/libwacomxi.la

install -d %{buildroot}%{_datadir}/wacomcpl
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/wacomcpl/wacomcpl.desktop
sed -i -e "s,DATADIR,%{_datadir}," %{buildroot}%{_datadir}/wacomcpl/wacomcpl.desktop

desktop-file-install --vendor gnome                             \
                --dir %{buildroot}%{_datadir}/applications      \
                --mode 0644                                     \
                --add-only-show-in GNOME                        \
                %{buildroot}%{_datadir}/wacomcpl/wacomcpl.desktop
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/wacomcpl/wacomcpl-icon.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/%{name}-exec
%doc GPL
%{_libdir}/TkXInput/libwacomxi.so*
%{_libdir}/TkXInput/pkgIndex.tcl
%{_sysconfdir}/X11/xinit/xinitrc.d/wacomcpl.sh
%{_datadir}/applications/gnome-wacomcpl.desktop
%{_datadir}/wacomcpl/wacomcpl.desktop
%{_datadir}/wacomcpl/wacomcpl-icon.png
%{_mandir}/man1/wacomcpl.1*

%changelog
* Fri Jul 22 2011 Peter Hutterer <peter.hutterer@redhat.com> 0.10.0-3
- Add DTU 2231 to list of LCD models (related #705210)

* Wed Jul 06 2011 Peter Hutterer <peter.hutterer@redhat.com> 0.10.0-2
- Fix cintiq calibration issues (#675672)
- Set eraser mappings same as stylus (#711619)
- Allow multiple wacomcplrc files to be used  (#711618)

* Fri Jul 01 2011 Peter Hutterer <peter.hutterer@redhat.com> 0.10.0-1
- wacomcpl 0.10.0 (#713864)
- Drop all patches, merged upstream

* Tue Apr 12 2011 Peter Hutterer <peter.hutterer@redhat.com> 0.9.0-3
- Add Cintiq support (#694346)

* Thu Feb 03 2011 Peter Hutterer <peter.hutterer@redhat.com> 0.9.0-3
- Multiple patches to address button mapping issues (#624560).
- update the screen number when updating
- requires updated xorg-x11-drv-wacom for the matching fixes to xsetwacom
  and the driver.

* Thu Oct 14 2010 Peter Hutterer <peter.hutterer@redhat.com> 0.9.0-2
- Multiple patches to address issues with TwinView calibration and setting
  (#624560)
- requires xorg-x11-drv-wacom-0.10.5-7 for TwinView fixes.

* Tue May 25 2010 Peter Hutterer <peter.hutterer@redhat.com> 0.9.0-1
- Initial package.
