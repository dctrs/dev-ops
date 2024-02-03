def paginate_queryset(queryset, page, page_size):
    start = (page - 1) * page_size
    end = page * page_size
    return queryset[start:end]