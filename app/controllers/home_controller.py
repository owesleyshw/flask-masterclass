from app.model.post import Post

class HomeController:
    def index(self, view, request):
        posts = Post.query.all()
        return view('home/index.html', posts=posts)