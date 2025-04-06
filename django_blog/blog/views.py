from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm

# Create your views here.
def home(request):
    return render(request, 'blog/base.html')  # This is the home view function that renders the base.html template when the home page is accessed.
# print(os.path.exists('c:/Users/HP/Desktop/python mysql/learningdjango/Alx_DjangoLearnLab/django_blog/blog/templates/blog/base.html'))

def posts(request):
    return render(request, 'blog/posts.html')  # Render a template for blog posts

def login(request):
    return render(request, 'blog/login.html')  # Render a template for user login

def logout(request):
    return render(request, 'blog/logout.html')  # Render a template for user logout

def register(request):      
    if request.method == 'POST':        # Check if the request method is POST, which indicates that the user has submitted the registration form.
        form = UserRegisterForm(request.POST)
        if form.is_valid():        # Check if the form data is valid (e.g., all required fields are filled, and the data meets validation criteria).
            user = form.save()     # Save the form data to create a new user in the database.
            login(request, user)     # Log in the newly registered user automatically after successful registration.   
            return redirect('home')     # Redirect the user to the 'home' page after successful registration and login.
    else:
        form = UserRegisterForm()     # If the request method is not POST (e.g., GET), create an empty instance of the UserRegisterForm.

    # Render the 'register.html' template, passing the form instance to the template context.
    # This allows the template to display the registration form to the user.
    # The template can then use the form instance to render the form fields and handle any validation errors.    
    return render(request, 'blog/register.html', {'form': form}) # Render a template for user registration


from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm  # Simple built-in form
from django.contrib import messages  # Import messages for displaying success messages

@login_required  # Restrict access to logged-in users
def profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)  # Populate with current user
        if form.is_valid():
            form.save()  # Save updated info
            messages.success(request, 'Profile updated!')
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # Import CBVs
from .models import Post  # Import the Post model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # For permissions
from django.urls import reverse_lazy  # For redirection after delete

# Display all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']  # Show latest first

# Display post details
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):  # Automatically set author
        form.instance.author = self.request.user
        return super().form_valid(form)

# Edit a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # Restrict to author
        post = self.get_object()
        return self.request.user == post.author

# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm

@login_required  # Ensure user is logged in
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Get the post object
    if request.method == "POST":
        form = CommentForm(request.POST)  # Bind form to POST data
        if form.is_valid():
            comment = form.save(commit=False)  # Don't save to DB yet
            comment.author = request.user  # Assign current user
            comment.post = post  # Link to post
            comment.save()  # Save to database
            return redirect('post-detail', pk=post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})

class EditCommentView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class DeleteCommentView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

from django.db.models import Q

class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()


# from taggit.models import Tag

class TaggedPostListView(ListView):
    model = Post
    template_name = 'blog/posts_by_tag.html'

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))
