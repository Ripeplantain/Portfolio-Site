from django.forms import ModelForm
from base.models import Project,Comment

class ProjectForm(ModelForm):
    """This is the form to create and update a project"""
    class Meta:
        model = Project
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'

class CommentForm(ModelForm):
    """This is the form to create a comment"""
    class Meta:
        model = Comment
        fields = ['username', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for myField in self.fields:
            self.fields[myField].widget.attrs['class'] = 'form-control'