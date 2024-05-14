#Source: https://stackoverflow.com/questions/50007534/type-error-not-str-bytes-like-object-is-required-python-3-6
with open(f'{flim.title}.jpg', 'wb') as f:
            f.write(requests.get(all_img[1]['src']).content)