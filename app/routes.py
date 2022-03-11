from mvc_flask import Router

Router.get('/', 'home#index') # Controller#action
Router.get('/posts/<int:id>', 'posts#show') # Controller#action