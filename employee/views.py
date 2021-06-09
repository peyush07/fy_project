
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from employee.forms import EmployeeForm#, CDForm
from .CD_model2 import find_change
from .CD_model3 import run_model3
# from .CD_model2 import function

class EmployeeImage(TemplateView):
    form = EmployeeForm
    template_name = 'emp_image.html'

    def post(self, request, *args, **kwargs):
        form = EmployeeForm(request.POST, request.FILES, use_required_attribute=False)
        if form.is_valid():
            obj = form.save()
            path1 = obj.image1.path
            path2 = obj.image2.path

            if(obj.select_model == "PcaKmeans"):
                obj.percentage_change = run_model3(path1, path2)                        
                obj.output_image = "http://127.0.0.1/output/Cleanchangemap.png"
                

            if(obj.select_model == "vgg19"):
                obj.percentage_change = find_change(path1, path2)                            
                obj.output_image = "http://127.0.0.1/output/changemap2.png"
                
            obj.save()
            return HttpResponseRedirect(reverse_lazy('home:emp_image_display', kwargs={'pk': obj.id}))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)



from django.views.generic import DetailView
from employee.models import Employee
# from .CD_model import find_PCAKmeans 

class EmpImageDisplay(DetailView):
    model = Employee
    template_name = 'emp_image_display.html'
    context_object_name = 'emp'


# # The view for analysing images
# def upload_view(request,pk=None):
#     ob = get_object_or_404(Patient,pk=pk)
#     if request.method == 'POST':
#         form = forms.EmployeeForm(request.POST,request.FILES)
#         if form.is_valid():
#             image = form.save
#             image.patient = patient

#             messages.success(request,"Image added successfully!")
#             return HttpResponseRedirect(reverse_lazy('emp_image_display', kwargs={'pk' : image.id}))