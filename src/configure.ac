dnl  Copyright 2010 Red Hat, Inc.
dnl Process this file with autoconf to create configure.

AC_PREREQ([2.57])
AC_INIT(wacomcpl,[0.10.0], [], wacomcpl)
AM_INIT_AUTOMAKE([foreign dist-bzip2])
AM_MAINTAINER_MODE

AM_CONFIG_HEADER(config.h)

AC_PROG_LIBTOOL
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_SED

AC_CHECK_LIB(tcl, Tcl_Init)
AC_CHECK_LIB(tk, Tk_Init)

PKG_CHECK_MODULES(XINPUT, x11 xext [xi >= 1.2] [inputproto >= 1.5])

AC_SUBST(XINPUT_CFLAGS)
AC_SUBST(XINPUT_LIBS)

AC_OUTPUT([Makefile])

