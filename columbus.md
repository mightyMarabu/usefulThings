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
### min max time per day and user
```
SELECT id, name, date, speed, formated_time, geom
FROM gps_data
WHERE (name,date, formated_time) IN (
    SELECT name,date, MAX(formated_time)
    FROM gps_data
    GROUP BY name, date
    UNION
    SELECT name,date, MIN(formated_time)
    FROM gps_data
    GROUP BY name, date
)
order by date;

```



### save as table with geom column
```sql
CREATE TABLE gps_data (
    id INTEGER PRIMARY KEY,
    name TEXT,
	date INTEGER,
	speed FLOAT,
    formated_time TEXT,
    "Longitude E/W" TEXT,
    "Latitude N/S" TEXT
);

SELECT AddGeometryColumn('gps_data', 'geom', 4326, 'POINT', 'XY')

SELECT *
--delete 
FROM gps_data

INSERT INTO gps_data
SELECT 
    ID as id,
	NAME as name,
	DATE as date,
	SPEED as speed,
    CASE 
        WHEN length(TIME) = 4 THEN '00'||':'||substr(TIME, 1, 2) || ':' || substr(TIME, 3, 2)
        WHEN length(TIME) = 5 THEN '0'||substr(TIME, 1, 1)|| ':' ||substr(TIME, 2, 2) ||':'|| substr(TIME, 4, 2)
        WHEN length(TIME) = 6 THEN substr(TIME, 1, 2) || ':' || substr(TIME, 3, 2) || ':' || substr(TIME, 5, 2)
        ELSE 'Invalid UTC time' 
    END as formated_time,
    longitude,
    latitude,
    MakePoint(
        CAST(replace(longitude, 'E', '') as decimal),
        CASE 
            WHEN latitude like '%S' THEN CAST('-'||replace("Latitude N/S", 'S', '') as decimal) 
            ELSE CAST(replace(latitude, 'N', '') as decimal) 
        END,
        4326
    ) as geom
FROM combined_gps_data ;

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
