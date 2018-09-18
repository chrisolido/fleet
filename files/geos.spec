Name: geos
Version: 3.7.0
Release:  0
Summary: GEOS (Geometry Engine - Open Source) is a C++ port of the Java Topology Suite (JTS). As such, it aims to contain the complete functionality of JTS in C++. This includes all the OpenGIS Simple Features for SQL spatial predicate functions and spatial operators, as well as specific JTS enhanced topology functions.
Group: https://trac.osgeo.org/geos
License: GPL
URL: https://trac.osgeo.org/geos
Vendor: https://trac.osgeo.org/geos
Source: http://download.osgeo.org/geos/geos-3.7.0.tar.bz2
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

/usr/bin/geos-config
/usr/include/geos.h
/usr/include/geos/algorithm/Angle.h
/usr/include/geos/algorithm/BoundaryNodeRule.h
/usr/include/geos/algorithm/CGAlgorithms.h
/usr/include/geos/algorithm/CentralEndpointIntersector.h
/usr/include/geos/algorithm/Centroid.h
/usr/include/geos/algorithm/CentroidArea.h
/usr/include/geos/algorithm/CentroidLine.h
/usr/include/geos/algorithm/CentroidPoint.h
/usr/include/geos/algorithm/ConvexHull.h
/usr/include/geos/algorithm/ConvexHull.inl
/usr/include/geos/algorithm/HCoordinate.h
/usr/include/geos/algorithm/InteriorPointArea.h
/usr/include/geos/algorithm/InteriorPointLine.h
/usr/include/geos/algorithm/InteriorPointPoint.h
/usr/include/geos/algorithm/LineIntersector.h
/usr/include/geos/algorithm/MCPointInRing.h
/usr/include/geos/algorithm/MinimumDiameter.h
/usr/include/geos/algorithm/NotRepresentableException.h
/usr/include/geos/algorithm/PointInRing.h
/usr/include/geos/algorithm/PointLocator.h
/usr/include/geos/algorithm/RayCrossingCounter.h
/usr/include/geos/algorithm/RobustDeterminant.h
/usr/include/geos/algorithm/SIRtreePointInRing.h
/usr/include/geos/algorithm/SimplePointInRing.h
/usr/include/geos/algorithm/distance/DiscreteFrechetDistance.h
/usr/include/geos/algorithm/distance/DiscreteHausdorffDistance.h
/usr/include/geos/algorithm/distance/DistanceToPoint.h
/usr/include/geos/algorithm/distance/PointPairDistance.h
/usr/include/geos/algorithm/locate/IndexedPointInAreaLocator.h
/usr/include/geos/algorithm/locate/PointOnGeometryLocator.h
/usr/include/geos/algorithm/locate/SimplePointInAreaLocator.h
/usr/include/geos/export.h
/usr/include/geos/geom.h
/usr/include/geos/geom/BinaryOp.h
/usr/include/geos/geom/Coordinate.h
/usr/include/geos/geom/Coordinate.inl
/usr/include/geos/geom/CoordinateArraySequence.h
/usr/include/geos/geom/CoordinateArraySequenceFactory.h
/usr/include/geos/geom/CoordinateArraySequenceFactory.inl
/usr/include/geos/geom/CoordinateFilter.h
/usr/include/geos/geom/CoordinateList.h
/usr/include/geos/geom/CoordinateSequence.h
/usr/include/geos/geom/CoordinateSequenceFactory.h
/usr/include/geos/geom/CoordinateSequenceFilter.h
/usr/include/geos/geom/Dimension.h
/usr/include/geos/geom/Envelope.h
/usr/include/geos/geom/Envelope.inl
/usr/include/geos/geom/Geometry.h
/usr/include/geos/geom/GeometryCollection.h
/usr/include/geos/geom/GeometryCollection.inl
/usr/include/geos/geom/GeometryComponentFilter.h
/usr/include/geos/geom/GeometryFactory.h
/usr/include/geos/geom/GeometryFactory.inl
/usr/include/geos/geom/GeometryFilter.h
/usr/include/geos/geom/IntersectionMatrix.h
/usr/include/geos/geom/LineSegment.h
/usr/include/geos/geom/LineSegment.inl
/usr/include/geos/geom/LineString.h
/usr/include/geos/geom/Lineal.h
/usr/include/geos/geom/LinearRing.h
/usr/include/geos/geom/Location.h
/usr/include/geos/geom/MultiLineString.h
/usr/include/geos/geom/MultiLineString.inl
/usr/include/geos/geom/MultiPoint.h
/usr/include/geos/geom/MultiPolygon.h
/usr/include/geos/geom/MultiPolygon.inl
/usr/include/geos/geom/Point.h
/usr/include/geos/geom/Polygon.h
/usr/include/geos/geom/Polygonal.h
/usr/include/geos/geom/PrecisionModel.h
/usr/include/geos/geom/PrecisionModel.inl
/usr/include/geos/geom/Puntal.h
/usr/include/geos/geom/Triangle.h
/usr/include/geos/geom/prep/AbstractPreparedPolygonContains.h
/usr/include/geos/geom/prep/BasicPreparedGeometry.h
/usr/include/geos/geom/prep/PreparedGeometry.h
/usr/include/geos/geom/prep/PreparedGeometryFactory.h
/usr/include/geos/geom/prep/PreparedLineString.h
/usr/include/geos/geom/prep/PreparedLineStringIntersects.h
/usr/include/geos/geom/prep/PreparedPoint.h
/usr/include/geos/geom/prep/PreparedPolygon.h
/usr/include/geos/geom/prep/PreparedPolygonContains.h
/usr/include/geos/geom/prep/PreparedPolygonContainsProperly.h
/usr/include/geos/geom/prep/PreparedPolygonCovers.h
/usr/include/geos/geom/prep/PreparedPolygonIntersects.h
/usr/include/geos/geom/prep/PreparedPolygonPredicate.h
/usr/include/geos/geom/util/ComponentCoordinateExtracter.h
/usr/include/geos/geom/util/CoordinateOperation.h
/usr/include/geos/geom/util/GeometryCombiner.h
/usr/include/geos/geom/util/GeometryEditor.h
/usr/include/geos/geom/util/GeometryEditorOperation.h
/usr/include/geos/geom/util/GeometryExtracter.h
/usr/include/geos/geom/util/GeometryTransformer.h
/usr/include/geos/geom/util/LinearComponentExtracter.h
/usr/include/geos/geom/util/PointExtracter.h
/usr/include/geos/geom/util/PolygonExtracter.h
/usr/include/geos/geom/util/ShortCircuitedGeometryVisitor.h
/usr/include/geos/geom/util/SineStarFactory.h
/usr/include/geos/geomUtil.h
/usr/include/geos/geomgraph.h
/usr/include/geos/geomgraph/Depth.h
/usr/include/geos/geomgraph/DirectedEdge.h
/usr/include/geos/geomgraph/DirectedEdge.inl
/usr/include/geos/geomgraph/DirectedEdgeStar.h
/usr/include/geos/geomgraph/Edge.h
/usr/include/geos/geomgraph/EdgeEnd.h
/usr/include/geos/geomgraph/EdgeEndStar.h
/usr/include/geos/geomgraph/EdgeIntersection.h
/usr/include/geos/geomgraph/EdgeIntersectionList.h
/usr/include/geos/geomgraph/EdgeList.h
/usr/include/geos/geomgraph/EdgeNodingValidator.h
/usr/include/geos/geomgraph/EdgeRing.h
/usr/include/geos/geomgraph/GeometryGraph.h
/usr/include/geos/geomgraph/GeometryGraph.inl
/usr/include/geos/geomgraph/GraphComponent.h
/usr/include/geos/geomgraph/Label.h
/usr/include/geos/geomgraph/Node.h
/usr/include/geos/geomgraph/NodeFactory.h
/usr/include/geos/geomgraph/NodeMap.h
/usr/include/geos/geomgraph/PlanarGraph.h
/usr/include/geos/geomgraph/Position.h
/usr/include/geos/geomgraph/Quadrant.h
/usr/include/geos/geomgraph/TopologyLocation.h
/usr/include/geos/geomgraph/index/EdgeSetIntersector.h
/usr/include/geos/geomgraph/index/MonotoneChain.h
/usr/include/geos/geomgraph/index/MonotoneChainEdge.h
/usr/include/geos/geomgraph/index/MonotoneChainIndexer.h
/usr/include/geos/geomgraph/index/SegmentIntersector.h
/usr/include/geos/geomgraph/index/SimpleEdgeSetIntersector.h
/usr/include/geos/geomgraph/index/SimpleMCSweepLineIntersector.h
/usr/include/geos/geomgraph/index/SimpleSweepLineIntersector.h
/usr/include/geos/geomgraph/index/SweepLineEvent.h
/usr/include/geos/geomgraph/index/SweepLineEventObj.h
/usr/include/geos/geomgraph/index/SweepLineSegment.h
/usr/include/geos/geomgraphindex.h
/usr/include/geos/geosAlgorithm.h
/usr/include/geos/index/ItemVisitor.h
/usr/include/geos/index/SpatialIndex.h
/usr/include/geos/index/bintree/Bintree.h
/usr/include/geos/index/bintree/Interval.h
/usr/include/geos/index/bintree/Key.h
/usr/include/geos/index/bintree/Node.h
/usr/include/geos/index/bintree/NodeBase.h
/usr/include/geos/index/bintree/Root.h
/usr/include/geos/index/chain/MonotoneChain.h
/usr/include/geos/index/chain/MonotoneChainBuilder.h
/usr/include/geos/index/chain/MonotoneChainOverlapAction.h
/usr/include/geos/index/chain/MonotoneChainSelectAction.h
/usr/include/geos/index/intervalrtree/IntervalRTreeBranchNode.h
/usr/include/geos/index/intervalrtree/IntervalRTreeLeafNode.h
/usr/include/geos/index/intervalrtree/IntervalRTreeNode.h
/usr/include/geos/index/intervalrtree/SortedPackedIntervalRTree.h
/usr/include/geos/index/quadtree/DoubleBits.h
/usr/include/geos/index/quadtree/IntervalSize.h
/usr/include/geos/index/quadtree/Key.h
/usr/include/geos/index/quadtree/Node.h
/usr/include/geos/index/quadtree/NodeBase.h
/usr/include/geos/index/quadtree/Quadtree.h
/usr/include/geos/index/quadtree/Root.h
/usr/include/geos/index/strtree/AbstractNode.h
/usr/include/geos/index/strtree/AbstractSTRtree.h
/usr/include/geos/index/strtree/Boundable.h
/usr/include/geos/index/strtree/BoundablePair.h
/usr/include/geos/index/strtree/GeometryItemDistance.h
/usr/include/geos/index/strtree/Interval.h
/usr/include/geos/index/strtree/ItemBoundable.h
/usr/include/geos/index/strtree/ItemDistance.h
/usr/include/geos/index/strtree/SIRtree.h
/usr/include/geos/index/strtree/STRtree.h
/usr/include/geos/index/sweepline/SweepLineEvent.h
/usr/include/geos/index/sweepline/SweepLineIndex.h
/usr/include/geos/index/sweepline/SweepLineInterval.h
/usr/include/geos/index/sweepline/SweepLineOverlapAction.h
/usr/include/geos/indexBintree.h
/usr/include/geos/indexChain.h
/usr/include/geos/indexQuadtree.h
/usr/include/geos/indexStrtree.h
/usr/include/geos/indexSweepline.h
/usr/include/geos/inline.h
/usr/include/geos/io.h
/usr/include/geos/io/ByteOrderDataInStream.h
/usr/include/geos/io/ByteOrderDataInStream.inl
/usr/include/geos/io/ByteOrderValues.h
/usr/include/geos/io/CLocalizer.h
/usr/include/geos/io/ParseException.h
/usr/include/geos/io/StringTokenizer.h
/usr/include/geos/io/WKBConstants.h
/usr/include/geos/io/WKBReader.h
/usr/include/geos/io/WKBWriter.h
/usr/include/geos/io/WKTReader.h
/usr/include/geos/io/WKTReader.inl
/usr/include/geos/io/WKTWriter.h
/usr/include/geos/io/Writer.h
/usr/include/geos/linearref/ExtractLineByLocation.h
/usr/include/geos/linearref/LengthIndexOfPoint.h
/usr/include/geos/linearref/LengthIndexedLine.h
/usr/include/geos/linearref/LengthLocationMap.h
/usr/include/geos/linearref/LinearGeometryBuilder.h
/usr/include/geos/linearref/LinearIterator.h
/usr/include/geos/linearref/LinearLocation.h
/usr/include/geos/linearref/LocationIndexOfLine.h
/usr/include/geos/linearref/LocationIndexOfPoint.h
/usr/include/geos/linearref/LocationIndexedLine.h
/usr/include/geos/noding.h
/usr/include/geos/noding/BasicSegmentString.h
/usr/include/geos/noding/FastNodingValidator.h
/usr/include/geos/noding/FastSegmentSetIntersectionFinder.h
/usr/include/geos/noding/GeometryNoder.h
/usr/include/geos/noding/IntersectionAdder.h
/usr/include/geos/noding/IntersectionFinderAdder.h
/usr/include/geos/noding/IteratedNoder.h
/usr/include/geos/noding/MCIndexNoder.h
/usr/include/geos/noding/MCIndexNoder.inl
/usr/include/geos/noding/MCIndexSegmentSetMutualIntersector.h
/usr/include/geos/noding/NodableSegmentString.h
/usr/include/geos/noding/NodedSegmentString.h
/usr/include/geos/noding/Noder.h
/usr/include/geos/noding/NodingValidator.h
/usr/include/geos/noding/Octant.h
/usr/include/geos/noding/OrientedCoordinateArray.h
/usr/include/geos/noding/ScaledNoder.h
/usr/include/geos/noding/SegmentIntersectionDetector.h
/usr/include/geos/noding/SegmentIntersector.h
/usr/include/geos/noding/SegmentNode.h
/usr/include/geos/noding/SegmentNodeList.h
/usr/include/geos/noding/SegmentPointComparator.h
/usr/include/geos/noding/SegmentSetMutualIntersector.h
/usr/include/geos/noding/SegmentString.h
/usr/include/geos/noding/SegmentStringUtil.h
/usr/include/geos/noding/SimpleNoder.h
/usr/include/geos/noding/SingleInteriorIntersectionFinder.h
/usr/include/geos/noding/SinglePassNoder.h
/usr/include/geos/noding/snapround/HotPixel.h
/usr/include/geos/noding/snapround/HotPixel.inl
/usr/include/geos/noding/snapround/MCIndexPointSnapper.h
/usr/include/geos/noding/snapround/MCIndexSnapRounder.h
/usr/include/geos/noding/snapround/SimpleSnapRounder.h
/usr/include/geos/nodingSnapround.h
/usr/include/geos/opBuffer.h
/usr/include/geos/opDistance.h
/usr/include/geos/opLinemerge.h
/usr/include/geos/opOverlay.h
/usr/include/geos/opPolygonize.h
/usr/include/geos/opPredicate.h
/usr/include/geos/opRelate.h
/usr/include/geos/opValid.h
/usr/include/geos/operation.h
/usr/include/geos/operation/GeometryGraphOperation.h
/usr/include/geos/operation/IsSimpleOp.h
/usr/include/geos/operation/buffer/BufferBuilder.h
/usr/include/geos/operation/buffer/BufferInputLineSimplifier.h
/usr/include/geos/operation/buffer/BufferOp.h
/usr/include/geos/operation/buffer/BufferParameters.h
/usr/include/geos/operation/buffer/BufferSubgraph.h
/usr/include/geos/operation/buffer/OffsetCurveBuilder.h
/usr/include/geos/operation/buffer/OffsetCurveSetBuilder.h
/usr/include/geos/operation/buffer/OffsetSegmentGenerator.h
/usr/include/geos/operation/buffer/OffsetSegmentString.h
/usr/include/geos/operation/buffer/RightmostEdgeFinder.h
/usr/include/geos/operation/buffer/SubgraphDepthLocater.h
/usr/include/geos/operation/distance/ConnectedElementLocationFilter.h
/usr/include/geos/operation/distance/ConnectedElementPointFilter.h
/usr/include/geos/operation/distance/DistanceOp.h
/usr/include/geos/operation/distance/FacetSequence.h
/usr/include/geos/operation/distance/FacetSequenceTreeBuilder.h
/usr/include/geos/operation/distance/GeometryLocation.h
/usr/include/geos/operation/distance/IndexedFacetDistance.h
/usr/include/geos/operation/intersection/Rectangle.h
/usr/include/geos/operation/intersection/RectangleIntersection.h
/usr/include/geos/operation/intersection/RectangleIntersectionBuilder.h
/usr/include/geos/operation/linemerge/EdgeString.h
/usr/include/geos/operation/linemerge/LineMergeDirectedEdge.h
/usr/include/geos/operation/linemerge/LineMergeEdge.h
/usr/include/geos/operation/linemerge/LineMergeGraph.h
/usr/include/geos/operation/linemerge/LineMerger.h
/usr/include/geos/operation/linemerge/LineSequencer.h
/usr/include/geos/operation/overlay/EdgeSetNoder.h
/usr/include/geos/operation/overlay/ElevationMatrix.h
/usr/include/geos/operation/overlay/ElevationMatrixCell.h
/usr/include/geos/operation/overlay/FuzzyPointLocator.h
/usr/include/geos/operation/overlay/LineBuilder.h
/usr/include/geos/operation/overlay/MaximalEdgeRing.h
/usr/include/geos/operation/overlay/MinimalEdgeRing.h
/usr/include/geos/operation/overlay/MinimalEdgeRing.inl
/usr/include/geos/operation/overlay/OffsetPointGenerator.h
/usr/include/geos/operation/overlay/OverlayNodeFactory.h
/usr/include/geos/operation/overlay/OverlayOp.h
/usr/include/geos/operation/overlay/OverlayResultValidator.h
/usr/include/geos/operation/overlay/PointBuilder.h
/usr/include/geos/operation/overlay/PolygonBuilder.h
/usr/include/geos/operation/overlay/snap/GeometrySnapper.h
/usr/include/geos/operation/overlay/snap/LineStringSnapper.h
/usr/include/geos/operation/overlay/snap/SnapIfNeededOverlayOp.h
/usr/include/geos/operation/overlay/snap/SnapOverlayOp.h
/usr/include/geos/operation/polygonize/EdgeRing.h
/usr/include/geos/operation/polygonize/PolygonizeDirectedEdge.h
/usr/include/geos/operation/polygonize/PolygonizeEdge.h
/usr/include/geos/operation/polygonize/PolygonizeGraph.h
/usr/include/geos/operation/polygonize/Polygonizer.h
/usr/include/geos/operation/predicate/RectangleContains.h
/usr/include/geos/operation/predicate/RectangleIntersects.h
/usr/include/geos/operation/predicate/SegmentIntersectionTester.h
/usr/include/geos/operation/relate/EdgeEndBuilder.h
/usr/include/geos/operation/relate/EdgeEndBundle.h
/usr/include/geos/operation/relate/EdgeEndBundleStar.h
/usr/include/geos/operation/relate/RelateComputer.h
/usr/include/geos/operation/relate/RelateNode.h
/usr/include/geos/operation/relate/RelateNodeFactory.h
/usr/include/geos/operation/relate/RelateNodeGraph.h
/usr/include/geos/operation/relate/RelateOp.h
/usr/include/geos/operation/sharedpaths/SharedPathsOp.h
/usr/include/geos/operation/union/CascadedPolygonUnion.h
/usr/include/geos/operation/union/CascadedUnion.h
/usr/include/geos/operation/union/GeometryListHolder.h
/usr/include/geos/operation/union/PointGeometryUnion.h
/usr/include/geos/operation/union/UnaryUnionOp.h
/usr/include/geos/operation/valid/ConnectedInteriorTester.h
/usr/include/geos/operation/valid/ConsistentAreaTester.h
/usr/include/geos/operation/valid/IsValidOp.h
/usr/include/geos/operation/valid/QuadtreeNestedRingTester.h
/usr/include/geos/operation/valid/RepeatedPointTester.h
/usr/include/geos/operation/valid/SimpleNestedRingTester.h
/usr/include/geos/operation/valid/SweeplineNestedRingTester.h
/usr/include/geos/operation/valid/TopologyValidationError.h
/usr/include/geos/planargraph.h
/usr/include/geos/planargraph/DirectedEdge.h
/usr/include/geos/planargraph/DirectedEdgeStar.h
/usr/include/geos/planargraph/Edge.h
/usr/include/geos/planargraph/GraphComponent.h
/usr/include/geos/planargraph/Node.h
/usr/include/geos/planargraph/NodeMap.h
/usr/include/geos/planargraph/PlanarGraph.h
/usr/include/geos/planargraph/Subgraph.h
/usr/include/geos/planargraph/algorithm/ConnectedSubgraphFinder.h
/usr/include/geos/platform.h
/usr/include/geos/precision.h
/usr/include/geos/precision/CommonBits.h
/usr/include/geos/precision/CommonBitsOp.h
/usr/include/geos/precision/CommonBitsRemover.h
/usr/include/geos/precision/EnhancedPrecisionOp.h
/usr/include/geos/precision/GeometryPrecisionReducer.h
/usr/include/geos/precision/MinimumClearance.h
/usr/include/geos/precision/PrecisionReducerCoordinateOperation.h
/usr/include/geos/precision/SimpleGeometryPrecisionReducer.h
/usr/include/geos/profiler.h
/usr/include/geos/simplify/DouglasPeuckerLineSimplifier.h
/usr/include/geos/simplify/DouglasPeuckerSimplifier.h
/usr/include/geos/simplify/LineSegmentIndex.h
/usr/include/geos/simplify/TaggedLineSegment.h
/usr/include/geos/simplify/TaggedLineString.h
/usr/include/geos/simplify/TaggedLineStringSimplifier.h
/usr/include/geos/simplify/TaggedLinesSimplifier.h
/usr/include/geos/simplify/TopologyPreservingSimplifier.h
/usr/include/geos/spatialIndex.h
/usr/include/geos/timeval.h
/usr/include/geos/triangulate/DelaunayTriangulationBuilder.h
/usr/include/geos/triangulate/IncrementalDelaunayTriangulator.h
/usr/include/geos/triangulate/VoronoiDiagramBuilder.h
/usr/include/geos/triangulate/quadedge/LastFoundQuadEdgeLocator.h
/usr/include/geos/triangulate/quadedge/LocateFailureException.h
/usr/include/geos/triangulate/quadedge/QuadEdge.h
/usr/include/geos/triangulate/quadedge/QuadEdgeLocator.h
/usr/include/geos/triangulate/quadedge/QuadEdgeSubdivision.h
/usr/include/geos/triangulate/quadedge/TrianglePredicate.h
/usr/include/geos/triangulate/quadedge/TriangleVisitor.h
/usr/include/geos/triangulate/quadedge/Vertex.h
/usr/include/geos/unload.h
/usr/include/geos/util.h
/usr/include/geos/util/Assert.h
/usr/include/geos/util/AssertionFailedException.h
/usr/include/geos/util/CoordinateArrayFilter.h
/usr/include/geos/util/GEOSException.h
/usr/include/geos/util/GeometricShapeFactory.h
/usr/include/geos/util/IllegalArgumentException.h
/usr/include/geos/util/IllegalStateException.h
/usr/include/geos/util/Interrupt.h
/usr/include/geos/util/Machine.h
/usr/include/geos/util/TopologyException.h
/usr/include/geos/util/UniqueCoordinateArrayFilter.h
/usr/include/geos/util/UnsupportedOperationException.h
/usr/include/geos/util/math.h
/usr/include/geos/version.h
/usr/include/geos_c.h
/usr/lib/libgeos-3.7.0.so
/usr/lib/libgeos.a
/usr/lib/libgeos.la
/usr/lib/libgeos.so
/usr/lib/libgeos_c.a
/usr/lib/libgeos_c.la
/usr/lib/libgeos_c.so
/usr/lib/libgeos_c.so.1
/usr/lib/libgeos_c.so.1.11.0

%changelog
* Sun Sep 16 2018 Build <chris.olido@gmail.com>

In this file, under % prep section you may noticed the macro “%setup -q -n %{name}-%{version}”. This macro executes the following command in the background.

cd /root/rpmbuild/BUILD
rm -rf geos-3.7.0
gzip -dc /root/rpmbuild/SOURCES/geos-3.7.0.tar.gz | tar -xvf -
if [ $? -ne 0 ]; then
  exit $?
fi
cd geos-3.7.0
cd /root/rpmbuild/BUILD/geos-3.7.0
chown -R root.root .
chmod -R a+rX,g-w,o-w .