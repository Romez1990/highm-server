from django.urls import path
from rest_framework.routers import Route, DynamicRoute, SimpleRouter


class CustomLookupTypeRouter(SimpleRouter):
    routes = [
        Route(
            url='{prefix}{trailing_slash}',
            mapping={
                'get': 'list',
                'post': 'create'
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        DynamicRoute(
            url='{prefix}/{url_path}{trailing_slash}',
            name='{basename}-{url_name}',
            detail=False,
            initkwargs={}
        ),
        Route(
            url='{prefix}/{lookup}{trailing_slash}',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Instance'}
        ),
        DynamicRoute(
            url='{prefix}/{lookup}/{url_path}{trailing_slash}',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        ),
    ]

    def get_urls(self):
        ret = []

        for prefix, viewset, basename in self.registry:
            if hasattr(viewset, 'lookup_value_regex'):
                raise ValueError(
                    'lookup_value_regex is not supported in IntPkRouter')

            lookup_field = getattr(viewset, 'lookup_field', 'pk')
            lookup_type = getattr(viewset, 'lookup_type', 'str')
            lookup = f'<{lookup_type}:{lookup_field}>'
            routes = self.get_routes(viewset)

            for route in routes:
                mapping = self.get_method_map(viewset, route.mapping)
                if not mapping:
                    continue

                url = route.url.format(
                    prefix=prefix,
                    lookup=lookup,
                    trailing_slash=self.trailing_slash
                )

                initkwargs = route.initkwargs.copy()
                initkwargs.update({
                    'basename': basename,
                    'detail': route.detail,
                })

                view = viewset.as_view(mapping, **initkwargs)
                name = route.name.format(basename=basename)
                ret.append(path(url, view, name=name))

        return ret
