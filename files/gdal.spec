Name:           gdal
Version:        gdal-2.3.1
Release:        0
Summary:        gdal is a translator library for raster and vector geospatial data formats that is released under an X/MIT style Open Source license by the Open Source Geospatial Foundation
Group:          http://www.gdal.org
License:        GPL
URL:            http://www.gdal.org
Vendor:         http://www.gdal.org
Source:         http://download.osgeo.org/gdal/2.3.1/gdal-2.3.1.tar.gz
Prefix:         %{_prefix}
Packager: 	    Christopher J. Olido
BuildRoot:      %{_tmppath}/%{name}-root

%description
gdal is a translator library for raster and vector geospatial data 
formats that is released under an X/MIT style Open Source license 
by the Open Source Geospatial Foundation

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --mandir=%{_mandir} --sysconfdir=/etc
mv README.md README

make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) /etc/%{name}.xml
%{_bindir}/gdal
%{_prefix}/share/gdal/*

%changelog
* Sun Sep 16 2018 Build <chris.olido@gmail.com>

In this file, under % prep section you may noticed the macro “%setup -q -n %{name}-%{version}”. This macro executes the following command in the background.

cd /root/rpmbuild/BUILD
rm -rf gdal
gzip -dc /root/rpmbuild/SOURCES/gdal-2.3.1.tar.gz | tar -xvvf -
if [ $? -ne 0 ]; then
  exit $?
fi
cd gdal
cd /root/rpmbuild/BUILD/gdal
chown -R root.root .
chmod -R a+rX,g-w,o-w .