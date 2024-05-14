#Source: https://stackoverflow.com/questions/54055170/filenotfounderror-errno-2-no-such-file-or-directory-after-resizing-the-images
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)        
    profile_image = models.ImageField(upload_to='profile_images/', default='', blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        im = Image.open(self.profile_image)
        output = BytesIO()
        basewidth = 300
        wpercent = (basewidth/float(im.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        im = im.resize((basewidth, hsize))
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.profile_image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.profile_image.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(Profile, self).save()