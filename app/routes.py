from mvc_flask import Router

Router.get("/", "home#index")
Router.get("/auth/register", "auth#register")
Router.all("posts", only="show new create delete")
