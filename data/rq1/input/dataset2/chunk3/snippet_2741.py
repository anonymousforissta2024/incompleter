#Source: https://stackoverflow.com/questions/62484518/i-get-a-type-error-when-posting-data-using-via-rest-it-says-i-may-have-a-writab
class Certificate(models.Model):
    certificate_name = models.CharField(max_length=50)
    template_img = models.ImageField(blank=True, default='', upload_to='certificate_templates')
    template_url = models.URLField(blank=True, default='')
    names_file = models.FileField(blank=True, default='', upload_to='names_files')
    names_csv = models.TextField(blank=True, default='')
    Y_RATIO = 1.6268

    def get_remote_image(self):
        if self.template_url and not self.template_img:
            img_result = requests.get(self.template_url)
            img_name = os.path.basename(self.template_url)
            with open(os.path.join(TEMP_DIR, img_name), 'wb') as img_file:
                img_file.write(img_result.content)
            self.template_img.save(
                img_name,
                open(os.path.join(TEMP_DIR, img_name), 'rb')
                )
            self.save()


    def clean(self):
        if not self.template_img and not self.template_url:
            raise ValidationError({'template_img': 'Either one of template_img or template_url should have a value.'})
        if not self.names_csv and not self.names_file:
            raise ValidationError({'names_csv': 'Either one of names_csv or names_file should have a value.'})


    def save(self):
        if self.template_url and not self.template_img:
            self.get_remote_image()
            super(Certificate, self).save()
        else:
            super(Certificate, self).save()