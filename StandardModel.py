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

# Bosons
photon = particle('photon',0,0,1)
higgs = particle('higgs',126*10**(3),0,0) # Consider the unitary gauge
Z_boson = particle('Z boson',91.2*10**(3),0,1)
W_minus_boson = particle('W- boson',80.4*10**(3),-1,1) # W- and W+ masses might differ
W_plus_boson = particle('W+ boson',80.4*10**(3),11,1)

# Fermions

#Leptons
electron = particle('electron',0.5,-1,1/2)
positron = particle('positron',0.5,1,1/2)
muon = particle('muon',105.7,-1,1/2)
antimuon = particle('anti-muon',105.7,1,1/2)
tau = particle('tau',1.777*10**(3),-1,1/2)
anti_tau = particle('anti-tau',1.777*10**(3),1,1/2)
electron_neutrino = particle('electron neutrino',"Unknown",0,1/2)
muon_neutrino = particle('muon neutrino',"Unknown",0,1/2)
tau_neutrino = particle('tau neutrino',"Unknown",0,1/2)
anti_electron_neutrino = particle('anti-electron neutrino',"Unknown",0,1/2)
anti_muon_neutrino = particle('anti-muon neutrino',"Unknown",0,1/2)
anti_tau_neutrino = particle('anti-tau neutrino',"Unknown",0,1/2)

# Quarks
red_up_quark = particle('red up quark',2.3,2/3,1/2,"color red")
anti_red_up_quark = particle('anti-red up quark',2.3,-2/3,1/2,"color anti-red")
green_up_quark = particle('green up quark',2.3,2/3,1/2,"color green")
anti_green_up_quark = particle('anti-green up quark',2.3,-2/3,1/2,"color anti-green")
blue_up_quark = particle('blue up quark',2.3,2/3,1/2,"color blue")
anti_blue_up_quark = particle('anti-blue up quark',2.3,-2/3,1/2,"color anti-blue")
red_down_quark = particle('red down quark',4.8,-1/3,1/2,"color red")
anti_red_down_quark = particle('anti-red down quark',4.8,1/3,1/2,"color anti-red")
green_down_quark = particle('green down quark',4.8,-1/3,1/2,"color green")
anti_green_down_quark = particle('anti-green down quark',4.8,1/3,1/2,"color anti-green")
blue_down_quark = particle('blue down quark',4.8,-1/3,1/2,"color blue")
anti_blue_down_quark = particle('anti-blue down quark',4.8,1/3,1/2,"color anti-blue")
red_charm_quark = particle('red charm quark',1.275*10**(3),2/3,1/2,"color red")
anti_red_charm_quark = particle('anti-red charm quark',1.275*10**(3),-2/3,1/2,"color anti-red")
green_charm_quark = particle('green charm quark',1.275*10**(3),2/3,1/2,"color green")
anti_green_charm_quark = particle('anti-green charm quark',1.275*10**(3),-2/3,1/2,"color anti-green")
blue_charm_quark = particle('blue charm quark',1.275*10**(3),2/3,1/2,"color blue")
anti_blue_charm_quark = particle('anti-blue charm quark',1.275*10**(3),-2/3,1/2,"color anti-blue")