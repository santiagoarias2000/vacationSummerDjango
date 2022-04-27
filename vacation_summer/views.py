from django.shortcuts import render, redirect
from vacation_summer.models import Vacations


## view all site vacation
def list_sites_db(request):
    list = Vacations.objects.all()
    return render(request, 'index.html', {'site_vacation': list})


##save site vacation in data base
def save_site(request):
    _title = request.POST["title"]
    _description = request.POST["description"]
    _phone = request.POST["phone"]
    _web_url = request.POST["web_url"]
    _image = request.POST["image"]
    oneSite_Vacation = Vacations.objects.create(title=_title, description=_description, phone=_phone, web_url=_web_url,
                                                image=_image)
    return redirect("sites_vacations")


def form_go(request):
    return render(request, 'form.html')


def delete_data(request, id):
    vacation = Vacations.objects.get(id=id)
    if request.method == 'POST':
      vacation.delete()
      return redirect("sites_vacations")
    return render(request, {'sites_vacations': vacation})