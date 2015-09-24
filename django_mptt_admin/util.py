import json
import six
import django
from django.forms.models import model_to_dict

def get_tree_from_queryset(queryset, on_create_node=None, max_level=None):
    """
    Return tree data that is suitable for jqTree.
    The queryset must be sorted by 'tree_id' and 'left' fields.
    """
    pk_attname = queryset.model._meta.pk.attname

    def serialize_id(pk):
        if isinstance(pk, six.integer_types + six.string_types):
            return pk
        else:
            # Nb. special case for uuid field
            return str(pk)

    # Result tree
    tree = []

    # Dict of all nodes; used for building the tree
    # - key is node id
    # - value is node info (label, id)
    node_dict = dict()

    # The lowest level of the tree; used for building the tree
    # - Initial value is None; set later
    # - For the whole tree this is 0, for a subtree this is higher
    min_level = None

    for instance in queryset:
        if min_level is None:
            min_level = instance.mptt_level

        pk = getattr(instance, pk_attname)
        # node_info = model_to_dict(instance, fields=['id',"user","parent","name","slug","points","phone","gender","level","mptt_level"])
        node_info = dict(
            label=six.text_type(instance),
            id=serialize_id(pk),
            title=instance.name,
            key=serialize_id(pk),
            email=instance.user.email,
            phone=instance.phone,
            gender=instance.gender,
            level=instance.level.title,
            user=instance.user.username,
        )
        if on_create_node:
            on_create_node(instance, node_info)

        if max_level is not None and not instance.is_leaf_node():
            # If there is a maximum level and this node has children, then initially set property 'load_on_demand' to true.
            node_info['load_on_demand'] = True

        if instance.mptt_level == min_level:
            # This is the lowest level. Skip finding a parent.
            # Add node to the tree
            tree.append(node_info)
        else:
            # NB: Use parent.pk instead of parent_id for consistent values for uuid
            parent_id = getattr(instance.parent, pk_attname)

            # Get parent from node dict
            parent_info = node_dict.get(parent_id)

            # Check for corner case: parent is deleted.
            if parent_info:
                if 'childCounter' not in parent_info:
                    parent_info['childCounter'] = 0

                # Add node to the tree
                # parent_info['children'].append(node_info)
                parent_info['childCounter'] +=1
                parent_info['folder'] = True
                parent_info['lazy'] = True

                # If there is a maximum level, then reset property 'load_on_demand' for parent
                if max_level is not None:
                    parent_info['load_on_demand'] = False

        # Update node dict
        node_dict[pk] = node_info

    return tree


def get_tree_queryset(model, node_id=None, max_level=None, include_root=True):
    if node_id:
        node = model.objects.get(pk=node_id)
        max_level = node.mptt_level + 2
        qs = node.get_descendants().filter(mptt_level__lte=max_level)
        print max_level
    else:
        qs = model._default_manager.filter(mptt_level__lte=max_level)
        max_level = 1
        qs = qs.filter(mptt_level__lte=max_level)

        if not include_root:
            qs = qs.exclude(mptt_level=0)

    return qs.filter(member_type=0).order_by('tree_id', 'lft')


def get_javascript_value(value):
    """
    Get javascript value for python value.

    >>> get_javascript_value(True)
    true
    >>> get_javascript_value(10)
    10
    """
    if isinstance(value, bool):
        if value:
            return 'true'
        else:
            return 'false'
    else:
        return json.dumps(value)


def get_short_django_version():
    """
    Get first two numbers of Django version.
    E.g. (1, 8)
    """
    return django.VERSION[0:2]


def get_model_name(model):
    """
    Get the name of a Django model

    >>> get_model_name(Country)
    country
    """
    return model._meta.model_name
