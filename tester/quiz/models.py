from django.db import models
from django.contrib.auth.models import User



class Question(models.Model):
    question_text = models.CharField(max_length=255)
    question_number = models.IntegerField(default=1)

    def __str__(self):
        return f'Question{self.question_number}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    user_choice = models.IntegerField(default=0)

    def __str__(self):
        return f'Answer{self.question}'


#
# #
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#
#     def __str__(self):
#         return f'{self.user.username} Profile'
    # username = models.CharField(max_length=100)
    # password = models.CharField(max_length=50)
