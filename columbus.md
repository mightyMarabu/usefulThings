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
