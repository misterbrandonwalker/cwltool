# Stubs for networkx.drawing.nx_pylab (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def draw(G, pos: Optional[Any] = ..., ax: Optional[Any] = ..., **kwds): ...
def draw_networkx(
    G, pos: Optional[Any] = ..., arrows: bool = ..., with_labels: bool = ..., **kwds
): ...
def draw_networkx_nodes(
    G,
    pos,
    nodelist: Optional[Any] = ...,
    node_size: int = ...,
    node_color: str = ...,
    node_shape: str = ...,
    alpha: float = ...,
    cmap: Optional[Any] = ...,
    vmin: Optional[Any] = ...,
    vmax: Optional[Any] = ...,
    ax: Optional[Any] = ...,
    linewidths: Optional[Any] = ...,
    edgecolors: Optional[Any] = ...,
    label: Optional[Any] = ...,
    **kwds,
): ...
def draw_networkx_edges(
    G,
    pos,
    edgelist: Optional[Any] = ...,
    width: float = ...,
    edge_color: str = ...,
    style: str = ...,
    alpha: float = ...,
    arrowstyle: str = ...,
    arrowsize: int = ...,
    edge_cmap: Optional[Any] = ...,
    edge_vmin: Optional[Any] = ...,
    edge_vmax: Optional[Any] = ...,
    ax: Optional[Any] = ...,
    arrows: bool = ...,
    label: Optional[Any] = ...,
    node_size: int = ...,
    nodelist: Optional[Any] = ...,
    node_shape: str = ...,
    **kwds,
): ...
def draw_networkx_labels(
    G,
    pos,
    labels: Optional[Any] = ...,
    font_size: int = ...,
    font_color: str = ...,
    font_family: str = ...,
    font_weight: str = ...,
    alpha: float = ...,
    bbox: Optional[Any] = ...,
    ax: Optional[Any] = ...,
    **kwds,
): ...
def draw_networkx_edge_labels(
    G,
    pos,
    edge_labels: Optional[Any] = ...,
    label_pos: float = ...,
    font_size: int = ...,
    font_color: str = ...,
    font_family: str = ...,
    font_weight: str = ...,
    alpha: float = ...,
    bbox: Optional[Any] = ...,
    ax: Optional[Any] = ...,
    rotate: bool = ...,
    **kwds,
): ...
def draw_circular(G, **kwargs): ...
def draw_kamada_kawai(G, **kwargs): ...
def draw_random(G, **kwargs): ...
def draw_spectral(G, **kwargs): ...
def draw_spring(G, **kwargs): ...
def draw_shell(G, **kwargs): ...
