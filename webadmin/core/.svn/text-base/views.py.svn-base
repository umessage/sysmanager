# -*- coding: utf8 -*-
from django.shortcuts import render, render_to_response
from django.contrib.auth.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from webadmin.core.models import *
from django import forms
from webadmin.core.forms import *
from django.template import RequestContext
from django.contrib.auth.forms import *
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

import fab,time

@login_required
def view_log(request, id):
    u_instance = Task.objects.get(id=id)

    return HttpResponse(u_instance.log.replace(r'\n','').replace(r',','<br>'))

@login_required
def add_proj(request):
    form = ProjForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ProjForm()
        return HttpResponseRedirect('/current_proj/')

    return render_to_response('Edit/ProjEdit.html', {'form' : form})

@login_required   
def edit_proj(request, id):
    try:
        u_instance = Proj.objects.get(id=id)
    except:
        return HttpResponse('此任务不存在')

    form = ProjForm(request.POST or None, instance = u_instance)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/current_proj/')

    return render_to_response('Edit/ProjEdit.html', locals())

@login_required
def del_proj(request, id):
    try:
        if id:
            Proj.objects.get(id=id).delete()
    except:
        return HttpResponse('此任务不存在')
    return HttpResponseRedirect('/current_proj/')

@login_required
def add_host(request):
    form = HostForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = HostForm()
        return HttpResponseRedirect('/host/')

    return render_to_response('Edit/ProjEdit.html', {'form' : form})

@login_required
def edit_host(request, id):
    try:
        u_instance = Host.objects.get(id=id)
    except:
        return HttpResponse('此主机不存在')

    form = HostForm(request.POST or None, instance = u_instance)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/host/')

    return render_to_response('Edit/ProjEdit.html', locals())

@login_required
def del_host(request, id):
    try:
        if id:
            Host.objects.get(id=id).delete()
    except:
        return HttpResponse('此主机不存在')
    return HttpResponseRedirect('/host/')

@login_required
def add_idc(request):
    form = IDCForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = IDCForm()
        return HttpResponseRedirect('/idc/')

    return render_to_response('Edit/ProjEdit.html', {'form' : form})

@login_required
def edit_idc(request, id):
    try:
        u_instance = IDC.objects.get(id=id)
    except:
        return HttpResponse('此机房不存在')

    form = IDCForm(request.POST or None, instance = u_instance)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/idc/')

    return render_to_response('Edit/ProjEdit.html', locals())

@login_required
def del_idc(request, id):
    try:
        if id:
            IDC.objects.get(id=id).delete()
    except:
        return HttpResponse('此机房不存在')
    return HttpResponseRedirect('/idc/')

@login_required
def add_ip(request):
    form = IPForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = IPForm()
        return HttpResponseRedirect('/ip/')

    return render_to_response('Edit/ProjEdit.html', {'form' : form})

@login_required
def edit_ip(request, id):
    try:
        u_instance = IP.objects.get(id=id)
    except:
        return HttpResponse('此地址不存在')

    form = IPForm(request.POST or None, instance = u_instance)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/ip/')

    return render_to_response('Edit/ProjEdit.html', locals())

@login_required
def del_ip(request, id):
    try:
        if id:
            IP.objects.get(id=id).delete()
    except:
        return HttpResponse('此机房不存在')
    return HttpResponseRedirect('/ip/')

@login_required
def add_user(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        form.save()
        format_data = form.cleaned_data
        id = User.objects.get(username=format_data['username']).id

    return render_to_response('Edit/ProjEdit.html', {'form' : form})

@login_required
def edit_user(request, id):
    u_instance = User.objects.get(id=id)

    form = UserChangeForm(request.POST or None, instance = u_instance)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/user/')
    
    return render_to_response('Edit/ProjEdit.html', locals())

@login_required
def del_user(request, id):
    try:
        if id:
            User.objects.get(id=id).delete()
    except:
        return HttpResponse('不能识别的任务ID')
    return HttpResponseRedirect('/user/')

@login_required
def change_password(request, id):
    u_instance = User.objects.get(id=id)
    is_super = User.objects.get(id=id).is_superuser

    if is_super:
        form = PasswordChangeForm(request.POST or None)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/')

    return render_to_response('Edit/ProjEdit.html', locals())

@login_required
def no_active(request,id):
    user = User.objects.get(id=id)

    if user:
        user.is_active = 0
        user.save()
        return HttpResponseRedirect('/user/')

    return render_to_response('Edit/ProjEdit.html', locals())

@login_required
def active(request,id):
    user = User.objects.get(id=id)

    if user:
        user.is_active = 1
        user.save()
        return HttpResponseRedirect('/user/')

    return render_to_response('Edit/ProjEdit.html', locals())

@login_required
def index(request):
    if request.path == '/':
        template_name = '_base.html'
        graphic = 1
        count = int(Proj.objects.order_by('-id')[0].id)
        return render_to_response(template_name, {'graphic' : graphic, 'count' : count})

@login_required
def modellist(request, model):
    template_name = 'List/%sList.html' % model.__name__
    ObjList = model.objects.all()
    UserPerm = request.user
    return render_to_response(template_name, {'ObjList' : ObjList, 'UserPerm' : UserPerm})


@login_required
def exec_proj(request):
    tmp_sproj = []
    tmp_sdeploy = []
    tmp_fproj = []
    tmp_fdeploy = []
    flag = ''
    
    proj_name = request.GET['Plist']
    deploy_name = request.GET['func']
    pversion = request.GET['version']

    timestrap = str(time.time()).split('.')[0]
    try:
        flag = Task.objects.filter(name=proj_name).order_by('-id')[0].flag
    except Task.DoesNotExist:
        Task.objects.create(name=proj_name,flag=1,timestrap=timestrap,version=pversion)
        tmp_sproj.append(proj_name)
        tmp_sdeploy.append(deploy_name)
    except IndexError:
        Task.objects.create(name=proj_name,flag=1,timestrap=timestrap,version=pversion)
        tmp_sproj.append(proj_name)
        tmp_sdeploy.append(deploy_name)
    if flag is None or flag == 0:
        Task.objects.create(name=proj_name,flag=1,timestrap=timestrap,version=pversion)
        tmp_sproj.append(proj_name)
        tmp_sdeploy.append(deploy_name)
    else:
        tmp_fproj.append(proj_name)
        tmp_fdeploy.append(deploy_name)

    if pversion == '':
        vflag = 0
        return HttpResponse(fab.run_task(tmp_sproj, tmp_sdeploy, request.user.username, flag=vflag))
    else:
        vflag = 1
        return HttpResponse(fab.run_task(tmp_sproj, tmp_sdeploy, request.user.username, pversion, vflag))
