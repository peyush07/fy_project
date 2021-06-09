# from _typeshed import OpenTextModeUpdating
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView
from .models import BD_fixedModel
from .forms import BD_fixedForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
import os
from json import dumps

class BD_fixedView1(CreateView):
    template_name = 'BD_fixed.html'
    def select_disaster(request):
        return render(request, 'BD_fixed.html')
            


class BD_fixedView2(TemplateView):
    template_name = 'bd2.html'
    def get_images(request):
        # path = "static/srwf"
        # # path = "http://127.0.0.1/output"
        # img_list = os.listdir(path)
        # img_list = ['srwf/'+i for i in img_list]
        # print(img_list)        
        # return render(request, 'bd1.html', {'img_list':img_list})
        disaster = request.GET['disasters']
        # if(disaster == 'srwf'):
        #     path1 = "static/srwf/pre"
        #     img_list1 = sorted(os.listdir(path1))
        #     img_list1 = ['srwf/pre/'+i for i in img_list1]
        #     path2 = "static/srwf/post"
        #     img_list2 = sorted(os.listdir(path2))
        #     img_list2 = ['srwf/post/'+i for i in img_list2]
        #     pair_list = zip(img_list1, img_list2)
        #     list1_JSON = dumps(img_list1)
        #     list2_JSON = dumps(img_list2)
        #     output_path = "static/srwf/output"
        #     output_list1 = sorted(os.listdir(output_path))
        #     output_list2 = ['srwf/output/'+i for i in output_list1]
        #     output_list1JSON = dumps(output_list1)
        #     output_list2JSON = dumps(output_list2)
        # elif(disaster == 'gvol'):
        #     path1 = "static/gvol/pre"
        #     img_list1 = sorted(os.listdir(path1))
        #     img_list1 = ['gvol/pre/'+i for i in img_list1]
        #     path2 = "static/gvol/post"
        #     img_list2 = sorted(os.listdir(path2))
        #     img_list2 = ['gvol/post/'+i for i in img_list2]
        #     pair_list = zip(img_list1, img_list2)
        #     list1_JSON = dumps(img_list1)
        #     list2_JSON = dumps(img_list2)
        #     output_path = "static/gvol/output"
        #     output_list1 = sorted(os.listdir(output_path))
        #     output_list2 = ['srwf/output/'+i for i in output_list1]
        #     output_list1JSON = dumps(output_list1)
        #     output_list2JSON = dumps(output_list2)
        if(disaster):
            path1 = "static/"+disaster+"/pre"
            img_list1 = sorted(os.listdir(path1))
            img_list1 = [disaster+'/pre/'+i for i in img_list1]
            path2 = "static/"+disaster+"/post"
            img_list2 = sorted(os.listdir(path2))
            img_list2 = [disaster+'/post/'+i for i in img_list2]
            pair_list = zip(img_list1, img_list2)
            list1_JSON = dumps(img_list1)
            list2_JSON = dumps(img_list2)
            output_path = "static/"+disaster+"/output"
            output_list1 = sorted(os.listdir(output_path))
            output_list2 = [disaster+'/output/'+i for i in output_list1]
            output_list1JSON = dumps(output_list1)
            output_list2JSON = dumps(output_list2)
        else:
            pair_list = []
            list1_JSON = ""
            list2_JSON = ""
            output_path = ""
        
        # if request.method == 'GET':
        #     post_image = request.POST.get('img2')
        #     print("This is ajax")
        #     print(post_image)
        #     return render(request, 'bd2.html', {'post_image': post_image})
        # else:
        #     print("not ajax")

        # img_listJSON = dumps(img_list)
        # disasterJSON = dumps(disaster)            
        return render(request, 'bd2.html', {'disaster': disaster, 'img_list': pair_list, 'list1_JSON': list1_JSON,
         'list2_JSON': list2_JSON, 'output_list1JSON': output_list1JSON, 'output_list2JSON': output_list2JSON})

    def getOutput(request):
        if request.method == 'POST':
            data = request.POST.get('img2')
            # run_script(post_image)
            print("This is ajax")
            # print(post_image)
            # print(request.body)
            print(data)
            return render(request, 'bd2.html', {'post_image': 123})
        else:
            print("not ajax")

class BD_fixedView3(TemplateView):
    template_name = 'temp.html'
    # def getOutput(request):   
    #     if request.method == 'GET':
    #         post_image = request.POST.get('img2')
    #         print("This is ajax")
    #         print(post_image)
    #         return render(request, 'bd2.html', {'post_image': post_image})
    #     else:
    #         print("not ajax")