## Columbus data visualisation via QGIS and SPATILITE

```sql
select date, MakePoint( CAST(replace("Longitude E/W",'E','') as decimal),
						CASE 	WHEN "Latitude N/S" like '%S' 
								THEN CAST('-'||replace("Latitude N/S",'S','') as decimal) 
								ELSE (CAST(replace("Latitude N/S",'N','') as decimal)) END,4326) as geom
								
		, MakeLine(MakePoint( CAST(replace("Longitude E/W",'E','') as decimal),
						CASE 	WHEN "Latitude N/S" like '%S' 
								THEN CAST('-'||replace("Latitude N/S",'S','') as decimal) 
								ELSE (CAST(replace("Latitude N/S",'N','') as decimal)) END,4326)) as geom_line
from kenya
group by date
```
## time format
```sql
select id, TIME, DATE,
		CASE WHEN length(TIME) = 4 THEN '00'||':'||substr(TIME, 1, 2) || ':' || substr(TIME, 3, 2)
			 WHEN length(TIME) = 5 THEN '0'||substr(TIME, 1,1)|| ':' ||substr(TIME, 2, 2) ||':'|| substr(TIME, 4, 2)
			 WHEN length(TIME) = 6 THEN substr(TIME, 1,2) || ':' || substr(TIME, 3, 2) || substr(TIME, 5, 2)
			ELSE 'Invalid UTC time' END as formated_time,
		MakePoint( CAST(replace("Longitude E/W",'E','') as decimal),
						CASE 	WHEN "Latitude N/S" like '%S' 
								THEN CAST('-'||replace("Latitude N/S",'S','') as decimal) 
								ELSE (CAST(replace("Latitude N/S",'N','') as decimal)) END,4326) as geom




from "oneday231214" 
order by id
```
## everything so far ;-)
```sql
select  *,
		CASE WHEN length(TIME) = 4 THEN '00'||':'||substr(TIME, 1, 2) || ':' || substr(TIME, 3, 2)
			 WHEN length(TIME) = 5 THEN '0'||substr(TIME, 1,1)|| ':' ||substr(TIME, 2, 2) ||':'|| substr(TIME, 4, 2)
			 WHEN length(TIME) = 6 THEN substr(TIME, 1,2) || ':' || substr(TIME, 3, 2) || substr(TIME, 5, 2)
			ELSE 'Invalid UTC time' END as formated_time, 
		MakePoint( CAST(replace("Longitude E/W",'E','') as decimal),
						CASE 	WHEN "Latitude N/S" like '%S' 
								THEN CAST('-'||replace("Latitude N/S",'S','') as decimal) 
								ELSE (CAST(replace("Latitude N/S",'N','') as decimal)) END,4326) as geom
								
	--	, MakeLine(MakePoint( CAST(replace("Longitude E/W",'E','') as decimal),
	--					CASE 	WHEN "Latitude N/S" like '%S' 
	--							THEN CAST('-'||replace("Latitude N/S",'S','') as decimal) 
	--							ELSE (CAST(replace("Latitude N/S",'N','') as decimal)) END,4326)) as geom_line
from wako_diba_complete_gps
group by date
```

### save as table with geom column
```sql
CREATE TABLE gps_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Optional, for unique row IDs
    time TEXT,
    formated_time TEXT,
    "Longitude E/W" TEXT,
    "Latitude N/S" TEXT,
    geom GEOMETRY -- Geometry column
);

SELECT AddGeometryColumn('gps_data', 'geom', 4326, 'POINT', 'XY');


INSERT INTO gps_data (time, formated_time, "Longitude E/W", "Latitude N/S", geom)
SELECT 
    TIME,
    CASE 
        WHEN length(TIME) = 4 THEN '00'||':'||substr(TIME, 1, 2) || ':' || substr(TIME, 3, 2)
        WHEN length(TIME) = 5 THEN '0'||substr(TIME, 1, 1)|| ':' ||substr(TIME, 2, 2) ||':'|| substr(TIME, 4, 2)
        WHEN length(TIME) = 6 THEN substr(TIME, 1, 2) || ':' || substr(TIME, 3, 2) || ':' || substr(TIME, 5, 2)
        ELSE 'Invalid UTC time' 
    END as formated_time,
    "Longitude E/W",
    "Latitude N/S",
    MakePoint(
        CAST(replace(longitude, 'E', '') as decimal),
        CASE 
            WHEN latitude like '%S' THEN CAST('-'||replace("Latitude N/S", 'S', '') as decimal) 
            ELSE CAST(replace(latitude, 'N', '') as decimal) 
        END,
        4326
    ) as geom
FROM combined_gps_data;
```

## catLog
```sql

select makeline(makepoint(CAST(replace("Longitude",',','.')as decimal),CAST(replace("Latitude",',','.')as decimal),4326)) as geom,
date,
time 
from log8
group by date

```
## infoRange API
```
select 	*, MakePoint(cast(long as decimal), cast(lat as decimal),4326) as geom							
	, MakeLine( MakePoint(cast(long as decimal), cast(lat as decimal),4326)) as geom_line
from gps
```
