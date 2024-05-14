#Source: https://stackoverflow.com/questions/65473488/type-error-in-functions-to-run-point-in-polygon-query-on-rapids
def create_iterations(start, end, batches):
    iterations = list(np.arange(start, end, batches))
    iterations.append(end)
    return iterations


pip_iterations = create_iterations(0, 264, 24)


#loop to do point in polygon query in a table
def perform_pip(cuda_df, cuspatial_data, polygon_name, iter_batch):
    cuda_df['borough'] = " "
    for i in range(len(iter_batch)-1):
        start = pip_iterations[i]
        end = pip_iterations[i+1]
        pip = cuspatial.point_in_polygon(cuda_df['pickup_longitude'], cuda_df['pickup_latitude'],
                                         cuspatial_data[0][start:end],  #poly_offsets
                                         cuspatial_data[1],  #poly_ring_offsets
                                         cuspatial_data[2]['x'],  #poly_points_x
                                         cuspatial_data[2]['y']  #poly_points_y
                                        )

        for i in pip.columns:
            cuda_df['borough'].loc[pip[i]] = polygon_name[i]
    return cuda_df