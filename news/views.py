from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from news.models import News
from django.urls import reverse
from news.forms import NewsForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
@login_required
def news_list(request):
    news = News.objects.filter(reporter=request.user)
    return render(request, "list_news.html", {"form": news})


def news_home(request):
    news = News.objects.all().order_by("-id")

    paginator = Paginator(news, per_page=4)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)
    return render(request, "newshome.html", {"form": page_obj})


def news_detail_view(request, newsid):
    news = get_object_or_404(News, id=newsid)
    return render(request, "news_detail.html", {"form": news})


@login_required
def news_add_view(request):
    form = NewsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        rep = form.save(commit=False)
        rep.reporter = request.user
        rep.save()
        return HttpResponseRedirect(reverse("news:news"))
    return render(
        request, "add_news.html", {"form": form}
    )  # the dictionary key is passed in form in html file


@login_required
def news_edit_view(request, newsid):
    news = get_object_or_404(News, id=newsid)
    # try:
    #     News.objects.get(id=newsid)
    # except News.DoesNotExist:
    #     raise Http404()  import HTTp404 first
    form = NewsForm(request.POST or None, request.FILES or None, instance=news)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("news:news"))

    return render(request, "add_news.html", {"form": form})


@login_required
def news_delete_view(request):
    newsid = request.POST.get("newsid")
    news = get_object_or_404(News, id=newsid)
    news.delete()
    return HttpResponseRedirect(reverse("news:news"))


def demo_for_ajax(request):
    data = {"name": "Ram", "address": "Kathmandu"}
    return JsonResponse(data, safe=False)


def search_view(request):
    if request.method == "POST":
        searchtext = request.POST["searchtext"]
        print(searchtext)
        searchresult = News.objects.filter(title__contains=searchtext)
        paginator = Paginator(searchresult, per_page=4)
        page_number = request.GET.get("page")
        try:
            page_obj = paginator.get_page(
                page_number
            )  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = paginator.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = paginator.page(paginator.num_pages)
        return render(
            request, "search.html", {"searchtext": searchtext, "form": page_obj}
        )
    else:
        return render(request, "search.html")
