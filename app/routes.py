from mvc_flask import Router

Router.get("/", "home#index")

Router.get("/auth/login", "auth#login")
Router.post("/auth/logged", "auth#logged")

Router.get("/auth/register", "auth#register")
Router.post("/auth/registered", "auth#registered")

Router.all("posts", only="show new create delete")
