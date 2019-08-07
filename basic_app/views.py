from django.shortcuts import render
from basic_app.models import Movie_detail
from basic_app.serializers import MovieSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Q
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.http import HttpResponse
import json

def ajax_load_project(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        print(q)
        projects = Movie_detail.objects.filter(name__istartswith=q)[:5]
        results = []
        for project in projects:
            project_json = {}
            project_json['id'] = project.id
            project_json['value'] = project.name
            project_json['label'] = project.name
            results.append(project_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def searchProject(request):
    template = 'basic_app/testsearch.html'
    return render(request, template)

class MovieList(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'basic_app/testsearch.html'
    serializer_class = MovieSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter,)
    search_fields = ('name', )
    ordering_fields = ('rating', )

    def get(self, *args, **kwargs):
        query= self.request.GET.get('search','')
        print(query)
        queryset =Movie_detail.objects.filter(Q(name__icontains=query) | Q(titleid__icontains=query))
        return Response({'movie_context': queryset})
