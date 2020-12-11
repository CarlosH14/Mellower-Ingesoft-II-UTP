from django.http import request
from django.shortcuts import render
from predecir import predict

def vistaPrincipal (request):
    nombre_imagen=''
    res=''
    d=''
    answer=0
    if request.GET:
        nombre_imagen = request.GET.getlist('imagen')[0]
        answer=predict(nombre_imagen)
        if answer == 0:
          res="𝑳𝒂 𝒊𝒎𝒂𝒈𝒆𝒏 𝒑𝒓𝒆𝒅𝒆𝒄𝒊𝒅𝒂 𝒇𝒖𝒆: 𝙈𝙖𝙧𝙜𝙖𝙧𝙞𝙩𝙖"
        elif answer == 1:
          res="𝑳𝒂 𝒊𝒎𝒂𝒈𝒆𝒏 𝒑𝒓𝒆𝒅𝒆𝒄𝒊𝒅𝒂 𝒇𝒖𝒆: 𝘿𝙞𝙚𝙣𝙩𝙚 𝙙𝙚 𝙇𝙚𝙤𝙣"
        elif answer == 2:
          res="𝑳𝒂 𝒊𝒎𝒂𝒈𝒆𝒏 𝒑𝒓𝒆𝒅𝒆𝒄𝒊𝒅𝒂 𝒇𝒖𝒆: 𝙍𝙤𝙨𝙖"
        elif answer == 3:
          res="𝑳𝒂 𝒊𝒎𝒂𝒈𝒆𝒏 𝒑𝒓𝒆𝒅𝒆𝒄𝒊𝒅𝒂 𝒇𝒖𝒆: 𝙂𝙞𝙧𝙖𝙨𝙤𝙡"
        elif answer == 4:
          res="𝑳𝒂 𝒊𝒎𝒂𝒈𝒆𝒏 𝒑𝒓𝒆𝒅𝒆𝒄𝒊𝒅𝒂 𝒇𝒖𝒆: 𝙏𝙪𝙡𝙞𝙥𝙖𝙣"
    template_name='vistaPrincipal.html'
    return render(request, template_name, {"direccion_imagen":nombre_imagen, "Numero":answer,"Encontrada":res})
