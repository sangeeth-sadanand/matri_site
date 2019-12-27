from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from account.models import Notifications as ntf
from account.models import Account
from my_profile.models import UserProfile, ProfilePhoto, InterestedProfile, \
    Proposal, Married, ProfilePreference
from payment.views import paid_user

# Create your views here.
@login_required
def edit(request):
    a = UserProfile.objects.get(user=request.user)
    if request.method == "GET":
        print(a.date_of_birth)
        return render(request, 'my_profile/edit.djhtml', {'a': a})
    else:
        a.gender = request.POST.get('gender')
        a.date_of_birth = request.POST.get('dob')
        a.age = request.POST.get('age')
        a.religion = request.POST.get('religion')
        a.caste = request.POST.get('caste')
        a.sub_caste = request.POST.get('sub_caste')
        a.address = request.POST.get('address')
        a.country = request.POST.get('country')
        a.state = request.POST.get('state')
        a.education = request.POST.get('education')
        a.specialization = request.POST.get('specialization')
        a.occupation = request.POST.get('occupation')
        a.diet = request.POST.get('diet')
        a.body_type = request.POST.get('body_type')
        a.skin_color = request.POST.get('skin_color')
        a.drinks = request.POST.get('drinks')
        a.smoke = request.POST.get('smoke')
        a.differently_able = request.POST.get('differently_abled')
        a.blood_group = request.POST.get('blood_group')
        a.weight = request.POST.get('weight')
        a.height = request.POST.get('height')
        a.marital_status = request.POST.get('marital_status')
        a.mother_tongue = request.POST.get('mother_tongue')
        a.annual_income = request.POST.get('annual_income')
        a.fathers_occupation = request.POST.get('fathers_occupation')
        a.mothers_occupation = request.POST.get('mothers_occupation')
        a.no_sisters = request.POST.get('no_sisters')
        a.no_brothers = request.POST.get('no_brothers')
        a.about_me = request.POST.get('about_me')
        a.save()
        return redirect(show)


@login_required
def show(request):
    a = UserProfile.objects.get(user=request.user)
    p = ProfilePreference.objects.get_or_create(user=request.user)[0]
    return render(request, 'my_profile/show.djhtml', {'a': a, 'p': p})


@login_required
def upload_photo(request):
    if request.method == "GET":
        p = ProfilePhoto()
        return render(request, 'my_profile/upload_photo.djhtml', {'p': p})
    else:
        a = UserProfile.objects.get(user=request.user)
        p = ProfilePhoto()
        p.user = Account.objects.get(pk=a.pk)
        _, photo = request.FILES.popitem()
        print(photo)
        p.photo = photo[0]
        p.taken_on = request.POST.get('taken_on')
        p.modification = request.POST.get('modified')
        p.save()
        a.photo = p
        a.save()
        return redirect(show)


@login_required
def search(request):
    if request.method == 'GET':
        a = UserProfile.objects.get(user=request.user)
        a.religion = ''
        a.caste = ''
        a.sub_caste = ''
        a.mother_tongue = ''
        return render(request, 'my_profile/search.djhtml', {'a': a,
            'from': 0,
            'to': 100,
            'page_index': 1,
            'last_page': 1,
            'p': None})
    else:
        page_index = int(request.POST.get('page_index'))
        a = UserProfile()
        a.marital_status = request.POST.get('marital_status') or ''
        a.gender = request.POST.get('gender') or ''
        if a.gender == 'F':
            gender = 'M'
        else:
            gender = 'F'
        a.country = request.POST.get('country') or ''
        a.state = request.POST.get('state') or ''
        a.religion = request.POST.get('religion') or ''
        a.caste = request.POST.get('caste') or ''
        a.sub_caste = request.POST.get('sub_caste') or ''
        a.mother_tongue = request.POST.get('mother_tongue') or ''
        age_from = request.POST.get('from') or 0
        age_to = request.POST.get('to') or 100
        ps = UserProfile.objects.filter(gender__icontains=gender,
            marital_status__icontains=a.marital_status,
            country__icontains=a.country,
            state__icontains=a.state,
            religion__icontains=a.religion,
            caste__icontains=a.caste,
            sub_caste__icontains=a.sub_caste,
            mother_tongue__icontains=a.mother_tongue,
            age__range=(age_from, age_to))
        delta = 10
        length = len(ps)
        last_page = length // delta
        if page_index > last_page:
            page_index = last_page
        if page_index < 0:
            page_index = 0
        frm = page_index * delta
        if page_index == last_page:
            p = ps[frm:]
        else:
            p = ps[frm:frm + delta]
        for x in p:
            print(x.state)

        return render(request, 'my_profile/search.djhtml', {'a': a,
            'from': age_from,
            'to': age_to,
            'page_index': page_index,
            'last_page':
                range(last_page),
            'p': p})


@login_required
def interested_page(request):
    a = UserProfile.objects.get(user=request.user)
    p = InterestedProfile.objects.filter(user_profile=a)
    p = [x.interested_in for x in p]
    return render(request, 'my_profile/interested_profiles.djhtml', {'p': p})


@login_required
def interested_request(request):
    if request.method == "GET":
        if request.GET.get('interested_id'):
            try:
                interested_id = request.GET.get('interested_id')
                interested_user = UserProfile.objects.get(id=interested_id)
                this_profile = UserProfile.objects.get(user=request.user)
                f = InterestedProfile.objects.filter(user_profile=this_profile,
                    interested_in=interested_user)
                print(f)
                if len(f) == 0:
                    i = InterestedProfile()
                    i.user_profile = this_profile
                    i.interested_in = interested_user
                    i.save()
                    ntf.notify(i.interested_in.user, "Interest request",
                        f"{this_profile.user.get_full_name()} is interested in you", 'interested_me')
                    messages.success(request,
                        'Profile added to your interested '
                        'profile '
                        r'list ')
                    return redirect('interested_profiles')
                else:
                    messages.success(request,
                        'Profile already in your interested ' \
                        'profile list ')
                    return redirect('interested_profiles')
            except ObjectDoesNotExist:
                messages.success(request, 'Interested Profile not found')
                return redirect('interested_profiles')
        else:
            messages.success(request, 'Something went wrong')
            return redirect('interested_profiles')


@login_required
def intereseted_in_me(request):
    a = UserProfile.objects.get(user=request.user)
    p = InterestedProfile.objects.filter(interested_in=a)
    p = [x.user_profile for x in p]
    return render(request, 'my_profile/interested_in_me.djhtml', {'p': p})


@login_required
@paid_user
def view_profile_detail(request, id):
    try:
        a = UserProfile.objects.get(pk=id)
        u = UserProfile.objects.get(user=request.user)
        i = InterestedProfile.objects.filter(user_profile=a, interested_in=u)
        r = InterestedProfile.objects.filter(user_profile=u, interested_in=a)
        p = ProfilePreference.objects.get_or_create(user=a.user)[0]
        if len(i) == 1:
            if len(r) == 1:
                show_proposal = True
            else:
                show_proposal = False
            print(a.user.get_full_name())
            return render(request, 'my_profile/View_profile.djhtml', {'a': a,'p':p,
                'show_proposal': show_proposal})
        else:
            messages.error(request, 'Permission to view this profile denied')
    except ObjectDoesNotExist:
        messages.success(request, 'Profile not found')
        return redirect('interested_profiles')


@login_required
@paid_user
def proposal_request(request):
    if request.method == "GET":
        if request.GET.get('proposed_id'):
            try:
                proposal_id = request.GET.get('proposed_id')
                proposed_user = UserProfile.objects.get(id=proposal_id)
                this_profile = UserProfile.objects.get(user=request.user)
                f = Proposal.objects.filter(user_profile=this_profile,
                    proposal_to=proposed_user)
                if len(f) == 0:
                    p = Proposal()
                    p.user_profile = this_profile
                    p.proposal_to = proposed_user
                    p.save()
                else:
                    p = f[0]
                return render(request, 'my_profile/proposal_message.djhtml',
                    {'p': p})
            except ObjectDoesNotExist:
                messages.success(request, 'Profile not found')
                return redirect('interested_profiles')
        else:
            messages.success(request, 'Something went wrong')
            return redirect('interested_profiles')
    else:
        try:
            id = request.POST.get('id')
            p = Proposal.objects.get(id=id)
            p.contact_number = request.POST.get('contact')
            p.whatsapp_number = request.POST.get('whatsapp')
            p.message = request.POST.get('message')
            p.save()
            ntf.notify(p.proposal_to.user, "Proposed you",
                f"{p.user_profile.user.get_full_name()} proposed you.",
                'proposal_for_me')
            messages.success(request, 'Proposal sent')
            return redirect('interested_profiles')
        except Exception as e:
            messages.success(request, 'Something went wrong')
            return redirect('interested_profiles')


@login_required
@paid_user
def proposals_for_me(request):
    a = UserProfile.objects.get(user=request.user)
    p = Proposal.objects.filter(proposal_to=a)
    return render(request, 'my_profile/proposalforme.djhtml', {'p': p})

@login_required
@paid_user
def proposed_profiles(request):
    a = UserProfile.objects.get(user=request.user)
    p = Proposal.objects.filter(user_profile=a)
    return render(request, 'my_profile/proposed_profiles.djhtml', {'p': p})

@login_required
def we_are_getting_married(request):
    u = UserProfile.objects.get(user=request.user)
    m = Married.objects.get_or_create(user_profile=u)[0]
    if request.method == "GET":
        return render(request, 'my_profile/We_are_getting_married.djhtml',
            {'m': m})
    else:
        m.would_be = request.POST.get('name')
        m.met_here = request.POST.get('met_here')
        m.engagement_date = request.POST.get('eng_date')
        m.marriage_date = request.POST.get('mar_date')
        if len(request.FILES) != 0:
            _, photo = request.FILES.popitem()
            print(photo)
            m.photo = photo[0]
        u.marital_status = "M"
        u.save()
        m.save()
        messages.success(request, "Marital status changed")
        return redirect('profile_show')


@login_required
def edit_preference(request):
    p = ProfilePreference.objects.get_or_create(user=request.user)[0]
    if request.method == "GET":
        return render(request, 'my_profile/Profile_preference_edit.djhtml',
            {'p': p})
    else:
        p.age_from = request.POST.get('age_from')
        p.age_to = request.POST.get('age_to')
        p.religion = request.POST.get('religion')
        p.caste = request.POST.get('caste')
        p.sub_caste = request.POST.get('sub_caste')
        p.country = request.POST.get('country')
        p.state = request.POST.get('state')
        p.marital_status = request.POST.get('marital_status')
        p.education = request.POST.get('education')
        p.specialization = request.POST.get('specialization')
        p.body_type = request.POST.get('body_type')
        p.mother_tongue = request.POST.get('mother_tongue')
        p.height = request.POST.get('height')
        p.skin_color = request.POST.get('skin_color')
        p.diet = request.POST.get('diet')
        p.occupation = request.POST.get('occupation')
        p.about_my_partner = request.POST.get('about')
        p.save()
        messages.success(request, "Preference saved")
        return redirect('profile_show')



