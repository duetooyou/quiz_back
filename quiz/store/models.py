from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=150,
                            verbose_name='Название')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return f'{self.name}'


class Question(models.Model):
    quiz = models.ForeignKey('Quiz',
                             on_delete=models.CASCADE,
                             related_name='questions',
                             verbose_name='Тест')
    content = models.TextField(verbose_name='Текст вопроса')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'{self.content}'


class Answer(models.Model):
    question = models.ForeignKey('Question',
                                 on_delete=models.CASCADE,
                                 related_name='answers',
                                 verbose_name='Вопрос')
    text = models.CharField(max_length=50,
                            verbose_name='Ответ')
    correct = models.BooleanField(default=False,
                                  verbose_name='Верно')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f'{self.question}'
