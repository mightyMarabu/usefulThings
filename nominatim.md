# nominatim
[Nominatim via Docker](https://hub.docker.com/r/mediagis/nominatim)

```
git clone https://github.com/mediagis/nominatim-docker.git

```
download country of interest from geofabrik an save it to:
___/home/me/nominatimdata___ (host)

build container
```
docker run -t -v /home/me/nominatimdata:/data nominatim  sh /app/init.sh /data/<your_country>.osm.pbf postgresdata 4
```
# API
### example
#### viewbox
```
http://baremetalbill:7070/search.php?q=kassel&polygon_geojson=1&viewbox=
```
#### (geo)json
```
http://baremetalbill:7070/search.php?q=kassel&format=geojson
http://baremetalbill:7070/search.php?q=kassel&format=json
```
#postgres
## Query the API
```sql
CREATE OR REPLACE FUNCTION geo.geocode(
	city varchar (50),
	postcode varchar (50),
	street varchar(50),
	no varchar(5)
	)
    RETURNS TABLE(osm_id bigint, lon double precision, lat double precision, display_name varchar(255), class text) 
    LANGUAGE 'plpython3u'

    COST 100
    VOLATILE 
    ROWS 1000
AS $BODY$

 import requests

 city = "kassel"
 street = "bluecherstr"
 postcode = "34123"
 no = "17"

 q = "%s,%s,%s,%s" %(city, postcode, street, no)

 adress = {"q":q}

 API =  "http://192.168.3.157:7070/search.php?format=json&q="

 response = requests.get(API, params = adress)

 data = response.json()

 result = [(item["osm_id"],item["lat"],item["lon"],item["display_name"],item["class"])for item in data]
 return result

$BODY$;
```
## prepare data
```sql
truncate geo.input;
insert into geo.input (id, ort, plz, strasse, no)
--select * from geo.input;
select 	p_id, ort, plz,
		trim(regexp_replace(strasse, '[^[:alpha:]\s]', '', 'g')),
		NULLIF(regexp_replace(strasse, '\D','','g'), '')::numeric
from patients.patients
where geom is null
```
## geocode & update data
```sql
update patients.patients
set osm_id = r.osm_id, lon = r.lon, lat = r.lat, display_name = r.display_name, class = r.class, geom = r.geom 
from geo.geocode_result as r
where p_id = r.id

```
