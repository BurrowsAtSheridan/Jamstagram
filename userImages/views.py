from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import userImage
from django.contrib.auth.mixins import ( LoginRequiredMixin, UserPassesTestMixin )

class ImageListView(ListView):
  model = userImage
  template_name = 'image_list.html'

class ImageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = userImage
  fields = ('title', 'description', 'photo')
  template_name = 'image_edit.html'
  login_url = 'login'

  def test_func(self):
   obj = self.get_object()
   return obj.author == self.request.user


class ImageDetailView(DetailView):
  model = userImage
  template_name = 'image_detail.html'

class ImageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = userImage
  template_name = 'image_delete.html'
  success_url = reverse_lazy('image_list')
  login_url = 'login'
  def test_func(self):
    obj= self.get_object()
    return obj.author == self.request.user

class ImageCreateView(CreateView):
  model = userImage
  template_name = 'image_create.html'
  fields= ('title', 'description', 'photo')
  success_url = reverse_lazy('image_list')
  
  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)