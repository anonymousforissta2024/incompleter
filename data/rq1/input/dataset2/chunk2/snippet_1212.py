#Source: https://stackoverflow.com/questions/74706590/attributeerror-type-object-adminsignupform-has-no-attribute-as-view-why-is
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Admin(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    
    def __str__(self):
        return f'{self.user.username} Admin'
    
         
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    interests = models.ManyToManyField(Subject, related_name='interested_students')

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username