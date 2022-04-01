
download data from geofabrik and execute the following in the same folder

```
podman run -t -v "${PWD}:/data" docker.io/osrm/osrm-backend osrm-extract -p /opt/car.lua /data/germany-latest.osm.pbf
podman run -t -v "${PWD}:/data" docker.io/osrm/osrm-backend osrm-partition /data/germany-latest.osm.pbf
podman run -t -v "${PWD}:/data" docker.io/osrm/osrm-backend osrm-customize /data/germany-latest.osm.pbf
podman run -t -i -p 5000:5000 -v "${PWD}:/data" osrm/osrm-backend osrm-routed --algorithm mld /data/germany-latest.osm.pbf

```
