#Source: https://stackoverflow.com/questions/70104866/python-nonetype-attribute-error-using-to-file
with r.open("final_image.tif") as src:
    watershed_params = {
        'markers': 10000, # F1: 2500, F2, F3: 5000, F4: 10000
        'compactness': 0.0000001 # F1, F2, F3: 0.0001, F4: 0.0000001
    }
    image = src.read()
  
    rout = segmentation(model = watershed, params = watershed_params, image = image)
      
    vout = vectorize(image=rout, transform = src.transform,
                      crs=src.crs.to_proj4())
  
    vout = add_zonal_properties(image=image, transform= src.transform, 
      
                                  bands=[1, 2, 3], band_names=['red', 'green', 'blue'],
                                  stats=['mean','min','max','std'],
                                  gdf=vout)

    vout = add_shape_properties(rout, vout, ['area', 'perimeter',
                                              'eccentricity', 
                                              'equivalent_diameter',
                                              'major_axis_length',
                                              'minor_axis_length',
                                              'orientation'])

    edges = sobel_edge_detect(src, band=1)

      
    vout = add_zonal_properties(image= image, band_names=['sobel'],
                                  stats=['mean','min','max','std'],
                                  transform = src.transform, gdf=vout)
    
    vout.to_file("segmentation.gpkg", layer=f"seg-{idx}", driver="GPKG")
    
    print("All done!!")