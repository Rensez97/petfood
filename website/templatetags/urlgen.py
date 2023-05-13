from django import template

register = template.Library()


@register.simple_tag
def urlstr(*args):
    filters = [arg for arg in args if arg != '']
    options = ["category", "animal", "age_group", "brand", "sort_by", "page"]
    newstr = ""
    for i, item in enumerate(filters):
        if i < len(filters) - 1:
            if filters[i+1] not in options:
                key = item
                value = filters[i+1]
                if not newstr:
                    newstr = f"?{key}={value}"
                else:
                    newstr = f"{newstr}&{key}={value}"
    return newstr
