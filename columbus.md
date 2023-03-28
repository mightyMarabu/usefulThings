## Columbus data visualisation via QGIS and SPATILITE

```sql
select date, MakePoint(CAST(replace("Longitude E/W",'E','') as decimal),CAST(replace("Latitude N/S",'N','') as decimal),4326) as geom,
		MakeLine(MakePoint(CAST(replace("Longitude E/W",'E','') as decimal),CAST(replace("Latitude N/S",'N','') as decimal),4326)) as geom_line
from markII
group by date
```