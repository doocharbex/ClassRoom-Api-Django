from django.views.generic import TemplateView
from class_room.settings import ALLOWED_HOSTS
from .models import DocumentApiModel

# <--- Show And Post Data in Template 'index.html' ---->
class HomeView(TemplateView):
    template_name = 'home_app/index.html'

    def get(self, request, *args, **kwargs):

        getDataDocumentApiModel = DocumentApiModel.objects.all()


        response = self.render_to_response({
            'documentApi': getDataDocumentApiModel
        })

        return response
