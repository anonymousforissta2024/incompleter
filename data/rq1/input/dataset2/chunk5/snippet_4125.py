#Source: https://stackoverflow.com/questions/49259443/im-overlooking-something-typeerror-create-got-unexpected-keyword-argument
class ProjectManager(models.Manager):
    """"""
    def create(self, owner, project_name):
        project = super().create(owner=owner, project_name=project_name)
        project.save()

        System.objects.create(project=project, system_name="System initial name")

        return project

class Project(models.Model):
    objects = ProjectManager()

    owner           = models.ForeignKey('auth.User', related_name='projects', on_delete=models.CASCADE)
    project_name    = models.CharField(max_length=200)