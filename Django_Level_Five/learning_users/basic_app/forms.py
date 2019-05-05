from django import forms
from basic_app.models import Person


percentage = (
    ('ns', 'not satisfied'),
    ('ss', 'somewhat satisfied'),
    ('n', 'neutral'),
    ('g', 'good'),
    ('e','excellent'),
)



class PersonForm(forms.ModelForm):
    name = forms.CharField(max_length=60,widget=forms.TextInput(
    attrs={
    'class' : 'form-control',
    'placeholder' : 'ENTER YOUR FULL NAME ...'
    }
    ))
    question_1 = forms.ChoiceField(label='The Group’s /Project’s goal and objectives are clear to me.',choices=percentage, widget=forms.RadioSelect)
    question_2 = forms.ChoiceField(label='Roles and Responsibilities within the group are understood.',choices=percentage, widget=forms.RadioSelect)
    question_3 = forms.ChoiceField(label='Clear Reporting Structures have been established.',choices=percentage, widget=forms.RadioSelect)
    question_4 = forms.ChoiceField(label='I have resources to perform my job effectively.',choices=percentage, widget=forms.RadioSelect)
    question_5 = forms.ChoiceField(label='My work environment is stressful',choices=percentage, widget=forms.RadioSelect)
    question_6 = forms.ChoiceField(label='My team members are giving need based support to perform my role effectively.',choices=percentage, widget=forms.RadioSelect)
    question_7 = forms.ChoiceField(label='My work in team is appreciated and recognized.',choices=percentage, widget=forms.RadioSelect)
    question_8 = forms.ChoiceField(label='Innovation/ new ways of doing things are liked by all team members.',choices=percentage, widget=forms.RadioSelect)
    question_9 = forms.ChoiceField(label='I can communicate effectively regarding my work with senior management.',choices=percentage, widget=forms.RadioSelect)
    question_10 = forms.ChoiceField(label='Management has good understanding of what is going in our group team.',choices=percentage, widget=forms.RadioSelect)
    question_11 = forms.ChoiceField(label='I find my job challenging.',choices=percentage, widget=forms.RadioSelect)
    question_12 = forms.ChoiceField(label='I can handle the size of my workload.',choices=percentage, widget=forms.RadioSelect)
    question_13 = forms.ChoiceField(label='My organization helps me to enhance my career development.',choices=percentage, widget=forms.RadioSelect)
    question_14 = forms.ChoiceField(label='I am willing to put extra efforts when necessary to complete the assigned job.',choices=percentage, widget=forms.RadioSelect)
    question_15 = forms.ChoiceField(label='I am proud to say that I am part of TBRL family.',choices=percentage, widget=forms.RadioSelect)
    question_16= forms.ChoiceField(label='I have got adequate information regarding my compensation and benefits.',choices=percentage, widget=forms.RadioSelect)
    question_17 = forms.ChoiceField(label='Reimbursement of TA, DA etc. by Accounts section is timely.',choices=percentage, widget=forms.RadioSelect)
    question_18 = forms.ChoiceField(label='Performance appraisal system is effectively conducted by our organization.',choices=percentage, widget=forms.RadioSelect)
    question_19= forms.ChoiceField(label='I received a proper induction/ orientation while joining TBRL.',choices=percentage, widget=forms.RadioSelect)
    question_20 = forms.ChoiceField(label='Management seeks the involvement of employees’ opinion when making important decisions.	',choices=percentage, widget=forms.RadioSelect)
    question_21 = forms.ChoiceField(label='The tools and technologies that I use help me to be efficient in completing my work.',choices=percentage, widget=forms.RadioSelect)

    question_22 = forms.ChoiceField(label='Our technology is reliable and works when we need it to work.',choices=percentage, widget=forms.RadioSelect)

    question_23 = forms.ChoiceField(label='Do you think the hygiene of mess is maintained properly.',choices=percentage, widget=forms.RadioSelect)

    question_24 = forms.ChoiceField(label='Are you satisfied with the facilities at MI room.',choices=percentage, widget=forms.RadioSelect)

    question_25 = forms.ChoiceField(label='Is hygiene and cleanliness maintained regularly.',choices=percentage, widget=forms.RadioSelect)
    question_26 = forms.ChoiceField(label='Are you stisfied with the security services. 	',choices=percentage, widget=forms.RadioSelect)
    question_27 = forms.ChoiceField(label='Do you believe that awareds/rewards are distributed to the employees on a fair basis.',choices=percentage, widget=forms.RadioSelect)
    question_28 = forms.ChoiceField(label='How helpful does the organized trainings helpful to you.',choices=percentage, widget=forms.RadioSelect)
    question_29 = forms.ChoiceField(label='Do you feel your senior maintains a good level of transparency with you and your team ',choices=percentage, widget=forms.RadioSelect)
    question_30 = forms.ChoiceField(label='Do you need access to HR employees for advice and assistance.',choices=percentage, widget=forms.RadioSelect)
    question_31 = forms.ChoiceField(label='Do you find the survey useful.',choices=percentage, widget=forms.RadioSelect)


    class Meta:

        model=Person
        fields=("__all__")
