# # model
# class CarCategory(models.Model):
#     name = models.CharField(max_length=255)
#     def __str__(self):
#         return self.name
# # model
# class Car(models.Model):
#     id = models.CharField(max_length=255)
#     driven = models.IntegerField()
#     price = models.IntegerField()

# # view
# def search(request):
#         if 'search_filter' in request.GET:
#             search_params = request.GET.dict()
#             search_params.pop("search_filter")
#             price_from = search_params['price_from']
#             price_to = search_params['price_to']
#             q_list = [Q(("{}__icontains".format(param), search_params[param])) for param in search_params 
#             if search_params[param] is not None]  

#             my_query = Car.objects.filter(reduce(operator.and_, q_list))
#             cars = [{
#                 'id': x.id,
#                 'driven': x.driven,
#                 'price': x.price,
#             } for x in my_query
#             ]
#             return JsonResponse({'data': cars})
#         context = {'cars': Car.objects.all().order_by('price')}
#         return render(request, 'cars/car_index.html', context)

# # error 
# # Object of type CarCategory is not JSON serializable

# "GET /cars/search_car/?search_filter=true&car_type=ford&price_from=0&price_to=10000search_filter=true HTTP/1.1" 200 12
# [<Q: (AND: ('car_type__icontains', 'ford'))>)>]



# class CarUpdateForm(ModelForm):
#     image = forms.CharField(required=True,
#                             widget=forms.TextInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = Car
#         exclude = ['id', 'created']
#         widgets = {
#             'number': widgets.NumberInput(attrs={'class': 'form-control'}),
#             'description': widgets.TextInput(attrs={'class': 'form-control'}),
#             'driven': widgets.NumberInput(attrs={'class': 'form-control'}),
#             'category': widgets.NumberInput(attrs={'class': 'form-control'}),
#             'price': widgets.NumberInput(attrs={'class': 'form-control'}),
#         }


# @login_required
# def update_car(request, id):
#     instance = get_object_or_404(Car, pk=id)
#     if request.method == 'POST':
#         form = CarUpdateForm(data=request.POST, instance=instance)
#         car_image = CarImage(image=request.POST['image'], car=instance)
#         if form.is_valid():
#             car_image.save()
#             edit.save()
#             return redirect('car_details', id=id)
#     else:
#         form = CarUpdateForm(instance=instance)
#     return render(request, 'car/update_car.html', {
#         'form': form,
#         'id': id
#     })


# {% if is_paginated %}
#     <div class="pagination h3">
#         {% if apartments.has_previous %}
#             <a class="btn btn-outline-info mb-4" href="?page=1">First</a>
#             <a class="btn btn-outline-info mb-4"
#                 href="?page={{ apartments.previous_page_number }}">Previous</a>
#         {% endif %}

#         {% for num in apartments.paginator.page_range %}
#             {% if apartments.number == num %}
#                 <a class="btn btn-info mb-4" href="?page={{ num }}">{{ num }}</a>
#             {% elif num > apartments.number|add:'-3' and num < apartments.number|add:'3' %}
#                 <a class="btn btn-outline-info mb-4" href="?page={{ num }}">{{ num }}</a>
#             {% endif %}
#         {% endfor %}

#         {% if apartments.has_next %}
#             <a class="btn btn-outline-info mb-4" href="?page={{ apartments.next_page_number }}">Next</a>
#             <a class="btn btn-outline-info mb-4"
#                 href="?page={{ apartments.paginator.num_pages }}">Last</a>
#         {% endif %}
#     </div>
# {% endif %}


# def index(request):
#     apartment_list = Apartment.objects.all().order_by('-created')
#     building_types = ApartmentCategory.objects.all()
#     zip_code = ZIP.objects.all()
#     paginator = Paginator(apartment_list, 4)
#     page = request.POST.get('page', 'Default')
#     apartments = paginator.get_page(page)
#     context = {'apartments': apartments, 'building_types': building_types, 'zip': zip_code}
#     return render(request, 'index/index.html', context)




# class CarListView(ListView):
#     model = Car
#     template_name = 'listings.html'
#     context_object_name = 'cars'
#     ordering = ['-created']
#     paginate_by = 5
#     limit = 10
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context)
#         paginator = context['paginator']
#         page_numbers_range = 10  # Display 5 page numbers
#         max_index = len(paginator.page_range)

#         page = self.request.GET.get('page')
#         print(self.request)
#         current_page = int(page) if page else 1

#         start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
#         end_index = start_index + page_numbers_range
#         if end_index >= max_index:
#             end_index = max_index

#         page_range = paginator.page_range[start_index:end_index]
#         # context['page_range'] = page_range
#         # return context
#         cars = Apartment.objects.all()[:self.limit]
#         car_types = CarType.objects.all()
#         context = {'cars': cars, 'car_types': car_types}
#         return context



# def get_car_by_id(request, id):
#     cars = Car.objects.all()
#     car_types = CarCategory.objects.all()
#     context = {'apartments': apartments, 'car_types': car_types,
#                'car': get_object_or_404(Car, pk=id)}
#     return render(
#         request, 'car/single_car.html', context
#     )