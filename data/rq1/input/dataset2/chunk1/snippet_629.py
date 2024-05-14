#Source: https://stackoverflow.com/questions/64218176/attributeerror-line2d-object-has-no-property-xlabel
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, send_file, make_response, render_template
#from flask_ngrok import run_with_ngrok
import io

app = Flask(__name__)
#run_with_ngrok(app) 

@app.route("/")
def home():
  dates = ['2010-11', '2011-12', '2012-13', '2013-14', '2014-15', '2015-16', '2016-17']
  steps = [9000, 9500.756, 9800.859, 10000.262, 9800.972, 10500.058, 11300.703]
  df= pd.DataFrame(
      {'date': dates, 'steps': steps})
  fig, axes = plt.subplots(nrows=1, ncols=1)
  major_xtick=[2,3,4,5,6,7]
  major_xticklabel=['2010-11','2011-12','2012-13','2013-14','2014-15','2015-16','2016-17']
  color=['blue','green','blue']
  ax=df.plot(ax=axes,figsize=(10,8),linewidth=2,marker='o',xlabel="Year" \
          ,ylabel="steps" \
          ,title="2dline plot" \
          ,xlim=(0,8),ylim=(2000,15000) \
          , color=color)
  ax.set_xticks(major_xtick)
  ax.set_xticklabels(major_xticklabel)
  ax.legend()
  bytes_image = io.BytesIO()
  plt.savefig(bytes_image, format='png')
  bytes_image.seek(0)
  bytes_obj = bytes_image #do_plot()
    
  # return render_template('create_plot.html', pfile='abc')
  # return "<h3>  {{ pfile }} is successfully created</h3>"
  return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')

#if __name__ == '__main__':
    # app.run(debug=False)
#    app.run()