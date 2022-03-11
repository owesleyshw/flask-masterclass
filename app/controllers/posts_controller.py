from app.model.post import Post

class PostsController:
    def show(self, view, request, id):
        post = Post.query.get(id)
        return view('posts/show.html', post=post)