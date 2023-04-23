from .models import Category


def all_category(request):
    return {
      "categories" : Category.objects.all()
    }