from app.ext import db
from app.form import PostForm
from app.model.post import Post
from flask import redirect, url_for
from flask_login import login_required


class PostsController:
    def show(self, view, request, id):
        post = Post.query.get(id)
        return view("posts/show.html", post=post)

    @login_required
    def new(self, view, request):
        form = PostForm()
        return view("posts/new.html", form=form)

    def create(self, view, request):
        form = PostForm()
        if form.validate_on_submit():
            published = True if form.publish else False
            post = Post(
                title=form.title.data,
                content=form.content.data,
                published=published,
                user_id=form.authors.data,
            )
            db.session.add(post)
            db.session.commit()

            return redirect(url_for("posts.show", id=post.id))

        return view("posts/new.html", form=form)

    def delete(self, view, request, id):
        post = Post.query.get(id)
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for("home.index"))
