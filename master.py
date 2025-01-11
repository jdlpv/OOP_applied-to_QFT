# Libraries
import sympy

# Define particles
class particle:

    def __init__(self,name,mass,charge,spin,*args):
        self.quantum_numbers=(charge,spin,*args) # Define the charge of the particles in natural units and the spin in absolute value.
        self.mass=mass # MeV (Recomendation)
        self.spin=spin # Do not enter natural numbers as float (example: spin 1 is valid, but not 1.0)
        self.charge=charge
        self.name=name
        
        if type(self.spin) == int:
            self.type="boson"
        elif type(self.spin) == float:
            self.type="fermion"

    def propagator(self,unicode1='\u03BC',unicode2='\u03BD'):

        [k,m,eta,alpha,epsilon]=sympy.symbols('k,m,\u03B7,\u03B1,\u03B5', real=True)
        mu=sympy.Symbol(unicode1, real=True)
        nu=sympy.Symbol(unicode2, real=True)
        gamma=sympy.Symbol('\u03B3', commutative=False)
        Minkowiski_metric=eta**(mu*nu)

        if (self.mass == 0) and (self.type == "boson"):
            return (sympy.I*Minkowiski_metric)/(k**2+sympy.I*epsilon)
        elif (self.mass != 0) and (self.type == "fermion"):
            return (sympy.I*(k**(alpha)*gamma**(alpha)+m))/(k**2-m**2+sympy.I*epsilon)
    
    def external_legs(self):
        [mu,nu]=[0,0]

# Create particles
photon = particle('photon',0,0,1) #In order to calculate amplitudes in QED, it is not necessary to include additional quantum numbers
electron = particle('electron',0.5,-1,0.5)
positron = particle('positron',0.5,1,0.5)

# Define QED vertex
def QED_vertex(unicode):

    [e,Q,mu]=sympy.symbols('e,Q,\u03BC',real=True)
    gamma=sympy.Symbol('\u03B3', commutative=False)
    mu=sympy.Symbol(unicode)
    gamma_mu=gamma**mu

    return sympy.I*e*Q*gamma_mu

# Define Feynman diagram
def QED_Feynman_diagram(propagated_particle):
    return QED_vertex('\u03BC')*propagated_particle.propagator()*QED_vertex('\u03BD')

# Tree-level amplitude
print('Case in which a photon propagates')
print(sympy.pretty(QED_Feynman_diagram(photon))) #Case in which a photon propagates
print('Case in which a fermion propagates')
print(sympy.pretty(QED_Feynman_diagram(electron))) #Case in which a fermion propagates. Note that QED_Feynman_diagram(positron) produces the same result.