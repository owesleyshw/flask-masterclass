from app.model.post import Post

class HomeController:
    def index(self, view, request):
        posts = Post.query.filter_by(published=True).all()
        return view('home/index.html', posts=posts)