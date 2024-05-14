#Source: https://stackoverflow.com/questions/65463949/getting-type-errorfunction-takes-exactly-6-arguments-5-given-while-using-imag
for i,img in enumerate(target_img_path):
  tils=image_slicer.slice(img,16)
  image_slicer.save_tiles(tils, directory='/content/drive/My Drive/tarsplt',prefix='{}'.format(i) ,format='tiff')