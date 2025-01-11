# Libraries
import sympy

# Define particles
class particle:

    def __init__(self,name,mass,charge,spin,*args):
        self.quantum_numbers=(charge,spin,*args) # Define the charge of the particles in natural units and the spin in absolute value.
        self.mass=mass # MeV
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
    
    def external_legs(self,unicode):
        mu=sympy.Symbol(unicode, real=True)

# Create particles
photon = particle('photon',0,0,1) #In order to calculate amplitudes in QED, it is not necessary to include additional quantum numbers
electron = particle('electron',0.5,-1,0.5)
positron = particle('positron',0.5,1,0.5)
muon = particle('muon',105.7,-1,0.5)
antimuon = particle('anti-muon',105.7,1,0.5)
tau = particle('tau',1.777*10**(3),-1,0.5)
antitau = particle('anti-tau',1.777*10**(3),1,0.5)
higgs = particle('higgs', 126*10**(3),0,0)