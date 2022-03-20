from turtle import title
from django.shortcuts import render, get_object_or_404

from .models import VisaCategory, TypeOfSubVisa, SubVisa, VisaPageDescription, VisaDetailsDescription, UseFullQuestion, VisaTopSection


def visa(request):
    visa_top = VisaTopSection.objects.all().first()
    visa_cats = VisaCategory.objects.all()
    descriptions = VisaPageDescription.objects.all()
    context = {
        'visa_cats': visa_cats,
        'descriptions': descriptions,
        'visa_top': visa_top,
    }
    return render(request, 'visa.html', context)


def get_subvisa_meta(visa_slug):
    if visa_slug == "parent-visas":
        title = "Parent Visa to Australia Information | Visa Alliance"
        description = "Under this visa option, the parents’ of a settled Australian citizen, or an Australian permanent resident, or an eligible New Zealand citizen can visit Australia to live here."
    elif visa_slug == "student-graduate-training-visas":
        title = "Apply Student Visa for Australia | Visa Alliance"
        description = "Kick-start the journey to your dream of studying in Australia. Visa alliance helps you find the right course at the best universities in Australia and simplify your visa application."
    elif visa_slug == "temporary-work-skilled-migration-visas":
        title = "Temporary Work & Skilled Migration Visa to Australia | Visa Alliance"
        description = "Study, work and live in Australia. Our expert migration agents will help & guide you through various assessment tests, sponsorships, and skilled graduate visas."
    elif visa_slug == "global-talent-independent-gti-distinguished-talent-visas":
        title = "Global Talent Visa Australia  | FAQs | Visa Alliance"
        description = "The Global Talent visa (subclass 858) is a permanent visa for highly skilled and internationally recognized talents in specific fields. FAQs answered."
    elif visa_slug == "visitor-tourist-visas":
        title = "Visitor Visa to Australia | Tourist Visa Australia | Visa Alliance"
        description = "Tourists or visitors can enter Australia to visit their family or friends, for business or medical treatment purposes, or to spend a holiday via visitor visa."
    else:
        # partner-visa
        title = "Apply for Partner, Spouse or Fiancé Visa Australia | Visa Alliance"
        description = "Partner or spouse visa helps reunite immediate and extended family members with their eligible Australian relatives and spouses. You can apply for the temporary and permanent visa together."
    return title, description


def subvisa(request, visa_slug):
    visas = get_object_or_404(VisaCategory, slug=visa_slug)
    sub_visas = SubVisa.objects.all().filter(visa__slug=visa_slug)
    single_visas = TypeOfSubVisa.objects.all().filter(visa=visas)
    visa_description = VisaDetailsDescription.objects.get(visa__slug=visa_slug)

    existed = UseFullQuestion.objects.all().filter(visa=visas).exists()
    usefull = None
    if existed:
        usefull = UseFullQuestion.objects.all().filter(visa=visas)

    title, description = get_subvisa_meta(visa_slug)
    context = {
        'single_visas': single_visas,
        'visa_description': visa_description,
        'usefull': usefull,
        'existed': existed,
        'visas': visas,
        'meta_title': title,
        'meta_description': description
    }

    return render(request, 'visa_details.html', context)
