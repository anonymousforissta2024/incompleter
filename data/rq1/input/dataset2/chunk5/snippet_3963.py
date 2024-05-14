#Source: https://stackoverflow.com/questions/72013969/nameerror-name-mark-safe-is-not-defined-django
# "admin.py"

from django.contrib.admin.widgets import AdminFileWidget

class CustomAdminFileWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        result = []
        if hasattr(value, "url"):
            result.append(
                f'''<a href="{value.url}" target="_blank">
                      <img 
                        src="{value.url}" alt="{value}" 
                        width="100" height="100"
                        style="object-fit: cover;"
                      />
                    </a>'''
            )
        result.append(super().render(name, value, attrs, renderer))
        return mark_safe("".join(result))