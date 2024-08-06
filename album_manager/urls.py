from django.urls import path
from . import views

app_name = "album_manager"
urlpatterns = [
    path("artist/", views.list_artist, name="list_artist"),
    path("artist/artist/<int:artist_id>/", views.artist, name="artist"),
    path("artist/add_artist/", views.add_artist, name="add_artist"),
    path("artist/edit_artist/<int:id>/", views.edit_artist, name="edit_artist"),
    path("artist/delete_artist/<int:id>/", views.delete_artist, name="delete_artist"),

    path("album/", views.list_album, name="list_album"),
    path("album/album/<int:album_id>/", views.album, name="album"),
    path("album/add_album/", views.add_album, name="add_album"),
    path("album/edit_album/<int:id>/", views.edit_album, name="edit_album"),
    path("album/delete_album/<int:id>/", views.delete_album, name="delete_album")

]