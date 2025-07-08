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

### get GPS points related to NDVI S2

select * from gps_data
where date between 240729 and 240802;
select * from gps_data
where date between 240803 and 240807;
select * from gps_data
where date between 240808 and 240812;
select * from gps_data
where date between 240813 and 240817;
select * from gps_data
where date between 240818 and 240822;```

```
