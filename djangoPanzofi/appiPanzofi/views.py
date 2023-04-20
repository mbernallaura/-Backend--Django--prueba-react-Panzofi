from django.views import View
from django.http.response import JsonResponse
from .models import usuario, panzofi
from django.db.models import Q
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
class UsuarioView (View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def getUser(request, user='', password=''):
        usuarios = list(usuario.objects.filter(user=user).filter(password=password).values())
        if len(usuarios) > 0:
            respuesta= {
                'message':'Usuarios encontrados',
                'usuarios': usuarios[0]
            }
        else:
            respuesta= {
                'message':'Usuario o Contraseña incorrecta'
            }
        
        return JsonResponse(respuesta)  
    
    def getUsers(request):
        usuarios = list(usuario.objects.filter(~Q(cod_rol=1)).values())
        if len(usuarios) > 0:
            respuesta= {
                'message':'Usuarios encontrados',
                'usuarios': usuarios
            }
        else:
            respuesta= {
                'message':'Usuarios no encontrados'
            }
        return JsonResponse(respuesta) 
    
    def getPageNormal(request):
        pagina = list(panzofi.objects.values())
        if len(pagina) > 0:
            respuesta= {
                'message':'Vista encontrada',
                'usuarios': pagina[0]
            }
        else:
            respuesta= {
                'message':'Vista no encontrada'
            }
        
        return JsonResponse(respuesta) 
    
    @csrf_exempt

    def updateUser(request,id):
        jd= json.loads(request.body)
        personas = list(usuario.objects.filter(cod_id = id).values())

        if len(personas) > 0:
            persona = usuario.objects.get(cod_id = id)
            persona.date_session = jd['date_session']
            #persona.time_session = jd['time_session']
            persona.button1 = jd['button1']
            persona.button2 = jd['button2']
            persona.save()
            respuesta = {'message':'Usuario Actualizado'}
        else:
            respuesta = {'message':'Usuario no encontrado'}
        return JsonResponse(respuesta) 