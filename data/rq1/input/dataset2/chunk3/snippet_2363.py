#Source: https://stackoverflow.com/questions/62703755/typeerror-init-got-multiple-values-for-argument-center
import yt

ds = yt.load("puredef_hdf5_chk_000000")
p = yt.ProjectionPlot(ds,'particle_postion_x', 'particle_postion_y',['particle_dens'], center='m', width=(20, 'Mpc'))
p.annotate_particles((20, 'Mpc'))
p.save()