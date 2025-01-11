# Libraries
import sympy
from SM import photon, electron, positron, muon, antimuon, tau, antitau

# Define QED vertex
def QED_vertex(unicode):

    [e,Q,mu]=sympy.symbols('e,Q,\u03BC',real=True)
    gamma=sympy.Symbol('\u03B3', commutative=False)
    mu=sympy.Symbol(unicode)
    gamma_mu=gamma**mu

    return sympy.I*e*Q*gamma_mu

# Define Feynman diagram (tree level)
def QED_Feynman_diagram(propagated_particle):
    return QED_vertex('\u03BC')*propagated_particle.propagator()*QED_vertex('\u03BD')

# Tree-level amplitude
print('Case in which a photon propagates')
print(sympy.pretty(QED_Feynman_diagram(photon))) #Case in which a photon propagates
print('Case in which a fermion propagates')
print(sympy.pretty(QED_Feynman_diagram(electron))) #Case in which a fermion propagates. Try with muons or taus...