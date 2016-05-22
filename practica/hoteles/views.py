
from django.shortcuts import render
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
from xmlparser import myContentHandler
import xml.etree.ElementTree as ET
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from models import Hotel,PagUser,HotelsUser,Image,Comment
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.shortcuts import render_to_response
import urllib2
from django.contrib import auth

mini=0;
maxi=10;


def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


def auth_view(request):
    username = request.POST.get("username", '')
    password = request.POST.get("password", '')
    user = auth.authenticate(username=username, password=password)


    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect('/')


def canalRSS(request):
    lista=Comment.objects.all()
    hotel=Hotel.objects.all()
    context={'lista':lista}
    return render_to_response('canalRSS.xml', context, context_instance = RequestContext(request), content_type='application/xml')

def more(request):
    respuesta=""
    global maxi
    global mini
    maxi+=10
    mini+=10
    lista=Comment.objects.all()
    listauser=PagUser.objects.all()
    context = {'lista':lista[mini:maxi],'user':request.user.username,'listausers':listauser,'condicion':""}
    if request.user.is_authenticated():
        us=PagUser.objects.get(user=request.user.username)
        context = {'lista':lista[mini:maxi],'user':request.user.username,'listausers':listauser,'condicion':"",'color':us.color,'size':us.size}
    return render_to_response('index.html', context, context_instance = RequestContext(request))

def init(request):

    respuesta=""
    salida=""
    numhoteles = Hotel.objects.count()
    lista=Comment.objects.all()
    listauser=PagUser.objects.all()

    if (numhoteles) == 0:
        print("Parsing....")
        theParser = make_parser()
        theHandler = myContentHandler()
        theParser.setContentHandler(theHandler)
        fil = urllib2.urlopen( 'http://cursosweb.github.io/etc/alojamientos_es.xml')
        theParser.parse(fil)

    context = {'lista':lista[0:10],'user':request.user.username,'listausers':listauser,'condicion':""}
    if request.user.is_authenticated():
        us=PagUser.objects.get(user=request.user.username)
        context = {'lista':lista[0:10],'user':request.user.username,'listausers':listauser,'condicion':"",'color':us.color,'size':us.size}

    return render_to_response('index.html', context, context_instance = RequestContext(request))

def show_aloj(request):
    lista=Hotel.objects.all()
    listauser=PagUser.objects.all()
    context = {'lista':lista,'user':request.user.username,'listausers':listauser,'condicion':""}
    if request.method =='POST':
        valuetype = request.POST.get('filtrotipo', "")
        valuestars=request.POST.get('filtrostars',"")
        if valuetype != "" and valuestars != "":
            lista=Hotel.objects.filter(tipo=valuetype,stars=valuestars)
        elif valuestars == "" and valuetype != "":
            lista=Hotel.objects.filter(tipo=valuetype)
        elif valuetype == "" and valuestars != "":
            lista=Hotel.objects.filter(stars=valuestars)
        context = {'lista':lista,'user':request.user.username,'listausers':listauser,'condicion':""}

    if request.user.is_authenticated():
        us=PagUser.objects.get(user=request.user.username)
        context = {'lista':lista,'user':request.user.username,'condicion':"",'color':us.color,'size':us.size,'listausers':listauser}

    return render_to_response('aloj.html', context, context_instance = RequestContext(request))


def show_aloj_id(request,id):
    lista=Hotel.objects.get(id=id)
    listimages=Image.objects.filter(hid=lista.id)
    listauser=PagUser.objects.all()
    listcoms=""
    hoteles=Hotel.objects.filter(id=id)
    listahoteles=Hotel.objects.all()

    if request.method == 'POST' and 'like' in request.POST :
        print lista.puntuacion
        lista.puntuacion = lista.puntuacion + 1
        h_megusta=Hotel(id=id,name=lista.name,url=lista.url,body=lista.body,
                        address=lista.address,source=lista.source,
                        stars=lista.stars,tipo=lista.tipo,puntuacion=lista.puntuacion)
        h_megusta.save()

    if request.method == 'POST' and 'quiero' in request.POST :
        print "aqui"
        h_us = HotelsUser(hotel=lista,user=request.user.username)
        h_us.save()
    if request.method =='POST' and 'comentario' in request.POST :
        value = request.POST.get('comentarios', "")
        if value !="":
            comment=Comment(hid=lista.id,com=lista,text=value)
            comment.save()




    listcoms=Comment.objects.filter(hid=lista.id)
    context = {'lista':listimages[0:5],'h':hoteles,'condicion':"",'url':lista.url,'name':lista.name, 'body':lista.body,
                'address':lista.address,'comentarios':listcoms,'type':lista.tipo,'stars':lista.stars, 'puntuacion':lista.puntuacion,
                'user':request.user.username,'listausers':listauser}
    if request.user.is_authenticated():
        us=PagUser.objects.get(user=request.user.username)
        context = {'lista':listimages[0:5],'h':hoteles,'condicion':"",'url':lista.url,'name':lista.name,
                    'address':lista.address,'comentarios':listcoms,'type':lista.tipo,'stars':lista.stars, 'body':lista.body,
                    'color':us.color,'size':us.size,'user':request.user.username,'listausers':listauser}

    return render_to_response('alojid.html', context,context_instance = RequestContext(request))

def show_aloj_id_frances(reuqest,id):
    fil = urllib2.urlopen( 'http://cursosweb.github.io/etc/alojamientos_fr.xml')
    tree = ET.parse(fil)
    root = tree.getroot()
    hotel=Hotel.objects.get(id=id)

    encontrado = False
    for child in root.iter('basicData'):
        name=child.find('name').text
        if name == hotel.name:
                print name
                encontrado=True;
                body=child.find('body').text
                phone=child.find('phone').text
                web=child.find('web').text
                if body == None:
                    body="Info no disponible"
                if phone == None:
                    phone= "Telefono no disponible"
                if web == None:
                    web= " Web no disponible"
                break;
    if not encontrado:
        return HttpResponse(" Hotel no disponible en este idioma")
    for child in root.iter('geoData'):
        address=child.find('address').text
        if address==hotel.address:
            country=child.find('country').text
            break;
    for child in root.iter('media'):
        url=child.find('url').text

        if url == hotel.source:
            break;
    if url == None:
        url= " imagen nos disponible"
    return HttpResponse("<h1>"+name+"</h1>"+body+phone+"<br>" +"<a href="+web+">"+web+"</a>"+"</br>"+address+"</br>"+country+"</br><img src="+url+"></img>")

def show_aloj_id_ingles(reuqest,id):
    encontrado=False;
    fil = urllib2.urlopen( 'http://cursosweb.github.io/etc/alojamientos_en.xml')
    tree = ET.parse(fil)
    root = tree.getroot()
    hotel=Hotel.objects.get(id=id)
    print hotel.name
    for child in root.iter('basicData'):
        name=child.find('name').text

        if name == hotel.name:
                encontrado=True;
                body=child.find('body').text
                phone=child.find('phone').text
                web=child.find('web').text
                if body == None:
                    body="Info no disponible"
                if phone == None:
                    phone= "Telefono no disponible"
                if web == None:
                    web= " Web no disponible"
                break;
    if not encontrado:
        return HttpResponse(" Hotel no disponible en este idioma")
    for child in root.iter('geoData'):
        address=child.find('address').text
        if address==hotel.address:
            country=child.find('country').text
            break;
    for child in root.iter('media'):
        url=child.find('url').text

        if url == hotel.source:
            print url
            break;

    return HttpResponse("<h1>"+name+"</h1>"+body+phone+"<br>" +"<a href="+web+">"+web+"</a>"+"</br>"+address+"</br>"+country+"</br><img src="+url+"></img>")



def usuario(request,usuario):
    value=""
    siz=""
    title=""
    us=PagUser.objects.get(user=usuario)
    listhotels=HotelsUser.objects.filter(user=usuario)
    listauser=PagUser.objects.all()

    if request.method =='POST':
        value = request.POST.get('css', "")
        siz= request.POST.get('size', "")
        title= request.POST.get('title', "")
        us=PagUser.objects.get(user=usuario)
        if value != "" :
            us.color=value;
        if siz != "":
            us.size=siz;
        if title != "":
            us.title=title;
    #us=PagUser.objects.get(user=usuario)
    us.save()

    value=us.color
    siz=us.size
    title=us.title
    print "value "+value
    context={'lista':listhotels[0:10],'color':value,'usuario':usuario,'size':siz,'title':title,
             'user':request.user.username,'listausers':listauser,'condicion':""}
    return render_to_response('usuario.html', context, context_instance = RequestContext(request))

def usuario_xml(request,usuario):
    us=PagUser.objects.get(user=usuario)
    listhotels=HotelsUser.objects.filter(user=us.user)
    listauser=PagUser.objects.all()
    context = {'h':listhotels,'us':us,'listauser':listauser}
    #f = open('templates/user_xml.xml', 'r')
    #xml=f.read()
    return render_to_response('user_xml.xml', context, context_instance = RequestContext(request), content_type='application/xml')

def xml_init(request):
    lista=Comment.objects.all()
    context ={'lista':lista}
    return render_to_response('init_xml.xml', context, context_instance = RequestContext(request), content_type='application/xml')
def about(request):
    lista=Hotel.objects.all()
    listauser=PagUser.objects.all()
    context={'listausers':listauser,'user':request.user.username}
    if request.user.is_authenticated():
        us=PagUser.objects.get(user=request.user.username)
        context={'listausers':listauser,'user':request.user.username,'color':us.color,'size':us.size}
    return render_to_response('about.html', context, context_instance = RequestContext(request))
