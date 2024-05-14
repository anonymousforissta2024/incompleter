#Source: https://stackoverflow.com/questions/59437405/why-when-i-run-my-script-the-downloaded-image-files-have-zero-bytes-and-i-recei
imageFile = open(os.path.join('redditpics', os.path.basename(url)), 'wb')
for chunk in url.iter_content(100000):
    print("saving " + imageFile)

    imageFile.write(chunk)
imageFile.close()
print('Done.')