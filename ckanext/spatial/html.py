PACKAGE_MAP="""
<hr class="cleared" />
<div class="dataset-map subsection">
<h3>%(title)s</h3>
<div id="dataset-map-container"></div>
<div id="dataset-map-attribution">Map data CC-BY-SA by <a href="http://openstreetmap.org">OpenStreetMap</a> | Tiles courtesy of <a href="http://www.mapquest.com">MapQuest</a></div>
</div>
"""

PACKAGE_MAP_EXTRA_HEADER="""
    <link type="text/css" rel="stylesheet" media="all" href="/ckanext/spatial/css/dataset_map.css" />
"""

PACKAGE_MAP_EXTRA_FOOTER="""
    <script type="text/javascript" src="/ckanext/spatial/js/openlayers/OpenLayers_dataset_map.js"></script>
    <script type="text/javascript" src="/ckanext/spatial/js/dataset_map.js"></script>
    <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function(){
            CKAN.DatasetMap.extent = '%(extent)s';
            CKAN.DatasetMap.setup();
        })
        //]]>
    </script>


"""

WMS_PREVIEW="""
<div id="wms-preview" class="row span-24">
    <div id="map" class="span-16"></div>
    <div id="layers" class="span-8"></div>
    </div>

"""


WMS_PREVIEW_EXTRA_HEADER="""
        <link type="text/css" rel="stylesheet" media="all" href="/ckanext/spatial/css/wms_preview.css" />
"""

WMS_PREVIEW_EXTRA_FOOTER="""
        <script type="text/javascript" src="/ckanext/spatial/js/openlayers/OpenLayers_wms_preview.js"></script>
        <script type="text/javascript" src="/ckanext/spatial/js/wms_preview.js"></script>
      <script type="text/javascript">
        //<![CDATA[
        $(document).ready(function(){
            CKAN.WMSPreview.setup("%(wms_url)s");
        })
        //]]>
      </script>


"""
