### update direction field
```
rtrim(string_to_array(  "filename", '_' )[7],'°')
```


### photo visualisation
```html
<img src="file:///[% photo %]" width="350" height="250">
```


### ZonalStats
```sql

select min(date), max(date) from  gpsZonalStat_Laisamis

-- drop table import

insert into gpsZonalStat_Laisamis (geom,id ,name ,date ,speed ,formated_time ,"Longitude E/W" ,"Latitude N/S" ,ndvi1 ,_count ,_mean ,_median ,_stdev ,_min,_max ,_range ,_minority ,_majority ,_variance )
select geom,id ,name ,date ,speed ,formated_time ,"Longitude E/W" ,"Latitude N/S" ,ndvi1 ,_count ,_mean ,_median ,_stdev ,_min ,_max ,_range ,_minority ,_majority ,_variance
from import
```

### get GPS points related to NDVI S2
```sql
select * from gps_data
where date between 240729 and 240802;
select * from gps_data
where date between 240803 and 240807;
select * from gps_data
where date between 240808 and 240812;
select * from gps_data
where date between 240813 and 240817;
select * from gps_data
where date between 240818 and 240822;
```

### season flag
```
CASE
    WHEN month("stop_start") IN (1, 2, 3) and year("stop_start") = 2024 THEN '2024_Dry_1'
    WHEN month("stop_start") IN (4, 5, 6) and year("stop_start") = 2024 THEN '2024_Wet_1'
    WHEN month("stop_start") IN (7, 8, 9) and year("stop_start") = 2024 THEN '2024_Dry_2'
    WHEN month("stop_start") IN (10, 11, 12) and year("stop_start") = 2024 THEN '2024_Wet_2'
    WHEN month("stop_start") IN (1, 2, 3) and year("stop_start") = 2025 THEN '2025_Dry_1'
    WHEN month("stop_start") IN (4, 5, 6) and year("stop_start") = 2025 THEN '2025_Wet_1'
    WHEN month("stop_start") IN (7, 8, 9) and year("stop_start") = 2025 THEN '2025_Dry_2'
    WHEN month("stop_start") IN (10, 11, 12) and year("stop_start") = 2025 THEN '2025_Wet_2'

    ELSE 'Unknown'
END
```
sqlite update
```
insert into gps_data
SELECT *,
    CASE
        WHEN (("date" / 10000) + 2000) = 2024 AND (("date" / 100 % 100) IN (1,2,3))
            THEN '2024_Dry_1'
        WHEN (("date" / 10000) + 2000) = 2024 AND (("date" / 100 % 100) IN (4,5,6))
            THEN '2024_Wet_1'
        WHEN (("date" / 10000) + 2000) = 2024 AND (("date" / 100 % 100) IN (7,8,9))
            THEN '2024_Dry_2'
        WHEN (("date" / 10000) + 2000) = 2024 AND (("date" / 100 % 100) IN (10,11,12))
            THEN '2024_Wet_2'

        WHEN (("date" / 10000) + 2000) = 2025 AND (("date" / 100 % 100) IN (1,2,3))
            THEN '2025_Dry_1'
        WHEN (("date" / 10000) + 2000) = 2025 AND (("date" / 100 % 100) IN (4,5,6))
            THEN '2025_Wet_1'
        WHEN (("date" / 10000) + 2000) = 2025 AND (("date" / 100 % 100) IN (7,8,9))
            THEN '2025_Dry_2'
        WHEN (("date" / 10000) + 2000) = 2025 AND (("date" / 100 % 100) IN (10,11,12))
            THEN '2025_Wet_2'

        ELSE 'Unknown'
    END AS season
FROM gps_data_raw;
```
