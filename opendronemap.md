```
 sudo docker run -d -it --rm
                  -v "$(pwd)/data/spots/DJI_20250401_004_Ngurunit2/rgb:/code/images"
                  -v "$(pwd)/odm/orthophoto/n2/rgb:/code/odm_orthophoto"
                  -v "$(pwd)/odm/georeferencing/n2/rgb:/code/odm_georeferencing"
                  -v "$(pwd)/odm/report/n2/rgb:/code/odm_report"
                  -v "$(pwd)/odm/dem/n2/rgb:/code/odm_dem"
                  -v "$(pwd)/odm/texturing/n2/rgb:/code/odm_texturing"
  docker.io/opendronemap/odm
  --mesh-size 100000 --dtm --dem-resolution 2
```
