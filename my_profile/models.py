from django.db import models



# Create your models here.

class ProfilePreference(models.Model):
    MARITAL_STATUS_CHOICES = {
        'N': 'N/A',
        'M': 'Married',
        'S': 'Single',
        'D': 'Divorced'
    }

    def marital_status_get(self):
        return self.MARITAL_STATUS_CHOICES.get(self.marital_status)

    EDUCATION_CHOICES = {
        'N': 'N/A',
        '1': 'Primary',
        '2': 'SSC',
        '3': 'HSC',
        '4': 'Graduation',
        '5': 'Post-graduation',
        '6': 'Doctorate',
        '0': 'Others'
    }

    def education_get(self):
        return self.EDUCATION_CHOICES.get(self.education)

    BODY_TYPE_CHOICES = {
        'N': 'N/A',
        'S': 'Slim',
        'F': 'Fat',
        'A': 'Average'
    }

    def body_type_get(self):
        return self.BODY_TYPE_CHOICES.get(self.body_type)

    SKIN_COLOR_CHOICES = {
        '1': ('Very Fair', '#f8ebdb'),
        '2': ('Fair', '#f3c6a5'),
        '3': ('Olive Brown', '#edb98a'),
        '4': ('Light Brown', '#cc8162'),
        '5': ('Brown', '#b06f51'),
        '6': ('Dark Brown', '#975b43'),
        '7': ('Black Brown', '#825035')
    }

    def skin_color_get(self):
        return self.SKIN_COLOR_CHOICES.get(self.skin_color)[0]

    def get_color_skin(self):
        return self.SKIN_COLOR_CHOICES.get(self.skin_color)[1]

    DIET_CHOICES = {
        'V': 'Vegetarian',
        'N': 'Non-vegetarian'
    }

    def diet_get(self):
        return self.DIET_CHOICES.get(self.diet)

    user = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    age_from = models.IntegerField(default= 0)
    age_to = models.IntegerField(default=100)
    religion = models.CharField(max_length=25, default='N/A')
    caste = models.CharField(max_length=25, default='N/A')
    sub_caste = models.CharField(max_length=25, default='N/A')
    country = models.CharField(max_length=50, default='India')
    state = models.CharField(max_length=50, default='N/A')
    marital_status = models.CharField(max_length=1, default='N')
    education = models.CharField(max_length=1, default='N')
    specialization = models.CharField(max_length=100, default='N/A')
    body_type = models.CharField(max_length=1, default='N')
    mother_tongue = models.CharField(max_length=50, default='N/A')
    height = models.IntegerField(default=0)
    skin_color = models.CharField(max_length=1, default='6')
    diet = models.CharField(max_length=1, default='N')
    occupation = models.CharField(max_length=200, default="N/A")
    about_my_partner = models.TextField(max_length=500, default='N/A')

    class Meta:
        db_table = 'ProfilePreference'



class Married(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    would_be =models.CharField(max_length= 50, default=" ")
    met_here = models.BooleanField(default=True)
    engagement_date =models.DateField(default='2019-05-05')
    marriage_date = models.DateField(default='2019-05-05')
    photo = models.ImageField(upload_to='our_marriage_photo/',default='/static/images/upload.png')

class Proposal(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    proposal_to = models.ForeignKey('UserProfile', on_delete=models.CASCADE,
                            related_name='proposal_to')
    contact_number = models.CharField(max_length=15, default=' ')
    whatsapp_number = models.CharField(max_length=15, default=' ')
    message = models.CharField(max_length=250, default=' ')
    requested_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Proposal'


class InterestedProfile(models.Model):
    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    interested_in = models.ForeignKey('UserProfile',
                                      on_delete=models.CASCADE,
                                      related_name='interested')
    requested_date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'InterestedProfile'


class ProfilePhoto(models.Model):
    MODIFICATION_CHOICES = {
        'O': 'No modification',
        'M': 'Mild touchup',
        'B': 'Camera beautification',
        'U': 'Studio photo (unmodified)',
        'S': 'Studio photo (modified)',
        'N': 'Modified using photo-editing software'
    }

    user = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    taken_on = models.DateField(auto_now=True)
    modification = models.CharField(max_length=1, default='B')
    photo = models.ImageField(upload_to='images/',
                              default='/static/images/upload.png')

    class Meta:
        db_table = 'ProfilePhoto'


class UserProfile(models.Model):
    GENDER_CHOICES = {
        'N': 'N/A',
        'M': 'Male',
        'F': 'Female'
    }

    def gender_get(self):
        return self.GENDER_CHOICES.get(self.gender)

    MARITAL_STATUS_CHOICES = {
        'N': 'N/A',
        'M': 'Married',
        'S': 'Single',
        'D': 'Divorced'
    }

    def marital_status_get(self):
        return self.MARITAL_STATUS_CHOICES.get(self.marital_status)

    EDUCATION_CHOICES = {
        'N': 'N/A',
        '1': 'Primary',
        '2': 'SSC',
        '3': 'HSC',
        '4': 'Graduation',
        '5': 'Post-graduation',
        '6': 'Doctorate',
        '0': 'Others'
    }

    def education_get(self):
        return self.EDUCATION_CHOICES.get(self.education)

    BODY_TYPE_CHOICES = {
        'N': 'N/A',
        'S': 'Slim',
        'F': 'Fat',
        'A': 'Average'
    }

    def body_type_get(self):
        return self.BODY_TYPE_CHOICES.get(self.body_type)

    DIFFERENTLY_ABLE_CHOICES = {
        'N': 'Not Applicable',
        'B': 'Blind',
        'D': 'Deaf',
        'U': 'Dumb',
        'M': 'Mobility disabilities',
        'P': 'Psychological disabilities'
    }

    def differently_able_get(self):
        return self.DIFFERENTLY_ABLE_CHOICES.get(self.differently_able)

    YES_NO_CHOICES = {
        'Y': 'Yes',
        'N': 'No'
    }

    def smoke_get(self):
        return self.YES_NO_CHOICES.get(self.smoke)

    def drink_get(self):
        return self.YES_NO_CHOICES.get(self.drinks)

    BLOOD_GROUP_CHOICES = {
        'N': 'N/A',
        'Ap': 'A +ve',
        'An': 'A -ve',
        'Bp': 'B +ve',
        'Bn': 'B -ve',
        'ABp': 'AB +ve',
        'ABn': 'AB -ve',
        'Op': 'O +ve',
        'On': 'O -ve'
    }

    def blood_group_get(self):
        return self.BLOOD_GROUP_CHOICES.get(self.blood_group)

    SKIN_COLOR_CHOICES = {
        '1': ('Very Fair', '#f8ebdb'),
        '2': ('Fair', '#f3c6a5'),
        '3': ('Olive Brown', '#edb98a'),
        '4': ('Light Brown', '#cc8162'),
        '5': ('Brown', '#b06f51'),
        '6': ('Dark Brown', '#975b43'),
        '7': ('Black Brown', '#825035')
    }

    def skin_color_get(self):
        return self.SKIN_COLOR_CHOICES.get(self.skin_color)[0]

    def get_color_skin(self):
        return self.SKIN_COLOR_CHOICES.get(self.skin_color)[1]

    DIET_CHOICES = {
        'V': 'Vegetarian',
        'N': 'Non-vegetarian'
    }

    def diet_get(self):
        return self.DIET_CHOICES.get(self.diet)

    photo = models.ForeignKey('ProfilePhoto', on_delete=models.SET_NULL,
                              null=True)
    user = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, default='N')
    date_of_birth = models.DateField(blank=True, default='2019-12-10')
    religion = models.CharField(max_length=25, default='N/A')
    caste = models.CharField(max_length=25, default='N/A')
    sub_caste = models.CharField(max_length=25, default='N/A')
    country = models.CharField(max_length=50, default='India')
    state = models.CharField(max_length=50, default='N/A')
    address = models.TextField(max_length=250, default=' ')
    age = models.IntegerField(default=0)
    marital_status = models.CharField(max_length=1, default='N')
    education = models.CharField(max_length=1, default='N')
    specialization = models.CharField(max_length=100, default='N/A')
    body_type = models.CharField(max_length=1, default='N')
    differently_able = models.CharField(max_length=1, default='N')
    drinks = models.CharField(max_length=1, default='N')
    smoke = models.CharField(max_length=1, default='N')
    mother_tongue = models.CharField(max_length=50, default='N/A')
    blood_group = models.CharField(max_length=3, default='N')
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    skin_color = models.CharField(max_length=1, default='6')
    diet = models.CharField(max_length=1, default='N')
    occupation = models.CharField(max_length=200, default="N/A")
    annual_income = models.IntegerField(default=0)
    fathers_occupation = models.CharField(max_length=200, default="N/A")
    mothers_occupation = models.CharField(max_length=200, default="N/A")
    no_sisters = models.IntegerField(default=0)
    no_brothers = models.IntegerField(default=0)
    about_me = models.TextField(max_length=500, default='N/A')

    @property
    def get_age(self):
        import datetime
        diff = datetime.date.today() - self.date_of_birth
        self.age = diff.days // 365
        self.save()
        return self.age

    class Meta:
        db_table = 'user_profile'
