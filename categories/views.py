from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models
from . import forms

class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    permission_required = 'categories.view_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_form'] = forms.CategoryForm()
        context['subcategory_form'] = forms.SubcategoryForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Category
    template_name = 'category_list.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')
    permission_required = 'categories.add_category'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        try:
            messages.success(self.request, 'Categoria adicionada com sucesso!')
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, 'Houve um erro ao tentar adicionar a categoria!')
            return super().form_invalid(form)

class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    template_name = 'category_list.html'
    success_url = reverse_lazy('category_list')
    permission_required = 'categories.change_category'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        try:
            messages.success(self.request, 'Categoria alterada com sucesso!')
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, 'Houve um erro ao tentar editar a categoria!')
            return super().form_invalid(form)

class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Category
    success_url = reverse_lazy('category_list')
    permission_required = 'categories.delete_category'

    def form_valid(self, form):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(self.request, 'Categoria excluída com sucesso!')
        except ProtectedError as e:
            messages.error(self.request, f"Não é possível excluir a categoria '{self.object.name}' porque ela está sendo referenciada por outros registros.")
        return redirect(self.success_url)


class SubcategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Subcategory
    template_name = 'category_list.html'
    context_object_name = 'subcategories'
    permission_required = 'subcategories.view_subcategory'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        context['category_form'] = forms.CategoryForm()
        context['subcategory_form'] = forms.SubcategoryForm()
        context['selected_category'] = models.Category.objects.get(id=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

class SubcategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Subcategory
    template_name = 'category_list.html'
    form_class = forms.SubcategoryForm
    success_url = reverse_lazy('category_list')
    permission_required = 'subcategories.add_subcategory'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class SubcategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Subcategory
    form_class = forms.SubcategoryForm
    template_name = 'category_list.html'
    success_url = reverse_lazy('category_list')
    permission_required = 'subcategories.change_subcategory'

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

class SubcategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Subcategory
    success_url = reverse_lazy('category_list')
    permission_required = 'subcategories.delete_subcategory'

    def form_valid(self, form):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(self.request, 'Subcategoria excluída com sucesso!')
        except ProtectedError as e:
            messages.error(self.request, f"Não é possível excluir a subcategoria '{self.object.name}' porque ela está sendo referenciada por outros registros.")
        return redirect(self.success_url)


def subcategories_by_category(request, category_id):
    subcategories = models.Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)
