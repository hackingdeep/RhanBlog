from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,UpdateView,DeleteView
from .forms import PostCreateForms
from .models import Post
from django.urls import reverse_lazy

class BlogListView(View):
    def get(self,request,*args,**kwargs):
        post = Post.objects.all()
        context = {
            'posts':post
        }
        return render(request,'blog_list.html',context)
    

class BlogCreate(View):

    def get(self,request,*args,**kwargs):
        forms = PostCreateForms()

        context = {
            'forms':forms
        }
        return render(request,'blog_create.html',context)
    

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            forms = PostCreateForms(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect('blog:home') 
        else:
            forms = PostCreateForms()

        context = {
            
        }
        return render(request,'blog_create.html',context)


class BlogDetailView(View):
    def get(self,request,pk,*args,**kwargs):
        post = get_object_or_404(Post,pk=pk)

        context = {
            'post':post
        }
        return render(request,'blog_detail.html',context)
    

class BlogUpdate(UpdateView):
       model=Post
       fields=['title','content']
       template_name='blog_update.html'


       def get_success_url(self):
           pk = self.kwargs['pk']
           return reverse_lazy('blog:blog_detail',kwargs={'pk':pk})
       

class DeleteBlog(DeleteView):
    model = Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog:home')
