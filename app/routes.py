from mvc_flask import Router

Router.get("/", "home#index")
Router.all("posts", only="show new create delete")
