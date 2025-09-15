from django.urls import path

from .views import (
    CategoryListAPIView,
    CategoryCreateAPIView,
    CategoryUpdateAPIView,
    CategoryDeleteAPIView,
    CategoryDetailAPIView,
    RecipeCreateAPIView,
    RecipeDetailAPIView,
    RecipeListAPIView,
    RecipeUpdateAPIView,
    RecipeDeleteAPIView,

    CommentListAPIView,
    CommentCreateAPIView,
    CommentDetailAPIView,
    CommentUpdateAPIView,
    CommentDeleteAPIView,

    RatingCreateView,
    RecipeRatingListView,
)

urlpatterns = [
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("categories/create/", CategoryCreateAPIView.as_view(), name="category-create"),
    path("categories/<int:pk>/", CategoryDetailAPIView.as_view(), name="category-detail"),
    path("categories/<int:pk>/update/", CategoryUpdateAPIView.as_view(), name="category-update"),
    path("categories/<int:pk>/delete/", CategoryDeleteAPIView.as_view(), name="category-delete"),

    path("recipes/", RecipeListAPIView.as_view(), name="recipe-list"),
    path("recipes/create/", RecipeCreateAPIView.as_view(), name="recipe-create"),
    path("recipes/<int:pk>/", RecipeDetailAPIView.as_view(), name="recipe-detail"),
    path("recipes/<int:pk>/update/", RecipeUpdateAPIView.as_view(), name="recipe-update"),
    path("recipes/<int:pk>/delete/", RecipeDeleteAPIView.as_view(), name="recipe-delete"),

    path("recipes/<int:recipe_id>/comments/", CommentListAPIView.as_view(), name="comment-list"),
    path("recipes/<int:recipe_id>/comments/create/", CommentCreateAPIView.as_view(), name="comment-create"),
    path("comments/<int:pk>/", CommentDetailAPIView.as_view(), name="comment-detail"),
    path("comments/<int:pk>/update/", CommentUpdateAPIView.as_view(), name="comment-update"),
    path("comments/<int:pk>/delete/", CommentDeleteAPIView.as_view(), name="comment-delete"),

    path("recipes/<int:recipe_id>/ratings/", RecipeRatingListView.as_view(), name="recipe-ratings"),
    path("recipes/<int:recipe_id>/ratings/create/", RatingCreateView.as_view(), name="recipe-rating-create"),
]