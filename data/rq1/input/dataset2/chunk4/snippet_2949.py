#Source: https://stackoverflow.com/questions/66932143/django-file-not-found-error-when-the-file-is-there
@receiver(post_save, sender=Post)
def create_uuid(sender, instance, created, **kwargs):
  if created:
    img_dir = instance.media.url
    img_dir_list = img_dir.split("/")
    img_ext = img_dir_list[-1].split(".")[0]
    im = Image.open(img_dir)
    
    new_width = 0
    for x in range(0, 3):
        new_width += 200
        new_height = int(new_width/image.width * image.height)
        image = im.resize((new_width, new_height))
        image.save(f"{settings.MEDIA_URL}posts/{img}{new_width}x{new_height}.{img_ext}")

    instance.save()