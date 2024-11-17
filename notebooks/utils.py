from hashlib import md5
from networkx import weisfeiler_lehman_graph_hash as wlhash, union_all
get_hash = lambda w: md5(str(w).encode("utf-8")).hexdigest()
check_soln = lambda soln, hash : get_hash(soln) == hash
DFA_hash = lambda A: wlhash(union_all([G:=A._get_digraph(),((X:=G.copy()).remove_node(A.initial_state) or X),((X:=G.copy()).remove_nodes_from(A.final_states) or X)],rename=('G1#', 'G2#','G3#')))
check_DFA_soln = lambda A, hash: DFA_hash(A.minify()) == hash
