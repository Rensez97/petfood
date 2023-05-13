from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, TemplateView
from .models import Product
from urllib.parse import urlencode
from django.db.models import Min, Max, Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math


class HomeView(ListView):
    model = Product
    template_name = 'website/home.html'
    extra_context = {
        'title': 'Dierenvoedingexpert | De Voordeligste Huisdierenvoeding Online '}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_items'] = self.get_queryset()
        context['products'] = Product.objects.all()
        context['uitgelicht'] = Product.objects.all().order_by(
            '-sale_price')[:12]
        context['products'] = Product.objects.all()
        favorites_indices_self = [
            [10, 50, 150, 2100, 3400, 4100, 65, 1800, 4200, 600, 1200, 3200],
            [20, 60, 160, 2110, 3410, 4110, 75, 1810, 4210, 610, 1210, 3210],
            [420, 460, 560, 2130, 3430, 4130, 495, 2210, 4230, 1010, 1230, 3230]
        ]

        for i, indices in enumerate(favorites_indices_self, start=1):
            favorites = [context['products'][index] for index in indices]
            context[f'favorites{i*12}'] = favorites
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-sale')
        return queryset[:4]


class AanbiedingView(ListView):
    model = Product
    template_name = 'website/aanbieding.html'
    extra_context = {
        'title': 'Beste Deals op Alle Dierenvoeding | Dierenvoedingexpert'}
    paginate_by = 36

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_products = Product.objects.filter(
            sale__gt=0)
        queryset = self.get_queryset().filter(
            sale__gt=0)
        context["count"] = queryset.count()
        context["max_pages"] = math.ceil(queryset.count()/self.paginate_by)
        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            product_list = paginator.page(page)
        except PageNotAnInteger:
            product_list = paginator.page(1)
        except EmptyPage:
            product_list = paginator.page(paginator.num_pages)
        context['products'] = product_list
        context['animals'] = all_products.values_list('animal', flat=True)\
            .distinct()
        context['brands'] = all_products.values_list(
            'brand', flat=True).distinct().order_by('brand')
        animal = self.request.GET.get('animal')
        if animal:
            context['animal'] = animal
        category = self.request.GET.get('category')
        if category:
            context['category'] = category
        brand = self.request.GET.get('brand')
        if brand:
            context['brand'] = brand
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filters = self.request.GET.dict()
        for filter_key, filter_value in filters.items():
            if filter_key == "page":
                continue
            if filter_key == "sort_by":
                print(filter_value)
                if filter_value == 'discount':
                    queryset = queryset.order_by('-sale')
                elif filter_value == 'low_price':
                    queryset = queryset.order_by('sale_price')
                elif filter_value == 'high_price':
                    queryset = queryset.order_by('-sale_price')
                elif filter_value == 'most_recent':
                    queryset = queryset.order_by('-date_added')
                else:
                    queryset = queryset.order_by('-date_added')
                continue
            queryset = queryset.filter(
                **{filter_key: filter_value})
        return queryset


class AnimalListView(ListView):
    model = Product
    template_name = ''
    extra_context = {}
    paginate_by = 36

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_animal_products = self.model.objects.filter(
            animal=self.animal).exclude(category='Apotheek')
        queryset = self.get_queryset().filter(
            animal=self.animal).exclude(category='Apotheek')
        print(queryset[:5])
        context["count"] = queryset.count()
        context["max_pages"] = math.ceil(queryset.count()/self.paginate_by)
        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page')
        query_params = self.request.GET.dict()
        for key, value in query_params.items():
            context[key] = value
        try:
            # Get the Page object for the current page number
            product_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            product_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            product_list = paginator.page(paginator.num_pages)
        context['products'] = product_list
        context['categorys'] = self.categorys
        context['age_groups'] = self.age_groups
        context['brands'] = all_animal_products.values_list(
            'brand', flat=True).distinct().order_by('brand')
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filters = self.request.GET.dict()
        for filter_key, filter_value in filters.items():
            if filter_key == "page":
                continue
            if filter_key == "sort_by":
                print(filter_value)
                if filter_value == 'discount':
                    queryset = queryset.order_by('-sale')
                elif filter_value == 'low_price':
                    queryset = queryset.order_by('sale_price')
                elif filter_value == 'high_price':
                    queryset = queryset.order_by('-sale_price')
                elif filter_value == 'most_recent':
                    queryset = queryset.order_by('-date_added')
                else:
                    queryset = queryset.order_by('-date_added')
                continue
            queryset = queryset.filter(
                **{filter_key: filter_value})
        return queryset


class HondListView(AnimalListView):
    animal = 'Hond'
    template_name = 'website/hond.html'
    extra_context = {
        'title': 'Hondenbrokken, natvoer en snacks | Dierenvoedingexpert'}
    categorys = ["Droogvoer", "Natvoer", "Diepvriesvoer", "Hondensnack"]
    age_groups = ["Puppy", "Junior", "Volwassen", "Senior", "Alle Leeftijden"]


class KatListView(AnimalListView):
    animal = 'Kat'
    template_name = 'website/kat.html'
    extra_context = {'title': 'Kat'}
    categorys = ["Droogvoer", "Natvoer", "Diepvriesvoer", "Kattensnack"]
    age_groups = ["Kitten", "Junior", "Volwassen",
                  "Senior", "Alle leeftijden", "Algemeen"]


class KnaagdierListView(AnimalListView):
    animal = 'Knaagdier'
    template_name = 'website/knaagdier.html'
    extra_context = {'title': 'Knaagdier'}
    categorys = []
    age_groups = ["Konijn", "Cavia", "Hamster", "Rat"]


class ApotheekListView(ListView):
    model = Product
    template_name = 'website/apotheek.html'
    extra_context = {'title': 'Apotheek'}
    paginate_by = 36

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_medicine_products = Product.objects.filter(
            category='Apotheek')
        queryset = self.get_queryset().filter(
            category='Apotheek')
        context["count"] = queryset.count()
        context["max_pages"] = math.ceil(queryset.count()/self.paginate_by)
        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            # Get the Page object for the current page number
            product_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            product_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            product_list = paginator.page(paginator.num_pages)
        context['products'] = product_list
        context['animals'] = all_medicine_products.values_list('animal', flat=True)\
            .distinct()
        context['age_groups'] = all_medicine_products.values_list(
            'age_group', flat=True).distinct()
        context['brands'] = all_medicine_products.values_list(
            'brand', flat=True).distinct().order_by('brand')
        animal = self.request.GET.get('animal')
        if animal:
            context['animal'] = animal
        age_group = self.request.GET.get('age_group')
        if age_group:
            context['age_group'] = age_group
        brand = self.request.GET.get('brand')
        if brand:
            context['brand'] = brand
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filters = self.request.GET.dict()
        for filter_key, filter_value in filters.items():
            if filter_key == "page":
                continue
            if filter_key == "sort_by":
                print(filter_value)
                if filter_value == 'discount':
                    queryset = queryset.order_by('-sale')
                elif filter_value == 'low_price':
                    queryset = queryset.order_by('sale_price')
                elif filter_value == 'high_price':
                    queryset = queryset.order_by('-sale_price')
                elif filter_value == 'most_recent':
                    queryset = queryset.order_by('-date_added')
                else:
                    queryset = queryset.order_by('-date_added')
                continue
            queryset = queryset.filter(
                **{filter_key: filter_value})
        return queryset


class OverOnsView(TemplateView):
    template_name = 'website/overons.html'
    extra_context = {'title': 'Over ons'}


class ZoekView(ListView):
    model = Product
    template_name = 'website/zoeken.html'
    # context_object_name = 'products'
    extra_context = {'title': 'Zoeken'}
    paginate_by = 36

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_term = self.request.GET.get('search2', '')
        all_search_products = Product.objects.filter(
            product_title__icontains=search_term)
        # context["products"] = all_search_products
        context["count"] = all_search_products.count()
        context["max_pages"] = math.ceil(
            all_search_products.count()/self.paginate_by)
        paginator = Paginator(all_search_products, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            # Get the Page object for the current page number
            product_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            product_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            product_list = paginator.page(paginator.num_pages)
        context['products'] = product_list
        return context


class ProductView(TemplateView):
    template_name = 'website/product.html'
    extra_context = {'title': 'Product'}
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = Product.objects.all()[0]
        return context
