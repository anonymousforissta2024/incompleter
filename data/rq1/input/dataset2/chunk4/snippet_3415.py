#Source: https://stackoverflow.com/questions/70855311/why-am-i-getting-a-type-error-int-not-iterable-while-using-plot-function
filenameWPC = root_name_of_output_file+'GenPwr'
figWPC = figure( 1, dpi = 152 )
figWPC.set_size_inches( 6, 4.05 )
subplots_adjust( left=.12, bottom=0.12,right=.95, top=.95, hspace=.02, wspace=.18 )

plt.errorbar(Vel, Power_[str('mean')], yerr=Power_[str('std')], 
dashes=lnsty[0],color=mkclr[0], clip_on=True,marker='o')

xlim(3,25.)
ylim(0,5500)
xlabel( 'Wind speed [m/s]' )   #NOVO
ylabel( 'Turbine Power [kW] '  )   #NOVO
yticks(np.arange(0,5500.01,500))
xticks(np.arange(3,25.01,1.))
grid(True)
savefig( ResFolder+filenameWPC +'.pdf')