```
CREATE TABLE gps_filtered (
    speed FLOAT,
    time INTEGER,
    date INTEGER
);

-- Add the geometry column
SELECT AddGeometryColumn('gps_filtered', 'geom', 4326, 'POINT', 'XY');

INSERT INTO gps_filtered (speed, time, date, geom)
SELECT CAST("SPEED" AS FLOAT), 
       CAST("TIME" AS INTEGER), 
       CAST("DATE" AS INTEGER),
       MakePoint( CAST(replace("Longitude E/W", 'E', '') AS DECIMAL),
                  CASE  
                    WHEN "Latitude N/S" LIKE '%S' 
                    THEN CAST('-' || replace("Latitude N/S", 'S', '') AS DECIMAL)
                    ELSE CAST(replace("Latitude N/S", 'N', '') AS DECIMAL)
                  END, 4326) AS geom
FROM gps_latest
WHERE CAST("SPEED" AS FLOAT) < 10 
  AND CAST("DATE" AS INTEGER) BETWEEN 240615 AND 240715;
```
