### update direction field
```
rtrim(string_to_array(  "filename", '_' )[7],'°')
```


### photo visualisation
```
<img src="file:///[% photo %]" width="350" height="250">
```


### ZonalStats
```

select min(date), max(date) from  gpsZonalStat_Laisamis

-- drop table import

insert into gpsZonalStat_Laisamis (geom,id ,name ,date ,speed ,formated_time ,"Longitude E/W" ,"Latitude N/S" ,ndvi1 ,_count ,_mean ,_median ,_stdev ,_min,_max ,_range ,_minority ,_majority ,_variance )
select geom,id ,name ,date ,speed ,formated_time ,"Longitude E/W" ,"Latitude N/S" ,ndvi1 ,_count ,_mean ,_median ,_stdev ,_min ,_max ,_range ,_minority ,_majority ,_variance
from import
```
