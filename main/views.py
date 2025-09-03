from django.shortcuts import render

def show_main(request):
    context = {
        'npm': '2406432236',
        'name': 'Shafa Aurelia Permata Basuki',
        'class': 'PBP C',
    }
    return render(request, "main.html", context)
