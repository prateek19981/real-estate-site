from django.shortcuts import get_object_or_404,render

# Create your views here.
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from listings.models import Listing

def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
    
    paginator=Paginator(listings,3)
    page=request.GET.get('page')
    paged_listing=paginator.get_page(page)
    context={"listings":paged_listing}

    return render(request,'listing/listings.html',context)







def listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)
    context={"listing":listing}
    return render(request,'listing/listing.html',context)



def search(request):
    query_set=Listing.objects.order_by('-list_date')
    #keywords
    if 'keywords' in request.GET:
        keyword=request.GET['keywords']
        if keyword:
            query_set=query_set.filter(description__icontains=keyword)


    #city
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            query_set=query_set.filter(city__iexact=city)


    #state
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            query_set=query_set.filter(state__iexact=state)

    #bedrooms

    if 'bedrooms' in request.GET:
        bedroom=request.GET['bedrooms']
        if bedroom:
            query_set=query_set.filter(bedrooms__lte=bedroom)

    #price
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            query_set=query_set.filter(price__lte=price)




    context={ "listings":query_set,
              "value":request.GET

    }
    return render(request,'listing/search.html',context)