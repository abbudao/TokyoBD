from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import Context
from Main.forms import HabilitadoForm
import cx_Oracle
import re
# Create your views here.
def pdf2go(request):
    #Retrieve data or whatever you need
    return render_to_pdf(
            'Main/partida.html',
            {
                'pagesize':'A4',
                'mylist': results,
            }
        )
def index(request):
    template = loader.get_template('Main/index.html')
    context={}
    return HttpResponse(template.render(context,request))

def arbitra_see(request):
    ip='grad.icmc.usp.br'
    port= 15215
    SID='orcl'
    dsn_tns= cx_Oracle.makedsn(ip, port, SID)
    con= cx_Oracle.connect('8058718','a',dsn_tns) 
    cur= con.cursor()
    cur.execute('select HabilitadoArbitrar.NumeroId,Nome,Esporte from HabilitadoArbitrar join Arbitro on HabilitadoArbitrar.NumeroId= Arbitro.NumeroId order by Nome')
    data=[]
    for a in cur:
        datatem=[]
        datatem.append(a[0])
        datatem.append(a[1])
        datatem.append(a[2])
        data.append(datatem)
    template = loader.get_template('Main/consulta.html')
    context ={'data': data}
    return HttpResponse(template.render(context,request))

def arbitra_altera(request):
    try:
        ip='grad.icmc.usp.br'
        port= 15215
        SID='orcl'
        dsn_tns= cx_Oracle.makedsn(ip, port, SID)
        con= cx_Oracle.connect('8058718','a',dsn_tns) 
        cur= con.cursor()
        if request.method =='GET' :
            form= HabilitadoForm()
        else: 
            form = HabilitadoForm(request.POST)
            if form.is_valid():
                context ={'form':form,} 
                aux=form.cleaned_data
                aux_codigo=str(aux['codigo'])
                aux_esporte=((aux['esporte']))
                aux_esporte= re.sub('[\"]','[\']',aux_esporte)
                statement='insert into HabilitadoArbitrar(NumeroId,Esporte) values ('+ aux_codigo +','+'\''+aux_esporte+'\''+')'
                cur.execute(statement)
                con.commit()

        cur.execute('select HabilitadoArbitrar.NumeroId,Nome,Esporte from HabilitadoArbitrar join Arbitro on HabilitadoArbitrar.NumeroId= Arbitro.NumeroId order by Nome')
        data=[]
        for a in cur:
            datatem=[]
            datatem.append(a[0])
            datatem.append(a[1])
            datatem.append(a[2])
            data.append(datatem)
    
    except(RuntimeError, TypeError, NameError):
        pass
    template = loader.get_template('Main/altera.html')
    context ={'form':form,'data':data,}
    return HttpResponse(template.render(context,request))
def partida(request):
    return HttpResponse()

def arbitra_remove(request):
    ip='grad.icmc.usp.br'
    port= 15215
    SID='orcl'
    dsn_tns= cx_Oracle.makedsn(ip, port, SID)
    con= cx_Oracle.connect('8058718','a',dsn_tns) 
    cur= con.cursor()
    if request.method =='GET' :
        form= HabilitadoForm()
    else: 
        form = HabilitadoForm(request.POST)
        if form.is_valid():
            context ={'form':form,} 
            aux=form.cleaned_data
            aux_codigo=str(aux['codigo'])
            aux_esporte=((aux['esporte']))
            aux_esporte= re.sub('[\"]','[\']',aux_esporte)
            statement='delete from HabilitadoArbitrar where NumeroId='+aux_codigo+'and Esporte='+'\''+aux_esporte+'\''
            cur.execute(statement)
            con.commit()

    cur.execute('select HabilitadoArbitrar.NumeroId,Nome,Esporte from HabilitadoArbitrar join Arbitro on HabilitadoArbitrar.NumeroId= Arbitro.NumeroId order by Nome')
    data=[]
    for a in cur:
        datatem=[]
        datatem.append(a[0])
        datatem.append(a[1])
        datatem.append(a[2])
        data.append(datatem)
    template = loader.get_template('Main/remove.html')
    context ={'form':form,'data':data,}
    return HttpResponse(template.render(context,request))
def partida(request):
    ip='grad.icmc.usp.br'
    port= 15215
    SID='orcl'
    dsn_tns= cx_Oracle.makedsn(ip, port, SID)
    con= cx_Oracle.connect('8058718','a',dsn_tns) 
    cur= con.cursor()
    cur.execute(' SELECT DISTINCT ATLETA.NOME,COUNT(*) FROM ATLETA JOIN ATLETAPARTICIPA ON ATLETA.NUMEROID=ATLETAPARTICIPA.NUMEROID JOIN EQUIPEJOGA ON EQUIPEJOGA.NUMEROEQUIPE = ATLETAPARTICIPA.NUMERO GROUP BY ATLETA.NOME HAVING COUNT(*)>3 ')
    data=[]
    for a in cur:
        datatem=[]
        datatem.append(a[0])
        datatem.append(a[1])
        data.append(datatem)
    template = loader.get_template('Main/partida.html')
    print(con.version)
    context ={'data': data}
    return HttpResponse(template.render(context,request))
