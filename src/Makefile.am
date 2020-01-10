tcllibdir = $(libdir)/TkXInput
tcllib_HEADERS = pkgIndex.tcl
tcllib_LTLIBRARIES = libwacomxi.la
dist_bin_SCRIPTS = wacomcpl-exec
bin_SCRIPTS= wacomcpl

xinitrcdir = $(sysconfdir)/X11/xinit/xinitrc.d
dist_xinitrc_SCRIPTS = wacomcpl.sh

EXTRA_DIST = GPL wacomcpl.in
CLEANFILES = wacomcpl

# Source dependencies
libwacomxi_la_SOURCES = wacomxi.c wacomxi.h
libwacomxi_la_LDFLAGS = -no-undefined $(XINPUT_LIBS)

SUBSTS = \
         -e 's|__bindir__|$(bindir)|g' \
         -e 's|__libdir__|$(libdir)|g'

wacomcpl: wacomcpl.in Makefile
	$(SED) $(SUBSTS) < $< > $@
	chmod +x $@

