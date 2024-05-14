#Source: https://stackoverflow.com/questions/76921332/attributeerror-strbatch-object-has-no-attribute-stores-as
from typing import Optional, Tuple, List, Mapping

def stores_as(self, data: 'HeteroData'):
    for node_type in data.node_types:
        self.get_node_store(node_type)
    for edge_type in data.edge_types:
        self.get_edge_store(*edge_type)
    return self

def collate(cls, data_list: List[BaseData], increment: bool = True, add_batch: bool = True, follow_batch: Optional[List[str]] = None, exclude_keys: Optional[List[str]] = None, ) -> Tuple[BaseData, Mapping, Mapping]:
# Collates a list of data objects into a single object of type cls.
# collate can handle both homogeneous and heterogeneous data objects by# individually collating all their stores.
# In addition, collate can handle nested data structures such as# dictionaries and lists.
    if not isinstance(data_list, (list, tuple)):
        # Materialize `data_list` to keep the `_parent` weakref alive.
        data_list = list(data_list)
    if cls != data_list[0].__class__:  # data_list[0]==>data_list
        out = cls(_base_cls=data_list[0].__class__)  # Dynamic inheritance.  data_list[0]==>data_list
    else:
        out = cls()
    # Create empty stores:
    out.stores_as(data_list[0])