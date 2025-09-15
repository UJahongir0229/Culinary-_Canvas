from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


# Create your models here.
class Recipe(BaseModel):
    title = models.CharField(max_length=250, verbose_name=_("Recipe Title"))
    slug = models.SlugField(unique_for_date="published_at", verbose_name=_("Slug"))

    author = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="recipes",
        verbose_name=_("Author")
    )
    category = models.ForeignKey(
        "recipes.Category",
        on_delete=models.SET_NULL,
        related_name="recipes",
        null=True,
        blank=True,
        verbose_name=_("Recipe Category")
    )

    description = models.TextField(verbose_name=_("Description"))
    ingredients = models.TextField(verbose_name=_("Ingredients"))
    instructions = models.TextField(verbose_name=_("Instructions"))
    image = models.ImageField(upload_to="recipes/", verbose_name=_("Recipe Image"))

    is_draft = models.BooleanField(default=True, verbose_name=_("Is Draft"))

    class Meta:
        verbose_name = _("Recipe")
        verbose_name_plural = _("Recipes")

    def __str__(self):
        return self.title


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Category Name"))
    slug = models.SlugField(verbose_name=_("Slug"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Comment(BaseModel):
    content = models.TextField(verbose_name=_("Comment Content"))

    recipe = models.ForeignKey(
        "recipes.Recipe",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Recipe")
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Comment Author")
    )

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="replies",
        verbose_name=_("Parent Comment")
    )

    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return f"Comment by {self.user} on {self.recipe.title[:20]}"


class Rating(BaseModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="ratings",
        verbose_name=_("User")
    )
    recipe = models.ForeignKey(
        "recipes.Recipe",
        on_delete=models.CASCADE,
        related_name="ratings",
        verbose_name=_("Recipe")
    )

    score = models.PositiveSmallIntegerField(  # ⭐ baho (1–5)
        choices=[(i, str(i)) for i in range(1, 6)],
        verbose_name=_("Score")
    )
    review = models.TextField(blank=True, null=True, verbose_name=_("Review"))

    class Meta:
        unique_together = ("user", "recipe")
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")

    def __str__(self):
        return f"{self.user} - {self.recipe} ({self.score})"
