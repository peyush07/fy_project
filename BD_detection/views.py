from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .forms import BD_ImageForm
from .models import BD_Image
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .BD_model import run_model
from .draw_polygons import draw_pol
from .save_to_static import save_to_static

# class BD_pageView(TemplateView):
#     template_name = 'BD_page.html'

# class BD_fixedView(TemplateView):
#     template_name = 'BD_fixed.html'

# Create your views here.
class BD_SelectImageView(TemplateView):
    template_name = 'BD_selectImage.html'
    def post(self, request, *args, **kwargs):
        form = BD_ImageForm(request.POST, request.FILES, use_required_attribute=False)
        if form.is_valid():
            obj = form.save()
            path1 = obj.pre_image.path
            path2 = obj.post_image.path
            run_model(path1, path2)

            img3 = draw_pol(path2)
            
            save_to_static(path1, path2, img3)      
            obj.output_image = "http://127.0.0.1/output/output_polygons.png"                
            obj.save()
            return HttpResponseRedirect(reverse_lazy('home:BD_output_display', kwargs={'pk': obj.id}))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



class BD_output(DetailView):
    model = BD_Image
    template_name = 'BD_output_display.html'
    context_object_name = 'bd'

