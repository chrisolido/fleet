Name: postgis
Version: 2.4.5
Release:  0
Summary: PostGIS is a spatial database extender for PostgreSQL object-relational database. It adds support for geographic objects allowing location queries to be run in SQL.
Group: http://www.postgis.net
License: GPL
URL: http://www.postgis.net
Vendor: http://www.postgis.net
Source: https://download.osgeo.org/postgis/source/postgis-2.4.5.tar.gz
Prefix: %{_prefix}
Packager: Christopher J. Olido
BuildRoot: %{_tmppath}/%{name}-root

%description
PostGIS is a spatial database extender for PostgreSQL object-relational database. It adds support for geographic objects allowing location queries to be run in SQL.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --mandir=%{_mandir} --sysconfdir=/etc --with-pgconfig=/usr/pgsql-10/bin/pg_config

make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%dir /usr/include/
%dir /usr/lib/
%dir /usr/pgsql-10/
/usr/include/liblwgeom.h
/usr/include/liblwgeom_topo.h
/usr/lib/liblwgeom-2.4.so.0
/usr/lib/liblwgeom-2.4.so.0.0.0
/usr/lib/liblwgeom.a
/usr/lib/liblwgeom.la
/usr/lib/liblwgeom.so
/usr/pgsql-10/bin/pgsql2shp
/usr/pgsql-10/bin/raster2pgsql
/usr/pgsql-10/bin/shp2pgsql
/usr/pgsql-10/lib/postgis-2.4.so
/usr/pgsql-10/lib/postgis_topology-2.4.so
/usr/pgsql-10/lib/rtpostgis-2.4.so
/usr/pgsql-10/share/contrib/postgis-2.4/legacy.sql
/usr/pgsql-10/share/contrib/postgis-2.4/legacy_gist.sql
/usr/pgsql-10/share/contrib/postgis-2.4/legacy_minimal.sql
/usr/pgsql-10/share/contrib/postgis-2.4/postgis.sql
/usr/pgsql-10/share/contrib/postgis-2.4/postgis_comments.sql
/usr/pgsql-10/share/contrib/postgis-2.4/postgis_for_extension.sql
/usr/pgsql-10/share/contrib/postgis-2.4/postgis_proc_set_search_path.sql
/usr/pgsql-10/share/contrib/postgis-2.4/postgis_restore.pl
/usr/pgsql-10/share/contrib/postgis-2.4/postgis_upgrade.sql
/usr/pgsql-10/share/contrib/postgis-2.4/postgis_upgrade_for_extension.sql
/usr/pgsql-10/share/contrib/postgis-2.4/raster_comments.sql
/usr/pgsql-10/share/contrib/postgis-2.4/rtpostgis.sql
/usr/pgsql-10/share/contrib/postgis-2.4/rtpostgis_for_extension.sql
/usr/pgsql-10/share/contrib/postgis-2.4/rtpostgis_legacy.sql
/usr/pgsql-10/share/contrib/postgis-2.4/rtpostgis_proc_set_search_path.sql
/usr/pgsql-10/share/contrib/postgis-2.4/rtpostgis_upgrade.sql
/usr/pgsql-10/share/contrib/postgis-2.4/rtpostgis_upgrade_for_extension.sql
/usr/pgsql-10/share/contrib/postgis-2.4/sfcgal_comments.sql
/usr/pgsql-10/share/contrib/postgis-2.4/spatial_ref_sys.sql
/usr/pgsql-10/share/contrib/postgis-2.4/topology.sql
/usr/pgsql-10/share/contrib/postgis-2.4/topology_comments.sql
/usr/pgsql-10/share/contrib/postgis-2.4/topology_upgrade.sql
/usr/pgsql-10/share/contrib/postgis-2.4/uninstall_legacy.sql
/usr/pgsql-10/share/contrib/postgis-2.4/uninstall_postgis.sql
/usr/pgsql-10/share/contrib/postgis-2.4/uninstall_rtpostgis.sql
/usr/pgsql-10/share/contrib/postgis-2.4/uninstall_topology.sql
/usr/pgsql-10/share/extension/postgis--2.0.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.0.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.0.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.0.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.0.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.0.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.0.6--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.0.7--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.1.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.1.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.1.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.1.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.1.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.1.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.1.6--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.1.7--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.1.8--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.1.9--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.2.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.2.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.2.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.2.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.2.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.2.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.2.6--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.2.7--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.3.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.3.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.3.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.3.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.3.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.3.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.3.6--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.3.7--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.4.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.4.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.4.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.4.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.4.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.4.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.4.5--2.4.5next.sql
/usr/pgsql-10/share/extension/postgis--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--2.4.5next--2.4.5.sql
/usr/pgsql-10/share/extension/postgis--unpackaged--2.4.5.sql
/usr/pgsql-10/share/extension/postgis.control
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.0.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.0.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.0.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.0.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.0.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.0.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.0.6--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.0.7--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.1.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.1.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.1.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.1.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.1.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.1.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.1.6--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.1.7--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.1.8--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.1.9--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.2.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.2.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.2.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.2.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.2.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.2.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.2.6--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.2.7--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.3.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.3.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.3.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.3.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.3.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.3.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.3.6--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.3.7--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.4.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.4.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.4.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.4.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.4.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.4.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.4.5--2.4.5next.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--2.4.5next--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder--unpackaged--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_tiger_geocoder.control
/usr/pgsql-10/share/extension/postgis_tiger_geocoder.sql
/usr/pgsql-10/share/extension/postgis_topology--2.0.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.0.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.0.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.0.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.0.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.0.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.0.6--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.0.7--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.1.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.1.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.1.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.1.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.1.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.1.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.1.6--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.1.7--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.1.8--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.1.9--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.2.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.2.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.2.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.2.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.2.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.2.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.2.6--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.2.7--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.3.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.3.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.3.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.3.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.3.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.3.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.3.6--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.3.7--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.4.0--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.4.1--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.4.2--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.4.3--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.4.4--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.4.5--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.4.5--2.4.5next.sql
/usr/pgsql-10/share/extension/postgis_topology--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--2.4.5next--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology--unpackaged--2.4.5.sql
/usr/pgsql-10/share/extension/postgis_topology.control

%changelog
* Sun Sep 16 2018 Build <chris.olido@gmail.com>

In this file, under % prep section you may noticed the macro “%setup -q -n %{name}-%{version}”. This macro executes the following command in the background.

cd /root/rpmbuild/BUILD
rm -rf postgis-2.4.5
gzip -dc /root/rpmbuild/SOURCES/postgis-2.4.5.tar.gz | tar -xvf -
