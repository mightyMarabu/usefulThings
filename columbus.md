## Columbus data visualisation via QGIS and SPATILITE

```sql
select date, MakePoint( CAST(replace("Longitude E/W",'E','') as decimal),
						CASE 	WHEN "Latitude N/S" like '%S' 
								THEN CAST('-'||replace("Latitude N/S",'S','') as decimal) 
								ELSE (CAST(replace("Latitude N/S",'N','') as decimal)) END,4326) as geom,
		MakeLine(MakePoint( CAST(replace("Longitude E/W",'E','') as decimal),
						CASE 	WHEN "Latitude N/S" like '%S' 
								THEN CAST('-'||replace("Latitude N/S",'S','') as decimal) 
								ELSE (CAST(replace("Latitude N/S",'N','') as decimal)) END,4326)) as geom_line
from kenya
group by date
```