#Source: https://stackoverflow.com/questions/48887526/streamfield-typeerror-bool-object-is-not-iterable
class CardBlock(StructBlock):
    image = ImageChooserBlock()
    heading = CharBlock(classname="full title")
    caption = RichTextBlock()
    class Meta:
        icon = 'image'

class HomePage(Page):
    intro = RichTextField(blank=True)
    showcase_title = RichTextField(blank=True)
    card = StreamField([('card', CardBlock())], default=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        MultiFieldPanel([
            FieldPanel('showcase_title'),
            StreamFieldPanel('card'),
        ]),
    ]